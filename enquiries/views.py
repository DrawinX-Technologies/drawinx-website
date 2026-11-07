
import json
import logging
from urllib.request import Request, urlopen

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import EnquiryForm

logger = logging.getLogger(__name__)


def send_enquiry_notification(enquiry):
    if not settings.BREVO_API_KEY:
        raise RuntimeError("Brevo API key is not configured.")

    payload = {
        "sender": {
            "name": "DrawinX Technologies",
            "email": settings.DEFAULT_FROM_EMAIL,
        },
        "to": [
            {
                "email": settings.CONTACT_EMAIL,
            }
        ],
        "replyTo": {
            "email": enquiry.email,
            "name": enquiry.name,
        },
        "subject": f"New DrawinX website enquiry: {enquiry.service}",
        "textContent": (
            f"Name: {enquiry.name}\n"
            f"Email: {enquiry.email}\n"
            f"Organization: {enquiry.organization}\n\n"
            f"{enquiry.message}"
        ),
    }

    request = Request(
        "https://api.brevo.com/v3/smtp/email",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "accept": "application/json",
            "api-key": settings.BREVO_API_KEY,
            "content-type": "application/json",
        },
        method="POST",
    )

    with urlopen(request, timeout=10) as response:
        if response.status not in (200, 201, 202):
            raise RuntimeError(
                f"Brevo returned HTTP {response.status}"
            )


@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)

        # Honeypot spam check
        if form.is_valid():
            if form.cleaned_data.get("website"):
                messages.success(
                    request,
                    "Thanks. Your enquiry has been received."
                )
                return redirect("contact")

            enquiry = form.save()

            # Email notification is independent of database storage.
            try:
                send_enquiry_notification(enquiry)
            except Exception:
                logger.exception(
                    "Failed to send DrawinX enquiry notification."
                )

            messages.success(
                request,
                "Thanks — your enquiry has been received. "
                "We'll review it and follow up using the email you provided."
            )
            return redirect("contact")

    else:
        form = EnquiryForm()

    return render(
        request,
        "pages/contact.html",
        {
            "page_title": "Contact",
            "form": form,
        }
    )

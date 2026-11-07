from config import settings
from django.contrib import messages
from django.core.mail import EmailMessage, get_connection
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from .forms import EnquiryForm

@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        # A filled honeypot is treated as spam without revealing the check.
        if form.is_valid():
            if form.cleaned_data.get("website"):
                messages.success(request, "Thanks. Your enquiry has been received.")
                return redirect("contact")
            enquiry = form.save()
            # In development this prints to the terminal. Configure SMTP in production
            # before relying on email notifications; database storage is independent.
            try:

                connection = get_connection(
                    backend=settings.EMAIL_BACKEND,
                    fail_silently=True
                )
                
                email = EmailMessage(
                    subject=f"New DrawinX website enquiry: {enquiry.service}",
                    body=(f"Name: {enquiry.name}\nEmail: {enquiry.email}\nOrganization: {enquiry.organization}\n\n{enquiry.message}"),
                    from_email=settings.DEFAULT_FROM_EMAIL, to=[settings.CONTACT_EMAIL], connection=connection
                )
                
                email.send()
            except Exception:
                pass
            messages.success(request, "Thanks — your enquiry has been received. We'll review it and follow up using the email you provided.")
            return redirect("contact")
    else:
        form = EnquiryForm()
    return render(request, "pages/contact.html", {"page_title": "Contact", "form": form})
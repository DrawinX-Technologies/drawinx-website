from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={"tabindex": "-1", "autocomplete": "off"}))

    class Meta:
        model = Enquiry
        fields = ["name", "email", "organization", "service", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "autocomplete": "name", "placeholder": "Your name", "minlength": 2}),
            "email": forms.EmailInput(attrs={"class": "form-control", "autocomplete": "email", "placeholder": "you@example.com"}),
            "organization": forms.TextInput(attrs={"class": "form-control", "autocomplete": "organization", "placeholder": "Organization (optional)"}),
            "service": forms.Select(attrs={"class": "form-select"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Tell us about the project...", "minlength": 10}),
        }

    def clean_name(self):
        value = self.cleaned_data["name"].strip()
        if len(value) < 2: raise forms.ValidationError("Please enter at least 2 characters.")
        return value

    def clean_message(self):
        value = self.cleaned_data["message"].strip()
        if len(value) < 10: raise forms.ValidationError("Please provide a little more detail (at least 10 characters).")
        return value

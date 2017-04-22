from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label="Your Name")
    contact_email = forms.EmailField(required=True, label="Your Email")
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="What You want Us To know!"
    )

# https://hellowebapp.com/news/tutorial-setting-up-a-contact-form-with-django/

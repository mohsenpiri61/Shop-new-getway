from django import forms
from .models import ContactModel, NewsLetter


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ["subject", "full_name", "email", "phone_number", "content"]


class NewsLetterForm(forms.ModelForm):
    

    class Meta:
        model = NewsLetter
        fields = ['email']
        

    def save(self, commit=True):
        newsletter, created = NewsLetter.objects.get_or_create(email=self.cleaned_data.get("email"))
        return newsletter

from django.views.generic import TemplateView, CreateView
from .forms import ContactForm, NewsLetterForm
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy



class IndexView(TemplateView):
    template_name = "website/index.html"


class ContactView(TemplateView):
    template_name = "website/contact.html"


class AboutView(TemplateView):
    template_name = "website/about.html"


class SendTicketView(CreateView):
    http_method_names = ['post']
    form_class = ContactForm

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'تیکت شما با موفقیت ثبت شد ')
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('website:contact')  


class NewsletterView(CreateView):
    http_method_names = ['post']
    form_class = NewsLetterForm
    success_url = '/'

    def form_valid(self, form):
        # handle successful form submission
        messages.success(
            self.request, '.ثبت نام شما برای دریافت اخبار جدید انجام شد')
        return super().form_valid(form)



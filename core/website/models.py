from django.db import models
from django.contrib.auth import get_user_model

# fetching user model
User = get_user_model()


# defining the status of items to be saved or released
class ContactModel(models.Model):
    full_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(default=None)
    phone_number = models.CharField(max_length=200, default=None)
    subject = models.CharField(max_length=200, default=None)
    content = models.TextField(max_length=700)
    is_seen = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.full_name


class NewsLetter(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

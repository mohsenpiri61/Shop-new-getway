from django.contrib import admin
from website.models import ContactModel, NewsLetter


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('subject', 'email', 'created_date', 'is_seen')
    list_filter = ('email',)
    search_fields = ('email',)


admin.site.register(ContactModel, ContactAdmin)
admin.site.register(NewsLetter)

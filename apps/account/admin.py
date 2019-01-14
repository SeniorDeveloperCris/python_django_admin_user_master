from django.contrib import admin

from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at','firstname','lastname')
    list_filter = ('created_at',)


admin.site.register(Subscriber, SubscriberAdmin)

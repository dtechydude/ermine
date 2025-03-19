from django.contrib import admin
from .models import SubscriberList
from import_export.admin import ImportExportModelAdmin


class SubscriberListAdmin(ImportExportModelAdmin, admin.ModelAdmin):
           
    # list_display=('profile__user', 'profile__code', 'profile__gender', 'profile__state')
    # list_filter  = ['profile__state',]
    # search_fields = ('profile__user__username', 'profile__code', 'profile__state')

    list_display=('job_status',)
    list_filter  = ['job_status',]
    search_fields = ('job_status',)

admin.site.register(SubscriberList, SubscriberListAdmin)

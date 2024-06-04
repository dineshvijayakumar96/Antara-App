from django.contrib import admin
from .models import Inquiry, AboutusInquiry, ContactusInquiry, ServiceDCInquiry, ServiceDPInquiry, ServiceHHInquiry, ServiceKWInquiry, ServiceNCInquiry, ServiceNDCInquiry, ServiceSCInquiry, ServiceWWInquiry, ServiceYTInquiry

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'country', 'timestamp')
    search_fields = ('name', 'email', 'country', 'timestamp')
    list_filter = ('gender', 'country', 'aboutus', 'timestamp')

admin.site.register(Inquiry, InquiryAdmin)

class AboutusInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'country', 'timestamp')
    search_fields = ('name', 'email', 'country', 'timestamp')
    list_filter = ('gender', 'country', 'aboutus', 'timestamp')

admin.site.register(AboutusInquiry, AboutusInquiryAdmin)

class ContactusInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'country', 'timestamp')
    search_fields = ('name', 'email', 'country', 'timestamp')
    list_filter = ('gender', 'country', 'aboutus', 'timestamp')

admin.site.register(ContactusInquiry, ContactusInquiryAdmin)

class ServiceDCInquiryAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'timestamp')
    search_fields = ('firstname', 'lastname', 'email', 'timestamp')
    # You can add more fields to list_filter if needed
    list_filter = ('firstname', 'lastname', 'email', 'timestamp')

admin.site.register(ServiceDCInquiry, ServiceDCInquiryAdmin)

class ServiceDPInquiryAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'timestamp')
    search_fields = ('firstname', 'lastname', 'email', 'timestamp')
    # You can add more fields to list_filter if needed
    list_filter = ('firstname', 'lastname', 'email', 'timestamp')

admin.site.register(ServiceDPInquiry, ServiceDPInquiryAdmin)

class ServiceHHInquiryAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'timestamp')
    search_fields = ('firstname', 'lastname', 'email', 'timestamp')
    # You can add more fields to list_filter if needed
    list_filter = ('firstname', 'lastname', 'email', 'timestamp')

admin.site.register(ServiceHHInquiry, ServiceHHInquiryAdmin)

class ServiceKWInquiryAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'timestamp')
    search_fields = ('firstname', 'lastname', 'email', 'timestamp')
    # You can add more fields to list_filter if needed
    list_filter = ('firstname', 'lastname', 'email', 'timestamp')

admin.site.register(ServiceKWInquiry, ServiceKWInquiryAdmin)

class ServiceNCInquiryAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'timestamp')
    search_fields = ('firstname', 'lastname', 'email', 'timestamp')
    # You can add more fields to list_filter if needed
    list_filter = ('firstname', 'lastname', 'email', 'timestamp')

admin.site.register(ServiceNCInquiry, ServiceNCInquiryAdmin)

class ServiceNDCInquiryAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'timestamp')
    search_fields = ('firstname', 'lastname', 'email', 'timestamp')
    # You can add more fields to list_filter if needed
    list_filter = ('firstname', 'lastname', 'email', 'timestamp')

admin.site.register(ServiceNDCInquiry, ServiceNDCInquiryAdmin)

class ServiceSCInquiryAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'timestamp')
    search_fields = ('firstname', 'lastname', 'email', 'timestamp')
    # You can add more fields to list_filter if needed
    list_filter = ('firstname', 'lastname', 'email', 'timestamp')

admin.site.register(ServiceSCInquiry, ServiceSCInquiryAdmin)

class ServiceWWInquiryAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'timestamp')
    search_fields = ('firstname', 'lastname', 'email', 'timestamp')
    # You can add more fields to list_filter if needed
    list_filter = ('firstname', 'lastname', 'email', 'timestamp')

admin.site.register(ServiceWWInquiry, ServiceWWInquiryAdmin)

class ServiceYTInquiryAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'timestamp')
    search_fields = ('firstname', 'lastname', 'email', 'timestamp')
    # You can add more fields to list_filter if needed
    list_filter = ('firstname', 'lastname', 'email', 'timestamp')

admin.site.register(ServiceYTInquiry, ServiceYTInquiryAdmin)
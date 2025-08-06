from django.contrib import admin
from .models import Applicant

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'role', 'submitted_at')
    search_fields = ('name', 'email')

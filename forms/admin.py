from django.contrib import admin
from .models import Form, Submission, SubmissionEntry

# Register your models here.


class SubmissionInline(admin.TabularInline):
    model = Submission
    extra = 3


class FormAdmin(admin.ModelAdmin):
    inlines = [SubmissionInline]


admin.site.register(Form, FormAdmin)


class SubmissionEntryInline(admin.TabularInline):
    model = SubmissionEntry
    extra = 0


class SubmissionAdmin(admin.ModelAdmin):
    inlines = [SubmissionEntryInline]


admin.site.register(Submission, SubmissionAdmin)

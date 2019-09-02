from django.contrib import admin
from .models import Form, Submission, SubmissionEntry

# Register your models here.

admin.site.register(Form)
admin.site.register(Submission)
admin.site.register(SubmissionEntry)

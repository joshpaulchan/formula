import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import FormRepository, SubmissionRepository
from .usecases import SubmitFormUseCase, SubmissionIsNotFalsey

# Create your views here.
form_repository = FormRepository()
submission_repository = SubmissionRepository()
submission_validator = SubmissionIsNotFalsey()
submit_form_use_case = SubmitFormUseCase(
    form_repository=form_repository,
    submission_repository=submission_repository,
    submission_validator=submission_validator,
)


def submit_form(request, form_id):
    entries = json.loads(request.body)
    return HttpResponse(submit_form_use_case(form_id, entries))

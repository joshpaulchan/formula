from django.db import models

from . import mappers

# Create your models here.


class Form(models.Model):
    name = models.CharField(max_length=144)
    created_at = models.DateTimeField("date created")

    def __str__(self):
        return f"Form{{id={self.id} name={self.name}}}"


class Submission(models.Model):
    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE,
        related_name="submissions",
        related_query_name="submission",
    )
    created_at = models.DateTimeField("date created")

    def __str__(self):
        return f"Submission{{form={self.form_id} id={self.id}}}"


class SubmissionEntry(models.Model):
    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE,
        related_name="entries",
        related_query_name="entry",
    )
    field = models.CharField(max_length=144)
    value = models.CharField(max_length=144)

    def __str__(self):
        return f"SubmissionEntry{{submission={self.submission_id} {self.field}={self.value}}}"


class FormRepository:
    def get_by_id(self, form_id):
        try:
            model = Form.objects.get(pk=form_id)
        except Form.DoesNotExist:
            return None
        return mappers.FormMapper.from_model(model)


class SubmissionRepository:
    def get_by_id(self, submission_id):
        try:
            mappers.SubmissionMapper.from_model(
                Submission.objects.get(pk=submission_id)
            )
        except Form.DoesNotExist:
            return None

    def create(self, submission):
        try:
            form_model = Form.objects.get(pk=submission.form.id)
        except Form.DoesNotExist:
            return False

        model = mappers.SubmissionMapper.to_model(submission)
        model.save()
        form_model.submissions.add(model)

        for field, value in submission.entries.items():
            model.entries.create(field=field, value=value)

        return mappers.SubmissionMapper.from_model(model)

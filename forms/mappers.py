from . import models, domain


class FormMapper:
    @staticmethod
    def from_model(form_model):
        return domain.Form(
            id=form_model.id, name=form_model.name, created_at=form_model.created_at
        )


class SubmissionMapper:
    @staticmethod
    def from_model(submission_model):
        return domain.Submission(
            form=FormMapper.from_model(submission_model.form),
            entries={
                field: value
                for field, value in map(
                    lambda entry: (entry.field, entry.value),
                    submission_model.entries.all(),
                )
            },
        )

    @staticmethod
    def to_model(submission):
        form_id = submission.form.id if submission.form else None
        return models.Submission(form_id=form_id, created_at=submission.created_at)

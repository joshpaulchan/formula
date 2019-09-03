from .domain import Submission


class SubmissionIsNotFalsey:
    def validate(self, submission):
        return bool(submission)


class SubmitFormUseCase:
    def __init__(self, form_repository, submission_repository, submission_validator):
        self.form_repository = form_repository
        self.submission_repository = submission_repository
        self.submission_validator = submission_validator

    def __call__(self, form_id, entries):
        form = self.form_repository.get_by_id(form_id)
        if not form:
            raise KeyError(f"Form with id:{form_id} does not exist.")

        submission = Submission.for_form(form)
        submission.entries.update(entries)

        if not self.submission_validator.validate(submission):
            return False

        return self.submission_repository.create(submission)

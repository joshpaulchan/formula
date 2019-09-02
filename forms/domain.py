import dataclasses
import datetime
import typing


@dataclasses.dataclass()
class Form:
    id: typing.Optional[int] = dataclasses.field(default=None)
    name: str = dataclasses.field(default="")
    created_at: datetime.datetime = dataclasses.field(
        default_factory=datetime.datetime.utcnow
    )


@dataclasses.dataclass()
class Submission:
    id: typing.Optional[int] = dataclasses.field(default=None)
    form: Form = dataclasses.field(default=None)
    entries: typing.Mapping = dataclasses.field(default_factory=dict)
    created_at: datetime.datetime = dataclasses.field(
        default_factory=datetime.datetime.utcnow
    )

    @classmethod
    def for_form(cls, form):
        return cls(form=form)

from dataclasses import dataclass
from typing import List


@dataclass
class ValidationError:
    field: str
    message: str


class ConfigValidator:

    REQUIRED_FIELDS = [
        "BASE_CURRENCY",
    ]

    def __init__(self, config):

        self.config = config

    def validate(self):

        errors: List[ValidationError] = []

        for field in self.REQUIRED_FIELDS:

            value = getattr(self.config, field, None)

            if value in (None, "", []):
                errors.append(
                    ValidationError(
                        field=field,
                        message="Value is required."
                    )
                )

        return errors

    def validate_or_raise(self):

        errors = self.validate()

        if errors:

            formatted = "\n".join(
                f"{e.field}: {e.message}"
                for e in errors
            )

            raise ValueError(
                "Invalid configuration:\n"
                + formatted
            )

        return True

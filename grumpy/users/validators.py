from django.conf import settings
from django.core.exceptions import ValidationError

from zxcvbn import zxcvbn


class LengthPasswordValidator:
    """
    Validates the password length is inside a range.
    """

    def __init__(
        self,
        min_length=settings.PASSWORD_MIN_LENGTH,
        max_length=settings.PASSWORD_MAX_LENGTH,
    ):
        assert (
            max_length > min_length and min_length > 0 and max_length > 0
        ), "Invalid LengthPasswordValidator"
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, password, user=None):

        password_length = len(password)

        if password_length < self.min_length:
            raise ValidationError(
                f"This password is too short.  It must contain at least {self.min_length} characters",
                code="password_too_short",
            )

        elif password_length > self.max_length:
            raise ValidationError(
                f"This password is too long.  It must contain at most {self.max_length} characters",
                code="password_too_long",
            )

    def get_help_text(self):
        return f"The password must contain between {self.min_length} and {self.max_length} characters."


class StrengthPasswordValidator:
    """
    Validates a password using the zxcvbn strength estimator.
    strength is set in __init__; possible values are:

    * 0 # too guessable: risky password. (guesses < 10^3)
    * 1 # very guessable: protection from throttled online attacks. (guesses < 10^6)
    * 2 # somewhat guessable: protection from unthrottled online attacks. (guesses < 10^8)
    * 3 # safely unguessable: moderate protection from offline slow-hash scenario. (guesses < 10^10)
    * 4 # very unguessable: strong protection from offline slow-hash scenario. (guesses >= 10^10)
    """

    def __init__(self, strength=settings.PASSWORD_STRENGTH):
        assert 0 <= strength <= 4, "Invalid StrongPasswordValidator strength."
        self.strength = strength

    def validate(self, password, user=None):

        user_inputs = (
            [
                user.email,
                user.username,
            ]
            if user is not None
            else []
        )

        password_results = zxcvbn(password, user_inputs=user_inputs)

        if password_results["score"] < self.strength:
            error_msg = "The password must not be weak."
            # error_msg += password_results["feedback"]["warning"]
            # error_msg += "; ".join(password_results["feedback"]["suggestions"])
            raise ValidationError(error_msg, code="password_too_weak")

    def get_help_text(self):
        return f"The password must be strong."

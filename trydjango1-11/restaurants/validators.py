from django.core.exceptions import ValidationError


# usually use validate_(for general validation not clean_(method in form)
def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )


def validate_email(value):
    email = value
    if '.edu' in email:
        raise ValidationError('We do not accept edu emails')


CATEGORIES = ['Mexican', 'Asian', 'American', 'Whatever']


def validate_category(value):
    cat = value.capitalize()
    if cat not in CATEGORIES:
        raise ValidationError(f'{value} not in a valid category')

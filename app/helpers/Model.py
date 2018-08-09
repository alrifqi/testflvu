from mongokit import ValidationError

def max_length(length):
    def validate(value):
        if len(value) <= length:
            return True
        raise ValidationError('%s must be at most {} characters long'.format(length))

    return validate
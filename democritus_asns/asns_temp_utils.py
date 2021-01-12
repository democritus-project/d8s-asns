import functools


def standardize_asn(func):
    """Standardize the first argument as an ASN."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        from .asns import asn_standardize

        first_arg = args[0]
        other_args = args[1:]

        standardized_first_arg = asn_standardize(first_arg)
        return func(standardized_first_arg, *other_args, **kwargs)

    return wrapper


def stringify_first_arg(func):
    """Convert the first argument to a string."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        first_arg_string = str(args[0])
        other_args = args[1:]
        return func(first_arg_string, *other_args, **kwargs)

    return wrapper

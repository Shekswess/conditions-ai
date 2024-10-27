"""Helper functions for the Conditions AI project."""


def convert_to_bool(value: str) -> bool:
    """Convert a string 'True' or 'False' to a boolean value.

    Parameters
    ----------
    value : str
        The value to convert.

    Returns
    -------
    bool
        The boolean value.
    """

    if value == "True":
        return True
    elif value == "False":
        return False
    else:
        raise ValueError(f"Invalid boolean value: {value}")

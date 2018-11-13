from CashInterpreter import return_value


def custom_command(*args):
    """
    This Is A Sample Custom Command

    Usage:
        custom_command
    """
    return_value.append("hello world")

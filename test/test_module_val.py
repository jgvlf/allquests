import allquests


def test_module_name_validation() -> None:
    if allquests.__name__ != "allquests":
        msg: str = f'Incorrect module name: {__package__}. Wouldn\'t be "allquests" the correct name?'
        raise NameError(msg)

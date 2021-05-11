
from demo_config_decorator.config import add_settings

@add_settings
def say_hello(name, *, settings):
    """
    Say hello.

    Note the '*' in the parameter list. 
    This means that everything to the right of the '*' must be explicitly mentioned when calling the function.
    """
    return f"Hello, {name}! This is a date from the settings: {settings.get('date1')}."

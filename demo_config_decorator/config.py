import yaml
import pkgutil
import functools

def add_settings(func):
    """
    Decorator to add settings.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        if 'settings' not in kwargs:
            kwargs['settings'] = read_config()
        
        return func(*args, **kwargs)
 
    return wrapper


def read_config(name='base.yaml'):
    """Return the project configuration settings.

    Returns:
        settings (dict): Project settings
    """

    setting_bytes = pkgutil.get_data(__name__, "conf/%s" % name)    
    return yaml.safe_load(setting_bytes)

# Configuration handling in machine learning projects

This repo is a demo on reading configuration files that are included in a python package and added to the scope of functions using decorators.

## Problem

Build and maintain a couple of machine learning projects, and you'll realise some good configuration handling is crucial.

- How to package the config along with your code
- How to make the configuration settings available where you need them without being too verbose
- How to support auto-reloading

You can solve these problems elegantly with `pkgutils` and a decorator.

## Solution

Add your `conf` folder inside your python package. Ours will be called `demo_config_decorator`:

```
.
├── MANIFEST.in
├── README.md
├── demo_config_decorator
│   ├── __init__.py
│   ├── conf                  <----- Folder containing configuration.
│   │   └── base.yaml
│   ├── config.py
│   └── demo.py
└── setup.py
```

Add a `MANIFEST.in` in the root of your repository like so:

```
demo_config_decorator/conf/*.yaml
```

Make sure your package includes package data by updating `setup.py` with:

```python
# setup.py
setup(
    # ...
    include_package_data=True,
    # ...
)
```

Then you can read your configuration using [`pkgutil`](https://docs.python.org/3/library/pkgutil.html) anywhere inside your package:

```python
# config.py
import pkgutil

def read_config():
    c = pkgutil.get_data(__name__, "conf/base.yaml")    
    return yaml.safe_load(c)
```

Now in any python file inside your package, you can add:

```python
from demo_config_fsdfs.config import read_config
SETTINGS = read_config()
```

The problem however is that this does not [auto-reload](https://godatadriven.com/blog/write-less-terrible-code-with-jupyter-notebook/), which is useful when you are using jupyter notebooks. This means that if you update the config, you'll need to restart the kernel to reload the `SETTINGS` global. You can fix this by adding a `settings = read_config()` inside each of your functions that need it.

That's a bit verbose perhaps, so you could choose to add a [decorator](https://realpython.com/primer-on-python-decorators):

```python
# config.py
import functools

def add_settings(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if 'settings' not in kwargs:
            kwargs['settings'] = read_config()
        return func(*args, **kwargs)
    return wrapper
```

Which you can use like this:

```python
# demo.py
@add_settings
def say_hello(name, *, settings):
    return f"Hello, {name}! This is a date from the settings: {settings.get('date1')}."

say_hello('World')
```

This approach is nice because:

1) The decorator will fill in the `settings` argument if the user does not supply it.
1) The `*, settings` in `say_hello()` [enforces use of a keyword argument](https://stackoverflow.com/questions/2965271/forced-naming-of-parameters-in-python) for `settings`, preventing errors.
1) You can explicitly pass a different set of `settings` to the function using a named argument, which is useful for unit testing or in production.
1) The approach supports auto-reloading (because the `read_config()` file is called on every function call)
1) Because the config is packaged along with your code, it is easy to distribute.

To get started with a working example, you can fork and clone this repository.

If this approach doesn't suit your needs, consider adding the parts of the config that you need inside a function as an explicit parameter. That's the approach [gin-config](https://github.com/google/gin-config) takes, a python package built by google explicitly for machine learning configuration management. They're also a great [intro to gin](https://calmcode.io/gin/intro-to-gin.html) video  by [calmcode](https://calmcode.io/).


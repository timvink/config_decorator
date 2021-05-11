
from demo_config_decorator.config import read_config
from demo_config_decorator.demo import say_hello


def test_read_config():
    assert len(read_config()) > 0

def test_say_hello():

    assert say_hello('world') == f"Hello, world! This is a date from the settings: 2020-05-07."

    settings = {'date1' : '2021-05-11'}
    assert say_hello('there', settings = settings) == f"Hello, there! This is a date from the settings: 2021-05-11."




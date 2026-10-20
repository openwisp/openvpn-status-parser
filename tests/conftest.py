from py.path import local
from pytest import fixture


@fixture
def datadir():
    return local(__file__).dirpath("data")

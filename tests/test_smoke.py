import sys

from mlops_project import __version__, hello


def test_hello():
    assert hello() == "mlops project is ready"


def test_version_is_set():
    assert __version__


def test_python_version():
    """Проверка версии Python окружения."""
    assert sys.version_info >= (3, 10)

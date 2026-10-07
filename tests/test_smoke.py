from mlops_project import __version__, hello


def test_hello():
    assert hello() == "mlops project is ready"


def test_version_is_set():
    assert __version__

import pytest

@pytest.fixture()
def here():
    print('he')
    yield
    print("\nafter")


def test_demo(here):
    assert 2==3
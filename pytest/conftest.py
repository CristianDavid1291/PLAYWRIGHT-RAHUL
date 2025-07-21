import pytest


@pytest.fixture(scope="session")
def pre_work():
    print("Pre-work setup complete")
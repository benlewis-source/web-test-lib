import pytest

from pages.home import HomePage

BASE_URL = "https://jupiter.cloud.planittesting.com"


@pytest.fixture(scope="function")
def jupiter_toys(page):
    yield HomePage(page, BASE_URL)

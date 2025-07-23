import sys
import os
import pytest

# Agregar el directorio padre al Python path para poder importar módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils import Base

@pytest.fixture(params=Base.get_credentials(), ids=lambda x: x['username'])
def user_data(request):
    return request.param

@pytest.fixture()
def browser_instance(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
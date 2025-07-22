import pytest
from utils.base import Base

@pytest.fixture(params=Base.get_credentials(), ids=lambda x: x['username'])
def user_data(request):
    return request.param
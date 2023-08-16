import pytest
from common.api.trainer import TrainerApi

@pytest.fixture(scope='session')
def api():
    '''
    Фикстура с базовым API
    '''
    api = TrainerApi()
    yield api
import pytest
from common.api.trainer import TrainerApi
from common.helper.schema.trainer import valid_trainer, error_trainer
from pytest_voluptuous import S
from .data import *


class TestTrainer():
    '''
    Тесты тренера
    '''
    CASE = [
        {'id': trainer_id, 'status_code': 200, 'schema': valid_trainer},
        {'id': 0, 'status_code': 400, 'schema': error_trainer},
        {'id': 'abc', 'status_code': 404, 'schema': error_trainer},
        {'id': '$#', 'status_code': 404, 'schema': error_trainer}
    ]

    def test_get_trainer(self):
        '''
        Получение тренера по trainer_id
        '''
        trainer_api = TrainerApi()
        response = trainer_api.get_trainer(trainer_id=trainer_id)

        trainer_api.status_code_should_be(expected_code=200)

        assert True, ''

    
    @pytest.mark.parametrize('case', CASE)
    def test_get_trainer(self, case, api):
        '''
        Получение тренера по trainer_id
        Проверка правильности структуры структуры
        '''
        response = api.get_trainer(trainer_id=case['id'])

        api.status_code_should_be(expected_code=case['status_code'])

        if response.response.status_code in [400, 404]:
            assert S(case['schema']) == response.response.json()
            assert response.response.json()['message'] == 'Тренер отсутствует'
        else:
            assert S(case['schema']) == response.response.json()
        
'''
Модуль для работы с тренерами
'''
from common.api.basic import Api
# from my_secrets import trainer_id

class TrainerApi(Api):
    '''
    Методы тренера
    '''
    def get_trainer(self, trainer_id: int = None):
        '''
        Получение тренера
        '''
        url=f'{self.url}/trainers'
        return self.get(url=url, params={'trainer_id': trainer_id})
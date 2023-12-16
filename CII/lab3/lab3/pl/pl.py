# coding: utf-8
from swiplserver import PrologMQI
from pl.services import (update_info, init_patterns,
                         form_query, questions, examples)


class PrologWorker:

    def __init__(self, path):
        mqi = PrologMQI()
        self.pl = mqi.create_thread()
        self.load_knowledge_by_path(path)
        self.info = [[], [], []]

    def load_knowledge_by_path(self, path):
        self.pl.query(f'consult("{path}")')

    def execute(self, query: str):
        gen = self.pl.query(query)
        if not gen:
            print('Запрос не вернул никаких результатов. Перепроверьте info:\n'
                  'Ваш герой: {0}\n'
                  'Ваша команда: {1}\n'
                  'Ваши артефакты: {2}'.format(
                    ''.join(self.info[0]),
                    ', '.join(self.info[1]),
                    ', '.join(self.info[2])))
            return None
        for answer in gen:
            yield answer

    def run(self):
        while True:
            info_type = input('Выберите, что хотите ввести: '
                              'информация (i) или запрос (q): ')
            if info_type not in ('i', 'q'):
                print('Неверный вариант - выберите i или q.')
                continue
            elif info_type == 'i':
                string = input('Введите ваш запрос. Примеры:\n{}\n'
                               .format('\n'.join(examples)))
                self.info = update_info(string, self.info)
            else:
                string = input(
                    'Введите ваш запрос. Примеры:\n{}\n'.format(
                        '\n'.join(questions.keys())
                    )
                )
                query = form_query(string, self.info)
                for answer in self.execute(query):


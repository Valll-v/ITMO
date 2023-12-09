from swiplserver import PrologMQI, PrologThread


class PrologWorker:

    def __init__(self, knowledge=None, path=None):
        mqi = PrologMQI()
        self.pl = mqi.create_thread()
        self.load_knowledge(knowledge, path)
        self.executors = {}

    def load_knowledge(self, knowledge: str, path: str):
        if knowledge:
            # TODO: Реализовать чтение базы знаний напрямую, а не из файла
            pass
        if path:
            self.pl.query(f'consult("{path}")')

    def execute(self, query: str):
        for answer in self.pl.query(query):
            yield answer

    def run(self):
        for i in self.execute('perfect_team(X,Y,Z)'):
            print(i)


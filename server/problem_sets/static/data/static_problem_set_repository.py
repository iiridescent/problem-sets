from problem_sets.static.data.sqlite.static_problem_set_sqlite_repository import StaticProblemSetSQLiteRepository
from problem_sets.static.data.static_problem_set_data_source import StaticProblemSetDataSource
from problem_sets.static.data.static_problem_set_entity import StaticProblemSetEntity


class StaticProblemSetRepository(StaticProblemSetDataSource):

    def __init__(self, sqlite_repo: StaticProblemSetSQLiteRepository):
        self.sqlite_repo = sqlite_repo

    def create(self, data: StaticProblemSetEntity):
        return self.sqlite_repo.create(data)

    def get(self, id: str) -> StaticProblemSetEntity:
        return self.sqlite_repo.get(id)

    def delete(self, id: str):
        return self.sqlite_repo.delete(id)

    def update(self, id: str, data: StaticProblemSetEntity):
        return self.sqlite_repo.update(id, data)

    def list(self):
        return self.sqlite_repo.list()

    def check_id_available(self, id: str) -> bool:
        return self.sqlite_repo.check_id_available(id)

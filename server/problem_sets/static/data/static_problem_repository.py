from problem_sets.static.data.static_problem_data_source import StaticProblemDataSource
from problem_sets.static.static_problem_entity import StaticProblemEntity


class StaticProblemRepository(StaticProblemDataSource):

    def __init__(self, sqlite_repo):
        self.sqlite_repo = sqlite_repo

    def create(self, data: StaticProblemEntity):
        return self.sqlite_repo.create(data)

    def get(self, id: int) -> StaticProblemEntity:
        return self.sqlite_repo.get(id)

    def delete(self, id: int):
        return self.sqlite_repo.delete(id)

    def update(self, id: int, data: StaticProblemEntity):
        return self.sqlite_repo.update(id, data)

    def pick_problem_from_set(self, set_id: str):
        return self.sqlite_repo.pick_problem_from_set(set_id)

    def list_problems_from_set(self, set_id: str):
        return self.sqlite_repo.list_problems_from_set(set_id)

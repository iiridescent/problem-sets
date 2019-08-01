import os
from typing import List

from problem_sets.static.data import data_util, data_manager
from problem_sets.static.data.sqlite.static_content_sqlite_repository import StaticContentRow
from problem_sets.static.data.sqlite.static_problem_sqlite_repository import StaticProblemSQLiteRepository, \
    StaticProblemRow
from problem_sets.static.data.static_content_entity import StaticContentEntity, StaticContentEntityType
from problem_sets.static.data.static_problem_data_source import StaticProblemDataSource
from problem_sets.static.data.static_problem_entity import StaticProblemEntity


class StaticProblemRepository(StaticProblemDataSource):

    def __init__(self, sqlite_repo: StaticProblemSQLiteRepository):
        self.sqlite_repo = sqlite_repo

    def create(self, data: StaticProblemEntity):

        problem_row: StaticProblemRow = self.sqlite_repo.create(data)

        def save_convert_static_content(contents: List[StaticContentEntity], rows: List[StaticContentRow]):
            for content, row in zip(contents, rows):
                if content.type == StaticContentEntityType.image:
                    data_util.write_bytes_file(os.path.join(data_manager.IMAGES_DIR, f"{str(row.id)}.png"),
                                               content.value)

        save_convert_static_content(data.content, problem_row.content)

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

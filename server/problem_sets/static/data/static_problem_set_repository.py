import os
from typing import List

from problem_sets.static.data import data_util, data_manager
from problem_sets.static.data.sqlite.static_content_sqlite_repository import StaticContentRow
from problem_sets.static.data.sqlite.static_problem_set_sqlite_repository import StaticProblemSetSQLiteRepository
from problem_sets.static.data.static_content_entity import StaticContentEntity, StaticContentEntityType
from problem_sets.static.data.static_problem_set_data_source import StaticProblemSetDataSource
from problem_sets.static.data.static_problem_set_entity import StaticProblemSetEntity


class StaticProblemSetRepository(StaticProblemSetDataSource):

    def __init__(self, sqlite_repo: StaticProblemSetSQLiteRepository):
        self.sqlite_repo = sqlite_repo

    def create(self, data: StaticProblemSetEntity):

        set_row = self.sqlite_repo.create(data)

        def save_convert_static_content(contents: List[StaticContentEntity], rows: List[StaticContentRow]):
            for content, row in zip(contents, rows):
                if content.type == StaticContentEntityType.image:
                    data_util.write_bytes_file(os.path.join(data_manager.IMAGES_DIR, f"{str(row.id)}.png"),
                                               content.value)

        # TODO determine if we need to convert to entities first
        # instruction_content_rows: List[StaticContentEntity] = list(
        #     (StaticContentSQLiteRepository.map_row_to_entity(item)) for item in set_row.instruction_contents)
        # answer_content_rows: List[StaticContentEntity] = list(
        #     (StaticContentSQLiteRepository.map_row_to_entity(item)) for item in set_row.answer_contents)

        instruction_content_rows = set_row.instruction_contents
        answer_content_rows = set_row.answer_contents

        save_convert_static_content(data.instruction_contents, instruction_content_rows)
        save_convert_static_content(data.answer_contents, answer_content_rows)

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

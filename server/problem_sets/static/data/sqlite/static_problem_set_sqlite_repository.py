#  Copyright (c) 2019 Thomas Howe

from dataclasses import dataclass
from typing import Optional

from sqlalchemy import Column, String
from sqlalchemy.orm import Session, relationship

from problem_sets.static.data.sqlite.static_content_sqlite_repository import \
    static_content_instruction_problem_set_association, \
    StaticContentSQLiteRepository, static_content_answer_problem_set_association

PROBLEM_SETS_TABLE_ID = "problem_set"

from problem_sets.static.data.sqlite.sqlite_repository import SQLiteRepository
from problem_sets.static.data.sqlite.sqlite_manager import Base
from problem_sets.static.data.static_problem_set_data_source import StaticProblemSetDataSource
from problem_sets.static.data.static_problem_set_entity import StaticProblemSetEntity


@dataclass
class StaticProblemSetRow(Base):
    __tablename__ = PROBLEM_SETS_TABLE_ID
    id: str = Column(String, primary_key=True)
    source: str = Column(String)
    problems = relationship("StaticProblemRow", backref=PROBLEM_SETS_TABLE_ID)
    instruction_contents = relationship("StaticContentRow",
                                        secondary=static_content_instruction_problem_set_association)
    answer_contents = relationship("StaticContentRow", secondary=static_content_answer_problem_set_association)

    def __init__(self, id: str, source: str):
        self.id = id
        self.source = source


class StaticProblemSetSQLiteRepository(SQLiteRepository, StaticProblemSetDataSource):

    def __init__(self, session: Session):
        super().__init__(session, StaticProblemSetRow)

    def create(self, data: StaticProblemSetEntity):
        row = self.map_entity_to_row(data)

        if data.instruction_contents:
            row.instruction_contents.extend(list(
                map(StaticContentSQLiteRepository.map_entity_to_row, data.instruction_contents)))

        if data.answer_contents:
            row.answer_contents.extend(list(
                map(StaticContentSQLiteRepository.map_entity_to_row, data.answer_contents)))

        self.db_insert(row)

    def get(self, id: str) -> Optional[StaticProblemSetEntity]:
        row: StaticProblemSetRow = self.db_find_by_id(id)

        if row is None:
            return None

        return self.map_row_to_entity(row)

    def delete(self, id: str):
        pass

    def update(self, id: str, data: StaticProblemSetEntity):
        pass

    def list(self):
        self.db_list()

    def check_id_available(self, id: str) -> bool:
        result = self.get(id)
        return result is None

    @staticmethod
    def map_row_to_entity(row: StaticProblemSetRow):
        instruction_entities = list(map(StaticContentSQLiteRepository.map_row_to_entity, row.instruction_contents))
        answer_entities = list(map(StaticContentSQLiteRepository.map_row_to_entity, row.answer_contents))

        return StaticProblemSetEntity(row.id, row.source, instruction_entities, answer_entities)

    @staticmethod
    def map_entity_to_row(entity: StaticProblemSetEntity) -> StaticProblemSetRow:
        return StaticProblemSetRow(str(entity.id), entity.source)

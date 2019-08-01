#  Copyright (c) 2019 Thomas Howe

from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, func
from sqlalchemy.orm import Session, relationship
from typing import Optional

from problem_sets.static.data.sqlite.static_content_sqlite_repository import static_content_problem_association, \
    StaticContentSQLiteRepository

PROBLEMS_TABLE_ID = "problem"

from problem_sets.static.data.sqlite.sqlite_manager import Base
from problem_sets.static.data.sqlite.sqlite_repository import SQLiteRepository
from problem_sets.static.data.sqlite.static_problem_set_sqlite_repository import PROBLEM_SETS_TABLE_ID
from problem_sets.static.data.static_problem_data_source import StaticProblemDataSource
from problem_sets.static.data.static_problem_entity import StaticProblemEntity


@dataclass
class StaticProblemRow(Base):
    __tablename__ = PROBLEMS_TABLE_ID
    id = Column(Integer, primary_key=True)
    set_id = Column(String, ForeignKey(f"{PROBLEM_SETS_TABLE_ID}.id"))
    used = Column(Boolean)
    content = relationship("StaticContentRow", secondary=static_content_problem_association)

    def __init__(self, id: int, set_id: str, used: bool):
        self.id = id
        self.set_id = set_id
        self.used = used


class StaticProblemSQLiteRepository(SQLiteRepository, StaticProblemDataSource):

    def __init__(self, session: Session):
        super().__init__(session, StaticProblemRow)

    def create(self, data: StaticProblemEntity) -> StaticProblemRow:
        row = self.map_entity_to_row(data)

        if data.content:
            row.content.extend(list(
                map(StaticContentSQLiteRepository.map_entity_to_row, data.content)))

        self.db_insert(row)

        return row

    def get(self, id: int) -> Optional[StaticProblemEntity]:
        row: StaticProblemRow = self.db_find_by_id(id)

        if row is None:
            return None

        return self.map_row_to_entity(row)

    def delete(self, id: int):
        pass

    def update(self, id: int, data: StaticProblemEntity):
        pass

    def pick_problem_from_set(self, set_id: str) -> Optional[StaticProblemEntity]:
        row = self.session.query(StaticProblemRow).filter(StaticProblemRow.set_id == set_id).order_by(
            func.random()).first()

        if row is None:
            return None

        return self.map_row_to_entity(row)

    def list_problems_from_set(self, set_id: str) -> Optional[StaticProblemEntity]:
        rows = self.session.query(StaticProblemRow).filter(StaticProblemRow.set_id == set_id)
        return self.db_map_list(rows)

    @staticmethod
    def map_row_to_entity(row: StaticProblemRow) -> StaticProblemEntity:
        content_rows = row.content

        content_entities = list(map(StaticContentSQLiteRepository.map_row_to_entity, content_rows))

        return StaticProblemEntity(row.set_id, row.used, content_entities, row.id)

    @staticmethod
    def map_entity_to_row(entity: StaticProblemEntity) -> StaticProblemRow:
        return StaticProblemRow(entity.id, entity.set_id, entity.used)

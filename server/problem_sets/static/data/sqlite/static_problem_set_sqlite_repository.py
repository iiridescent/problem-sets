#  Copyright (c) 2019 Thomas Howe

from dataclasses import dataclass

from sqlalchemy import Column, String
from sqlalchemy.orm import Session, relationship

PROBLEM_SETS_TABLE_ID = "problem_set"

from problem_sets.static.data.sqlite import sqlite_util
from problem_sets.static.data.sqlite.sqlite_repository import SQLiteRepository
from problem_sets.static.data.sqlite.sqlite_manager import Base
from problem_sets.static.data.static_problem_set_data_source import StaticProblemSetDataSource
from problem_sets.static.static_problem_set_entity import StaticProblemSetEntity


@dataclass
class StaticProblemSetRow(Base):
    __tablename__ = PROBLEM_SETS_TABLE_ID
    id: str = Column(String, primary_key=True)
    source: str = Column(String)
    problems = relationship("StaticProblemRow", backref=PROBLEM_SETS_TABLE_ID)

    def __init__(self, id: str, source: str):
        self.id = id
        self.source = source


class StaticProblemSetSQLiteRepository(SQLiteRepository, StaticProblemSetDataSource):

    def __init__(self, session: Session):
        super().__init__(session, StaticProblemSetRow)

    def create(self, data: StaticProblemSetEntity):
        row = self.map_entity_to_row(data)
        self.insert(row)

    def get(self, id: str) -> StaticProblemSetEntity:
        row: StaticProblemSetRow = self.find_by_id(id)

        return StaticProblemSetEntity(**row)

    def delete(self, id: str):
        pass

    def update(self, id: str, data: StaticProblemSetEntity):
        pass

    def list(self):
        get_problem_sets_command = """SELECT id FROM ? ORDER BY ROWID DESC
        """
        result = sqlite_util.query_fetch(self.session, get_problem_sets_command, (PROBLEM_SETS_TABLE_ID,))

    def check_id_available(self, id: str) -> bool:
        check_id_command = """SELECT id FROM problem_sets WHERE id=?
        """
        result = sqlite_util.query_fetch(self.session, check_id_command, (id,))
        return len(result) == 0

    def setup(self):
        # # create_table_command = """CREATE TABLE IF NOT EXISTS problem_sets (
        # #                                 id TEXT PRIMARY KEY,
        # #                                 source TEXT
        # #                             );"""
        # problem_sets_table = Table(
        #     ''
        # )
        # sqlite_util.write_commit(self.session, create_table_command)
        pass

    @staticmethod
    def map_row_to_entity(row: Base):
        return StaticProblemSetEntity(entity.id, entity.source)

    @staticmethod
    def map_entity_to_row(entity: StaticProblemSetEntity) -> StaticProblemSetRow:
        return StaticProblemSetRow(entity.id, entity.source)

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import Session

from problem_sets.static.data.sqlite.sqlite_manager import Base
from problem_sets.static.data.sqlite.sqlite_repository import SQLiteRepository
from problem_sets.static.data.static_content_entity import StaticContentEntity, StaticContentType

static_content_instruction_problem_set_association = Table('static_content_instruction_problem_set_association',
                                                           Base.metadata,
                                                           Column('content_id', Integer, ForeignKey('content.id')),
                                                           Column('problem_set_id', Integer,
                                                                   ForeignKey('problem_set.id')),
                                                           )

static_content_answer_problem_set_association = Table('static_content_answer_page_problem_set_association',
                                                      Base.metadata,
                                                      Column('content_id', Integer, ForeignKey('content.id')),
                                                      Column('problem_set_id', Integer,
                                                                   ForeignKey('problem_set.id')),
                                                      )

static_content_problem_association = Table('static_content_problem_association', Base.metadata,
                                           Column('content_id', Integer, ForeignKey('content.id')),
                                           Column('problem_id', Integer, ForeignKey('problem.id')),
                                           )


class StaticContentRow(Base):
    __tablename__ = "content"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    value = Column(String)

    def __init__(self, type: str, value: str, id: int = None):
        self.type = type
        self.value = value
        self.id = id


class StaticContentSQLiteRepository(SQLiteRepository):

    @staticmethod
    def map_row_to_entity(row: StaticContentRow) -> StaticContentEntity:
        return StaticContentEntity(row.id, StaticContentType(row.type), row.value)

    @staticmethod
    def map_entity_to_row(entity: StaticContentEntity) -> StaticContentRow:
        return StaticContentRow(entity.type.value, entity.value, entity.id)

    def __init__(self, session: Session):
        super().__init__(session, StaticContentRow)

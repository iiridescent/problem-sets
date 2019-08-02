from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import scoped_session

from problem_sets.static.data.sqlite.sqlite_manager import Base
from problem_sets.static.data.sqlite.sqlite_repository import SQLiteRepository
from problem_sets.static.data.static_content_entity import StaticContentEntity, StaticContentEntityType

static_content_instruction_problem_set_association = Table('static_content_instruction_problem_set_association',
                                                           Base.metadata,
                                                           Column('content_id', Integer,
                                                                  ForeignKey('content.id', ondelete='CASCADE')),
                                                           Column('problem_set_id', Integer,
                                                                  ForeignKey('problem_set.id', ondelete='CASCADE')),
                                                           )

static_content_answer_problem_set_association = Table('static_content_answer_page_problem_set_association',
                                                      Base.metadata,
                                                      Column('content_id', Integer,
                                                             ForeignKey('content.id', ondelete='CASCADE')),
                                                      Column('problem_set_id', Integer,
                                                             ForeignKey('problem_set.id', ondelete='CASCADE')),
                                                      )

static_content_problem_association = Table('static_content_problem_association', Base.metadata,
                                           Column('content_id', Integer, ForeignKey('content.id', ondelete='CASCADE')),
                                           Column('problem_id', Integer, ForeignKey('problem.id', ondelete='CASCADE')),
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
    row_class = StaticContentRow

    @staticmethod
    def map_row_to_entity(row: StaticContentRow) -> StaticContentEntity:
        return StaticContentEntity(StaticContentEntityType(row.type), row.value, row.id)

    @staticmethod
    def map_entity_to_row(entity: StaticContentEntity) -> StaticContentRow:
        value = entity.value
        if isinstance(value, bytes):
            value = None
        return StaticContentRow(entity.type.value, value, entity.id)

    def __init__(self, session: scoped_session):
        super().__init__(session)

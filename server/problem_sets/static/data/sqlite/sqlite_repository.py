#  Copyright (c) 2019 Thomas Howe

from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


class SQLiteRepository(ABC):

    def __init__(self, session: Session, table: str):
        self.session = session
        self.table = table,
        self.setup()

    @abstractmethod
    def setup(self):
        pass

    def select_by_id(self, id: any):
        select_by_id_command = f"""SELECT * FROM {self.table} WHERE id=?
        """
        result = self.session.query()

        if len(result) == 0:
            return None

        return result[0]

#  Copyright (c) 2019 Thomas Howe

from typing import List, Union

from problem_sets.static.data import data_manager
from problem_sets.static.data.sqlite.test import sqlite_test_util


def clean_start(tables: Union[str, List[str]]):
    sqlite_test_util.clean_start(tables)
    data_manager.initialize()
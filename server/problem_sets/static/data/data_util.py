#  Copyright (c) 2019 Thomas Howe

import os

from problem_sets.dir_util import ROOT_DIR

DATA_DIR = os.path.join(ROOT_DIR, "static_data")


def create_image(data, dir: str):
    # TODO: Set type of data
    raise NotImplementedError("'create_image' is not implemented")


def delete_image(dir: str):
    raise NotImplementedError("'delete_image' is not implemented")
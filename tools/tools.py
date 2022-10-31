import importlib
from typing import Tuple


def load_class(class_tuple: Tuple[str, str]):
    requested_class = getattr(importlib.import_module(class_tuple[0]), class_tuple[1])
    return requested_class

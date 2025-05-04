import os

import pytest

from config import ROOT_DIR
from src.classses.cls_json_processing import JSONSaver
from src.classses.cls_vacancy import Vacancy


def test_cls_json(raw_data_test: dict) -> None:
    """Тестирование функциональности JSONSaver"""
    if os.path.exists(f"{ROOT_DIR}/data/test_data.json"):
        os.remove(f"{ROOT_DIR}/data/test_data.json")
    test_json_s = JSONSaver("test_data.json")
    test_cls_data = Vacancy.cast_to_object_list(raw_data_test["items"])
    test_json_s.add_vacancy(test_cls_data)
    test_json_s.delete_vacancy(test_cls_data[0])


def test_delete_list(raw_data_test: dict) -> None:
    """Тестирование метода delete_vacancy"""
    with pytest.raises(ValueError):
        JSONSaver("")
    test_json_s = JSONSaver("test_data.json")
    test_cls_data = Vacancy.cast_to_object_list(raw_data_test["items"])
    test_json_s.add_vacancy(test_cls_data)
    test_json_s.add_vacancy(test_cls_data)
    test_json_s.delete_vacancy([test_cls_data[0]])

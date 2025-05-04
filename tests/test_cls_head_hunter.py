from unittest.mock import patch

from src.classses.cls_head_hunter import HH


def test_class_h_h(raw_data_test: dict) -> None:
    """Тестирование функционала класса HH"""
    hh_api = HH()
    with patch("requests.Session.get") as mock:
        mock.return_value.status_code = 200
        mock.return_value.json.return_value = raw_data_test
        test_hh_api = hh_api.get_vacancies("python")
        assert test_hh_api[0]["name"] == "Junior Python Developer"
        assert test_hh_api[1]["name"] == "Web-программист - стажер"

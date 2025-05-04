from src.classses.cls_vacancy import Vacancy


def test_valid_init(vacancy_data_test: Vacancy) -> None:
    """Тест инициализации"""
    test_vacancy = vacancy_data_test
    assert test_vacancy.name == "Тестировщик / IT специалист"
    assert test_vacancy.address == "https://hh.ru/applicant/vacancy_response?vacancyId=120063617"
    assert test_vacancy.experience == "Нет опыта"
    assert test_vacancy.salary_from == 100000
    assert test_vacancy.salary_to == 160000
    assert test_vacancy.description == "Нет результатов"


def test_cls_vacancy(raw_data_test: dict, vacancy_data_test: Vacancy) -> None:
    """Тестирование функционала класса Vacancy"""
    # Vacancy(0, 0, "", "", 0, 0)
    test_cls_data = Vacancy.cast_to_object_list(raw_data_test["items"])
    assert test_cls_data[0].name == raw_data_test["items"][0]["name"]
    assert test_cls_data[0] == test_cls_data[0]
    assert test_cls_data[0] <= vacancy_data_test
    assert vacancy_data_test >= test_cls_data[0]
    assert test_cls_data[0] < vacancy_data_test
    assert vacancy_data_test > test_cls_data[0]
    assert vacancy_data_test.__repr__() == "Vacancy('100000-160000')"
    assert str(vacancy_data_test) == (
        "Vacancy('Тестировщик / IT специалист "
        "https://hh.ru/applicant/vacancy_response?vacancyId=120063617 Нет опыта "
        "100000-160000 Нет результатов')"
    )
    assert vacancy_data_test.to_dict() == {
        "address": "https://hh.ru/applicant/vacancy_response?vacancyId=120063617",
        "description": "Нет результатов",
        "experience": "Нет опыта",
        "name": "Тестировщик / IT специалист",
        "salary_from": 100000,
        "salary_to": 160000,
    }

from _pytest.capture import CaptureFixture

from src.classses.cls_vacancy import Vacancy
from src.func_for_user import (
    filter_vacancies,
    get_top_vacancies,
    get_vacancies_by_salary,
    print_vacancies,
    sort_vacancies,
)


def test_additional_functions(raw_data_test: dict, capsys: CaptureFixture) -> None:
    """Тестирование функций для взаимодействия с пользователями"""
    test_cls_data = Vacancy.cast_to_object_list(raw_data_test["items"])
    filter_words = "py python".split()
    salary_range = "0 - 10000"
    top_n = 1
    filtered_vacancies = filter_vacancies(test_cls_data, filter_words)
    assert str(filtered_vacancies) == "[Vacancy('0-0')]"
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    assert str(ranged_vacancies) == "[Vacancy('0-0')]"
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    assert str(sorted_vacancies) == "[Vacancy('0-0')]"
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    assert str(top_vacancies) == "[Vacancy('0-0')]"
    print_vacancies(top_vacancies)
    read_out = capsys.readouterr()
    assert read_out.out == (
        "Vacancy('Junior Python Developer "
        "https://hh.ru/applicant/vacancy_response?vacancyId=120111330 Нет опыта 0-0 "
        "Build and maintain back-end for Improvado's marketing analytics SaaS "
        "platform (including architectural improvements regarding scalability, "
        "reliability and performance), python. ')\n"
    )

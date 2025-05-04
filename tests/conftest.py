import pytest

from src.classses.cls_vacancy import Vacancy


@pytest.fixture
def data_json_test() -> list[dict]:
    """Фикстура с тестовыми данными"""
    return [
        {
            "name": "Тестировщик / IT специалист",
            "address": "https://hh.ru/applicant/vacancy_response?vacancyId=120063617",
            "experience": "Нет опыта",
            "salary_from": 100000,
            "salary_to": 160000,
            "description": "python",
        },
        {
            "name": "Директор департамента Информационных Технологий",
            "address": "https://hh.ru/applicant/vacancy_response?vacancyId=119892956",
            "experience": "Более 6 лет",
            "salary_from": 500000,
            "salary_to": 0,
            "description": "java",
        },
    ]


@pytest.fixture()
def vacancy_data_test() -> Vacancy:
    """Фикстура с тестовыми данными для класса Vacancy"""
    return Vacancy(
        name="Тестировщик / IT специалист",
        address="https://hh.ru/applicant/vacancy_response?vacancyId=120063617",
        experience="Нет опыта",
        salary_from=100000,
        salary_to=160000,
        description="",
    )


@pytest.fixture()
def raw_data_test() -> dict:
    """Фикстура с сырыми данными"""
    raw_data = {
        "items": [
            {
                "id": "120111330",
                "premium": False,
                "name": "Junior Python Developer",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "160", "name": "Алматы", "url": "https://api.hh.ru/areas/160"},
                "salary": None,
                "salary_range": None,
                "type": {"id": "open", "name": "Открытая"},
                "address": None,
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2025-04-30T12:46:36+0300",
                "created_at": "2025-04-30T12:46:36+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=120111330",
                "show_logo_in_search": None,
                "show_contacts": False,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/120111330?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/120111330",
                "relations": [],
                "employer": {
                    "id": "9574451",
                    "name": "Improvado KZ",
                    "url": "https://api.hh.ru/employers/9574451",
                    "alternate_url": "https://hh.ru/employer/9574451",
                    "logo_urls": {
                        "original": "https://img.hhcdn.ru/employer-logo-original/1058233.png",
                        "90": "https://img.hhcdn.ru/employer-logo/5853573.png",
                        "240": "https://img.hhcdn.ru/employer-logo/5853574.png",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=9574451",
                    "accredited_it_employer": False,
                    "employer_rating": None,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Basic knowledge of <highlighttext>Python</highlighttext> "
                    "or 1 year in a role focused on <highlighttext>Python</highlighttext> "
                    "backend development (perfectly with Django framework). ",
                    "responsibility": "Build and maintain back-end for Improvado's marketing analytics "
                    "SaaS platform (including architectural improvements regarding scalability, "
                    "reliability and performance), python. ",
                },
                "contacts": None,
                "schedule": {"id": "remote", "name": "Удаленная работа"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": False,
                "fly_in_fly_out_duration": [],
                "work_format": [{"id": "REMOTE", "name": "Удалённо"}],
                "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
                "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
                "night_shifts": False,
                "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
                "accept_incomplete_resumes": False,
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "employment_form": {"id": "FULL", "name": "Полная"},
                "internship": False,
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
            {
                "id": "118711736",
                "premium": False,
                "name": "Web-программист - стажер",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "160", "name": "Алматы", "url": "https://api.hh.ru/areas/160"},
                "salary": None,
                "salary_range": {"from": 1, "to": 1000},
                "type": {"id": "open", "name": "Открытая"},
                "address": {
                    "city": "Алматы",
                    "street": "бульвар Бухар Жырау",
                    "building": "26/1",
                    "lat": 43.232296,
                    "lng": 76.923259,
                    "description": None,
                    "raw": "Алматы, бульвар Бухар Жырау, 26/1",
                    "metro": None,
                    "metro_stations": [],
                    "id": "16504789",
                },
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2025-04-23T12:52:10+0300",
                "created_at": "2025-04-23T12:52:10+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=118711736",
                "show_logo_in_search": None,
                "show_contacts": False,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/118711736?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/118711736",
                "relations": [],
                "employer": {
                    "id": "5031522",
                    "name": "Autodata",
                    "url": "https://api.hh.ru/employers/5031522",
                    "alternate_url": "https://hh.ru/employer/5031522",
                    "logo_urls": {
                        "original": "https://img.hhcdn.ru/employer-logo-original/1413898.png",
                        "90": "https://img.hhcdn.ru/employer-logo/7275252.png",
                        "240": "https://img.hhcdn.ru/employer-logo/7275253.png",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=5031522",
                    "accredited_it_employer": False,
                    "employer_rating": None,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Carfast- Первый онлайн авто аукцион в Казахстане. "
                    "Доброжелательный и целеустремленный командный игрок. "
                    "Принимаете верные решения в критических ситуациях. ",
                    "responsibility": "Лучшая система аналитики товаров на Kaspi. "
                    "Fastbot - Телеграм бот для поиска авто. "
                    "Ну и есть конечно же такие проекты, как...",
                },
                "contacts": None,
                "schedule": {"id": "fullDay", "name": "Полный день"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": False,
                "fly_in_fly_out_duration": [],
                "work_format": [],
                "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
                "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
                "night_shifts": False,
                "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
                "accept_incomplete_resumes": True,
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "employment_form": {"id": "FULL", "name": "Полная"},
                "internship": True,
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
        ]
    }
    return raw_data

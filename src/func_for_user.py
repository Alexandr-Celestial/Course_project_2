from src.classses.cls_vacancy import Vacancy


def filter_vacancies(vacancies_list: list[Vacancy], filter_words: list[str]) -> list[Vacancy]:
    """Фильтрует список вакансий по ключевым словам в описании"""
    filtered_vac_list = []
    for vac in vacancies_list:
        for word in filter_words:
            if word in vac.description:
                filtered_vac_list.append(vac)
                break
    return filtered_vac_list


def get_vacancies_by_salary(filtered_vacancies: list[Vacancy], salary_range: str) -> list[Vacancy]:
    """Фильтрует вакансии по диапазону зарплаты"""
    sal_from, sal_to = salary_range.split("-")
    filtered_vac_list = [
        vac for vac in filtered_vacancies if int(sal_from) <= vac.salary_from and int(sal_to) >= vac.salary_to
    ]
    return filtered_vac_list


def sort_vacancies(ranged_vacancies: list[Vacancy]) -> list[Vacancy]:
    """Сортирует вакансии по максимальной зарплате salary_to"""
    return sorted(ranged_vacancies, key=lambda x: x.salary_to)


def get_top_vacancies(sorted_vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """Получает топ-n вакансий из отсортированного списка"""
    return sorted_vacancies[:top_n]


def print_vacancies(top_vacancies: list[Vacancy]) -> None:
    """Выводит информацию о вакансиях в консоль"""
    for t_v in top_vacancies:
        print(t_v)

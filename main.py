# Создание экземпляра класса для работы с API сайтов с вакансиями
from src.classses.cls_head_hunter import HH
from src.classses.cls_vacancy import Vacancy
from src.func_for_user import (
    filter_vacancies,
    get_top_vacancies,
    get_vacancies_by_salary,
    print_vacancies,
    sort_vacancies,
)


# Функция для взаимодействия с пользователем
def user_interaction() -> None:
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
    h_h = HH()
    vacancies_list: list[dict] = h_h.get_vacancies(search_query)
    print(vacancies_list)
    vacancies_list_ = Vacancy.cast_to_object_list(vacancies_list)
    filtered_vacancies = filter_vacancies(vacancies_list_, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()

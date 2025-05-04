from typing import Any, Self


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("name", "address", "salary_from", "salary_to", "experience", "description")

    def __init__(
        self, name: str, address: str, salary_from: int, salary_to: int, experience: str, description: str
    ) -> None:
        """Инициализация экземпляра Vacancy"""
        self.name = Vacancy.__validate_name(name)
        self.address = Vacancy.__validate_address(address)
        self.salary_from = Vacancy.__validate_salary_from(salary_from)
        self.salary_to = Vacancy.__validate_salary_to(salary_to)
        self.experience = Vacancy.__validate_experience(experience)
        self.description = Vacancy.__validate_description(description)

    @classmethod
    def cast_to_object_list(cls, dirty_list_vacations: list[dict]) -> list[Self]:
        """Преобразует список словарей с данными вакансий в список объектов Vacancy"""
        clear_list_vacations = []
        for item in dirty_list_vacations:
            salary_from = 0
            salary_to = 0
            if sel_ran := item["salary_range"]:
                salary_from = sel_ran["from"] if sel_ran["from"] else 0
                salary_to = sel_ran["to"] if sel_ran["to"] else 0
            clear_list_vacations.append(
                cls(
                    item["name"],
                    item["apply_alternate_url"],
                    salary_from,
                    salary_to,
                    item["experience"]["name"],
                    item["snippet"]["responsibility"],
                )
            )
        return clear_list_vacations

    def __eq__(self, other: Any) -> Any:
        """Переопределённый метод __eq__"""
        return self.salary_to == other.salary_to

    def __lt__(self, other: Any) -> Any:
        """Переопределённый метод __lt__"""
        return self.salary_to < other.salary_to

    def __gt__(self, other: Any) -> Any:
        """Переопределённый метод __gt__"""
        return self.salary_to > other.salary_to

    def __le__(self, other: Any) -> Any:
        """Переопределённый метод __le__"""
        return self.salary_to <= other.salary_to

    def __ge__(self, other: Any) -> Any:
        """Переопределённый метод __ge__"""
        return self.salary_to >= other.salary_to

    def __repr__(self) -> str:
        """Переопределённый метод __repr__"""
        return f"{self.__class__.__name__}('{self.salary_from}-{self.salary_to}')"

    @staticmethod
    def __validate_name(name: str) -> Any:
        """Проводит валидацию названия вакансии"""
        if isinstance(name, str) and len(name) > 0:
            return name
        return NotImplemented

    @staticmethod
    def __validate_address(address: str) -> Any:
        """Проводит валидацию адреса вакансии"""
        if isinstance(address, str) and len(address) > 0:
            return address
        return NotImplemented

    @staticmethod
    def __validate_experience(experience: str) -> Any:
        """Проводит валидацию опыта вакансии"""
        if isinstance(experience, str) and len(experience) > 0:
            return experience
        return NotImplemented

    @staticmethod
    def __validate_salary_from(salary_from: int) -> Any:
        """Проводит валидацию зарплаты от"""
        if isinstance(salary_from, int) and salary_from >= 0:
            return salary_from
        return 0

    @staticmethod
    def __validate_salary_to(salary_to: int) -> Any:
        """Проводит валидацию зарплаты до"""
        if isinstance(salary_to, int) and salary_to >= 0:
            return salary_to
        return 0

    @staticmethod
    def __validate_description(description: str) -> Any:
        """Проводит валидацию описания вакансии"""
        if isinstance(description, str) and len(description) > 0:
            return description
        return "Нет результатов"

    def to_dict(self) -> dict:
        """Преобразует вакансию в словарь"""
        return {
            "name": self.name,
            "address": self.address,
            "experience": self.experience,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "description": self.description,
        }

    def __str__(self) -> str:
        """Переопределение метода __str__"""
        return (
            f"{self.__class__.__name__}('{self.name} {self.address} "
            f"{self.experience} {self.salary_from}-{self.salary_to} {self.description}')"
        )

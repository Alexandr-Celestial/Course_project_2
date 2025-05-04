import json
import os
from abc import ABC, abstractmethod

from config import ROOT_DIR
from src.classses.cls_vacancy import Vacancy


class ADDBase(ABC):
    """Абстрактный класс методов обработки файла вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancies: list[Vacancy]) -> None: ...
    """Абстрактный метод добавляет вакансии в хранилище"""

    @abstractmethod
    def _write_file_vacancy(self) -> None: ...
    """Абстрактный метод сохраняет текущие вакансии в файл"""

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy | list[Vacancy]) -> None: ...
    """Абстрактный метод удаляет одну или несколько вакансий из хранилища"""

    @abstractmethod
    def _read_file(self) -> None: ...
    """Абстрактный метод считывает вакансии из файла в память"""

    @abstractmethod
    def _validate_file_name(self, file_name: str) -> str: ...
    """Абстрактный метод проверяет корректность имени файла и возвращает путь к нему"""


class JSONSaver(ADDBase):
    """Класс для обработки информации о вакансиях в JSON-файл"""

    def __init__(self, file_name: str = "data.json") -> None:
        """Инициализация экземпляра JSONSaver"""
        self.vacancies_list: list[dict] = []
        self.__file_name = self._validate_file_name(file_name)
        self._read_file()

    def add_vacancy(self, vacancies: list[Vacancy]) -> None:
        """Добавляет новые вакансии в список и сохраняет их в файл без дублей"""
        vacancies_list = [vacancy_.get("address") for vacancy_ in self.vacancies_list]
        list_vacancy = [vacancy.to_dict() for vacancy in vacancies if vacancy.address not in vacancies_list]
        if not list_vacancy:
            return None
        self.vacancies_list.extend(list_vacancy)
        self._write_file_vacancy()

    def _write_file_vacancy(self) -> None:
        """Сохраняет список вакансий в файл"""
        with open(self.__file_name, "w", encoding="utf-8") as file:
            file.write(json.dumps(self.vacancies_list, ensure_ascii=False, indent=4))

    def delete_vacancy(self, vacancy: Vacancy | list[Vacancy]) -> None:
        """Удаляет одну или список вакансий и обновляет файл"""
        if isinstance(vacancy, list):
            for i, vac in enumerate(self.vacancies_list):
                for v in vacancy:
                    if vac["address"] == v.address:
                        del self.vacancies_list[i]
        else:
            for i, vac in enumerate(self.vacancies_list):
                if vac["address"] == vacancy.address:
                    del self.vacancies_list[i]
        self._write_file_vacancy()

    def _validate_file_name(self, file_name: str) -> str:
        """Проверяет корректность файла, если он существует - вакансии записываются в него"""
        if isinstance(file_name, str) and len(file_name) > 0:
            data_file = f"{ROOT_DIR}/data/{file_name}"
            return data_file
        raise ValueError("Имя файла не указано")

    def _read_file(self) -> None:
        """Метод читает данные из файла"""
        data_file = self.__file_name
        if os.path.exists(data_file):
            with open(data_file, encoding="utf-8", mode="r") as file:
                self.vacancies_list = json.load(file)
        else:
            with open(data_file, encoding="utf-8", mode="a"):
                pass

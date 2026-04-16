# utils/checks.py
import allure
from requests import Response
from models.main import *
from utils.logger import logger

class Checking:
    @staticmethod
    @allure.step("Проверка статус-кода: ожидается {status_code}")
    def check_status_code(response: Response, status_code):
        logger.info(f"Проверка статуса: ожидается {status_code}")
        assert status_code == response.status_code, f'Провал! Статус код {response.status_code} не соответствует ожидаемому: {status_code}'
        logger.info(f"Статус {response.status_code} OK")
        print(f'Успешно! Статус код: {response.status_code} соответствует ожидаемому {status_code}')

    @staticmethod
    @allure.step("Проверка данных частичного обновления")
    def check_partial_update_data(response: Response, original_payload: dict, partial_payload: dict):
        logger.info("Проверка частичного обновления (PATCH)")
        updated = Booking_validation.model_validate(response.json())
        original = Booking_validation.model_validate(original_payload)
        expected = original.model_copy()
        for field, value in partial_payload.items():
            setattr(expected, field, value)
        assert updated == expected, f"Обновлённые данные не совпадают.\nОжидалось: {expected}\nПолучено: {updated}"
        logger.info("Частичное обновление успешно")
        print(f"Частичное обновление данных методом PATCH прошло успешно")

    @staticmethod
    @allure.step("Проверка данных при создании бронирования")
    def check_create_data(response: Response, excepted_data):
        logger.info("Проверка создания бронирования")
        res_data = Validate_create_booking.model_validate(response.json())
        excepted_data = Booking_validation.model_validate(excepted_data)
        assert res_data.booking == excepted_data, print(f"Введенных данных для создания/изменения объекта нет в фактическом результате\n. Фактический результат: {res_data.booking}\n Ожидаемый результат: {excepted_data}")
        logger.info("Создание проверено успешно")
        print(f"Фактический результат: {res_data.booking}\nСовпадает с Ожидаемым: {excepted_data}")

    @staticmethod
    @allure.step("Проверка данных при полном обновлении (PUT)")
    def check_update_full_data(response: Response, excepted_data):
        logger.info("Проверка полного обновления (PUT)")
        res_data = Booking_validation.model_validate(response.json())
        excepted_data = Booking_validation.model_validate(excepted_data)
        assert res_data == excepted_data, print(f"Введенных данных для создания/изменения объекта нет в фактическом результате\n. Фактический результат: {res_data}\n Ожидаемый результат: {excepted_data}")
        logger.info("Полное обновление успешно")
        print(f"Фактический результат: {res_data}\nСовпадает с Ожидаемым: {excepted_data}")
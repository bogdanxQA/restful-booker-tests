import allure
import pytest
from common.api.booking_api import BookingAPI
from requests import Response
from models.main import *
from utils.checks import Checking
from models.types import Booking_Info
from data.test_invalid_data import invalid_booking_cases


@allure.feature("Негативные тесты API бронирований")
class TestBookingNagative:

    INVALID_COOKIES = [
        {},
        {"token": ""},
        {"token": "invalid_token"},
        {"token": "12345"},
    ]

    """"Частичное изменение, полное изменение и удаление данных бронирования с невалидным авторизационным токеном"""
    @allure.story("Доступ без авторизации (неверный/пустой токен)")
    @pytest.mark.parametrize("invalid_cookies", INVALID_COOKIES)
    def test_partial_upd_wo_auth(self, booking_api: BookingAPI, partial_update_payload, create_booking: Booking_Info, invalid_cookies):
        with allure.step(f"Попытка PATCH с cookies = {invalid_cookies}"):
            res: Response = booking_api.partial_update_booking(partial_update_payload, create_booking.id, cookies=invalid_cookies)
        Checking.check_status_code(res, 403)

    @allure.story("Доступ без авторизации (неверный/пустой токен)")
    @pytest.mark.parametrize("invalid_cookies", INVALID_COOKIES)
    def test_delete_wo_auth(self, booking_api: BookingAPI, create_booking: Booking_Info, invalid_cookies):
        with allure.step(f"Попытка DELETE с cookies = {invalid_cookies}"):
            res: Response = booking_api.delete_booking(create_booking.id, cookies=invalid_cookies)
        Checking.check_status_code(res, 403)

    @allure.story("Доступ без авторизации (неверный/пустой токен)")
    @pytest.mark.parametrize("invalid_cookies", INVALID_COOKIES)
    def test_full_upd_wo_auth(self, changed_valid_payload, create_booking: Booking_Info, booking_api: BookingAPI, invalid_cookies):
        with allure.step(f"Попытка PUT с cookies = {invalid_cookies}"):
            res: Response = booking_api.full_update_booking(changed_valid_payload, create_booking.id, cookies=invalid_cookies)
        Checking.check_status_code(res, 403)

    """"Попытка удаления, поиска, частичного и полного изменения несуществующего бронирования"""
    @allure.story("Операции над несуществующим бронированием")
    def test_delete_non_existent_booking(self, auth_token, booking_api: BookingAPI, create_booking: Booking_Info):
        id = create_booking.id
        with allure.step(f"Удаляем бронь {id}"):
            booking_api.delete_booking(id, auth_token)
        with allure.step(f"Повторно удаляем ту же бронь (ожидаем 405)"):
            res: Response = booking_api.delete_booking(id, auth_token)
        Checking.check_status_code(res, 405)

    @allure.story("Операции над несуществующим бронированием")
    def test_full_upd_non_existent_booking(self, auth_token, booking_api: BookingAPI, create_booking: Booking_Info, changed_valid_payload):
        id = create_booking.id
        with allure.step(f"Удаляем бронь {id}"):
            booking_api.delete_booking(id, auth_token)
        with allure.step(f"Попытка PUT для удалённой брони {id}"):
            res: Response = booking_api.full_update_booking(changed_valid_payload, id, auth_token)
        Checking.check_status_code(res, 405)

    @allure.story("Операции над несуществующим бронированием")
    def test_partial_upd_non_existent_booking(self, auth_token, booking_api: BookingAPI, create_booking: Booking_Info, changed_valid_payload):
        id = create_booking.id
        with allure.step(f"Удаляем бронь {id}"):
            booking_api.delete_booking(id, auth_token)
        with allure.step(f"Попытка PATCH для удалённой брони {id}"):
            res: Response = booking_api.partial_update_booking(changed_valid_payload, id, auth_token)
        Checking.check_status_code(res, 405)

    @allure.story("Операции над несуществующим бронированием")
    def test_get_byid_non_existent_booking(self, booking_api: BookingAPI, create_booking: Booking_Info, auth_token):
        id = create_booking.id
        with allure.step(f"Удаляем бронь {id}"):
            booking_api.delete_booking(id, auth_token)
        with allure.step(f"Попытка GET для удалённой брони {id}"):
            res: Response = booking_api.get_booking_by_id(id)
        Checking.check_status_code(res, 404)

    """Создание с неверными данными в payload"""
    @allure.story("Создание бронирования с невалидными данными")
    @pytest.mark.parametrize("payload, expected_status, case_name", invalid_booking_cases)
    def test_create_booking_with_invalid_payload(self, booking_api: BookingAPI, payload, expected_status, case_name):
        allure.dynamic.title(case_name)
        with allure.step(f"Отправка POST с некорректным payload: {case_name}"):
            res: Response = booking_api.create_booking(payload)
        Checking.check_status_code(res, expected_status)
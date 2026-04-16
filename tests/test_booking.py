import allure
from common.api.booking_api import BookingAPI
from requests import Response
from models.main import *
from utils.checks import Checking
from models.types import Booking_Info

@allure.feature("Управление бронированиями")
class TestBookingCRUD():

    @allure.story("Получение списка всех бронирований")
    def test_get_full_list_booking(self, booking_api: BookingAPI):
        with allure.step("Выполнить GET запрос к /booking/"):
            res: Response = booking_api.get_full_list_booking()
        with allure.step("Проверить статус код 200"):
            Checking.check_status_code(res, 200)
        with allure.step("Валидировать JSON-схему списка"):
            validated = full_list_adapter.validate_python(res.json())
        with allure.step("Проверить, что список не пуст"):
            assert len(validated) > 0, 'Список бронирований пуст'
        print(f'Ответ соответствует json schema. В ответе вернулось {len(validated)} бронирований')

    @allure.story("Частичное обновление бронирования (PATCH)")
    def test_partial_update_booking(self, auth_token, booking_api: BookingAPI, partial_update_payload, create_booking: Booking_Info):
        with allure.step(f"Отправить PATCH запрос для брони ID {create_booking.id}"):
            res: Response = booking_api.partial_update_booking(
                booking_data=partial_update_payload,
                booking_id=create_booking.id,
                cookies=auth_token
            )
        with allure.step("Проверить статус код 200"):
            Checking.check_status_code(res, 200)
        with allure.step("Проверить корректность обновлённых данных"):
            Checking.check_partial_update_data(res, create_booking.payload, partial_update_payload)

    @allure.story("Создание бронирования")
    def test_create_booking(self, booking_api: BookingAPI, valid_booking_payload):
        with allure.step("Отправить POST запрос на создание бронирования"):
            res: Response = booking_api.create_booking(valid_booking_payload)
        with allure.step("Проверить статус код 200"):
            Checking.check_status_code(res, 200)
        with allure.step("Проверить, что данные созданы верно"):
            Checking.check_create_data(res, valid_booking_payload)

    @allure.story("Получение бронирования по ID")
    def test_get_booking_by_id(self, booking_api: BookingAPI, create_booking: Booking_Info):
        with allure.step(f"Выполнить GET запрос для брони ID {create_booking.id}"):
            res: Response = booking_api.get_booking_by_id(create_booking.id)
        with allure.step("Проверить статус код 200"):
            Checking.check_status_code(res, 200)
        with allure.step("Валидировать JSON-схему ответа"):
            Booking_validation.model_validate(res.json())

    @allure.story("Удаление бронирования")
    def test_delete_booking(self, auth_token, booking_api: BookingAPI, create_booking: Booking_Info):
        with allure.step(f"Отправить DELETE запрос для брони ID {create_booking.id}"):
            res: Response = booking_api.delete_booking(booking_id=create_booking.id, cookies=auth_token)
        with allure.step("Проверить статус код 201"):
            Checking.check_status_code(res, 201)
        with allure.step("Проверить текст ответа 'Created'"):
            assert res.text == "Created"
        print(f'Бронирование с id = {create_booking.id} удалено')
        with allure.step("Проверить, что бронирование действительно удалено (GET вернёт 404)"):
            res_get: Response = booking_api.get_booking_by_id(create_booking.id)
            Checking.check_status_code(res_get, 404)
        print(f'Бронирование с id = {create_booking.id} не найдено в списке бронирований - удаление прошло успешно!')

    @allure.story("Полное обновление бронирования (PUT)")
    def test_full_update_booking(self, auth_token, changed_valid_payload, booking_api: BookingAPI, create_booking: Booking_Info):
        with allure.step(f"Отправить PUT запрос для брони ID {create_booking.id}"):
            res: Response = booking_api.full_update_booking(changed_valid_payload, create_booking.id, auth_token)
        with allure.step("Проверить статус код 200"):
            Checking.check_status_code(res, 200)
        with allure.step("Валидировать JSON-схему ответа"):
            Booking_validation.model_validate(res.json())
        with allure.step("Проверить, что данные обновлены полностью"):
            Checking.check_update_full_data(res, changed_valid_payload)
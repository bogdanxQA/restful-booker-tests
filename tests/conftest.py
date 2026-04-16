import pytest
import json
from common.api.auth_api import Auth
from common.api.client import APIclient
from common.api.booking_api import BookingAPI
from pathlib import Path
from models.types import Booking_Info

"""Загрузка данных для payload"""
def load_payload(key: str):
    current_dir = Path(__file__).parent
    data_file = current_dir.parent / "data" / "booking_payloads.json"
    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data[key]

@pytest.fixture(scope='session')
def auth_token():
   token = Auth.get_auth_token()
   cookies = {"token":token}
   return cookies


@pytest.fixture(scope='session')
def api_client():
   base_url = "https://restful-booker.herokuapp.com"
   return(APIclient(base_url))
      

@pytest.fixture
def booking_api(api_client) -> BookingAPI:
   return BookingAPI(api_client)

@pytest.fixture
def valid_booking_payload():
    return load_payload("valid_booking")

@pytest.fixture
def invalid_booking_payload():
    return load_payload("invalid_booking")

@pytest.fixture
def partial_update_payload():
    return load_payload("partial_update")

@pytest.fixture
def changed_valid_payload():
    return load_payload("changed_valid_booking")



@pytest.fixture#создание бронирования перед удалением (получаем id) использую для атомарности тестов
def create_booking(booking_api: BookingAPI, valid_booking_payload) -> Booking_Info:
    res = booking_api.create_booking(valid_booking_payload)
    booking_id = res.json()["bookingid"]
    return Booking_Info(id=booking_id, payload=valid_booking_payload)
    
    
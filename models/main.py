from pydantic import BaseModel, Field, TypeAdapter

class BookingDates(BaseModel):

    checkin : str
    checkout : str

class Booking_validation(BaseModel): #схема ответа информации о бронировании

    firstname : str
    lastname : str
    totalprice : int = Field(ge=0)
    depositpaid : bool
    bookingdates : BookingDates
    additionalneeds : str | None = None


class Validate_full_list(BaseModel): #схема ответа получения списка id всех бронирований

    bookingid : int = Field(ge=0)

full_list_adapter = TypeAdapter(list[Validate_full_list]) #проверка схемы всего списка

class Validate_create_booking(BaseModel): # схема ответа при создании бронирования

    bookingid : int = Field(ge=0)
    booking : Booking_validation



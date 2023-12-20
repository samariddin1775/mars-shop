from aiogram.dispatcher.filters.state import StatesGroup, State

class RegisterState(StatesGroup):
    full_name = State()
    phone_number = State()
    age = State()
    longitude = State()
    location = State()
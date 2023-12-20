from aiogram.dispatcher.filters.state import State, StatesGroup


class RegisterState(StatesGroup):
    name = State()
    phone = State()


class AddCarState(StatesGroup):
    photo = State()
    name = State()
    info = State()

class UpdateState(StatesGroup):
    id = State()
    select = State()
    name = State()
    photo = State()
    info = State()


class DeleteCarState(StatesGroup):
    id = State()

from aiogram.dispatcher.filters.state import StatesGroup, State


class ContactState(StatesGroup):
    text = State()


class AddproductState(StatesGroup):
    image = State()
    name = State()
   


class UpdateState(StatesGroup):
    id = State()
    select = State()
    photo = State()
    info = State()
    contact = State()
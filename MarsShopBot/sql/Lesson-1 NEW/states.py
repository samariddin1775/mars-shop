from aiogram.dispatcher.filters.state import StatesGroup, State


class ContactState(StatesGroup):
    text = State()


class AddproductState(StatesGroup):
    image = State()
    info = State()
    contact = State()
    price = State()
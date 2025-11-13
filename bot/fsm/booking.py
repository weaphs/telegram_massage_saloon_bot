from aiogram.fsm.state import State, StatesGroup

class BookingStates(StatesGroup):
    entering_name = State()
    entering_date = State()
    entering_time = State()
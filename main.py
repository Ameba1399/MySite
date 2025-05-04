import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Настройки
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')

# Инициализация
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

# Меню
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('👥 Пользователи'),
    KeyboardButton('📝 Отзывы'),
    KeyboardButton('⚙️ Настройки')
)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if str(message.from_user.id) == ADMIN_ID:
        await message.answer("Админ-панель:", reply_markup=main_menu)
    else:
        await message.answer("Доступ запрещён")

@dp.message_handler(text='👥 Пользователи')
async def users_menu(message: types.Message):
    # Реализация управления пользователями
    pass

@dp.message_handler(text='📝 Отзывы')
async def reviews_menu(message: types.Message):
    # Реализация модерации отзывов
    pass

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)

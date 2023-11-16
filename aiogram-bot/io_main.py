import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6513692439:AAFFgGmpXQfJzFsEUSiEP3FFK5QIZNqimO4")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Вы девушка должны загрузить мне два файла "  # noqa: F541
        f"один с разширением PDF, тот из которого ищем "  # noqa: F541
        f"второй с расширением XLSX, в котором ищем!"  # noqa: F541
    )

@dp.message()
async def save_file(message: types.Message, bot: Bot):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    name_file = message.document.file_name
    print(file_id)
    print(file)
    print(file_path)
    destination=f"C:\\robots\\RPA_telegram\\chat_files\\{name_file}"
    await bot.download_file(file_path, destination=destination)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




# @dp.message()
# async def save_file(message: types.Message, bot: Bot):
#     file_id = message.document.file_id
#     name_file = message.document.file_name
#     file = bot.get_file(file_id)
#     file_path = file.file_path
#     downloaded_file = bot.download_file(file)
#     print("Это print", downloaded_file)
#     document = message.document
#     # await bot.download(document)
#     await bot.download_file(file_path, name_file)
#     # destination=f"C:\\robots\\RPA_telegram\\chat_files\\{name_file}.pdf"
#     # print(name_file, destination)
#     # await bot.download(document, destination=destination)
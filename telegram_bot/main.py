import os

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

reply_keyboard = [
    ["Включить робота"],
    ["Проверить документы"],
    ["Выключить робота"],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


async def turn_on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    robot = "C:\\Program Files\\PIX\\Robot.exe"
    script = "C:\\robots\\financial_manager_process\\Check_excel\\test_test.pix"
    # print('"'+robot+'"' + " -f " + script)
    os.system('"'+robot+'"' + " -f " + script)


async def turn_off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # print("cmd.exe /c"+"Taskkill /IM '"'Robot.exe'"' /F")
    os.system("cmd.exe /c "+"Taskkill /IM Robot.exe /F")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(
        f"Привет {user.first_name}, я робот котрый проверяет твои акты сверки. ",
        reply_markup=markup)
    

def main():
    token="6513692439:AAFFgGmpXQfJzFsEUSiEP3FFK5QIZNqimO4"
    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(filters.Text("Включить робота"), turn_on))
    application.add_handler(MessageHandler(filters.Text("Выключить робота"), turn_off))
    application.add_handler(MessageHandler(filters.Text("Проверить документы"), echo))
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
    # application.idle()
    
if __name__ == '__main__':
    main()
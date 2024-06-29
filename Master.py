from telegram import Update
from telegram.ext import *
from BasicFunctions import *

# from filters import *

# VARIABLES
_token: str = get_tbtku_token()
_bot_username: str = get_tbtku_userName()


# COMMANDS
async def start_command(upd: Update, _context: ContextTypes.DEFAULT_TYPE) -> None:
    # log_printer_console(f"USER \"{upd.message.from_user.full_name}\" started conversation")
    _username: str = upd.message.from_user.full_name
    log_manager(f"USER \"{_username}\" started conversation")
    await upd.message.reply_text(
        f"Hello {_username}! Welcome to tbtKU (Thoughts Behind The KU) Telegram Bot!\ntbtKU FB Page: "
        f"https://www.facebook.com/tbtKU \ntbtKU FB Group: https://www.facebook.com/groups/tbtku ")
    await upd.message.reply_text(
        f"Currently I am Under Development, and\nI can understand English only (no Banglish or বাংলা)")


async def competition_submission_command(upd: Update, _context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def ku_stu_verification(upd: Update, _context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def help_command(upd: Update, _context: ContextTypes.DEFAULT_TYPE) -> None:
    await upd.message.reply_text("I am here to help you")


async def handle_message(upd: Update, _context: ContextTypes.DEFAULT_TYPE) -> None:
    _user_written_text: str = upd.message.text
    _username: str = upd.message.from_user.full_name
    log_manager(f"CONVERSATION: USER \"{_username}\" wrote \"{_user_written_text}\"")

    _response: str = handle_response(
        _user_written_text)  # getting reply from user defined function (defined in BasicFunctions)
    await upd.message.reply_text(_response)


async def error(upd: Update, _context: ContextTypes.DEFAULT_TYPE) -> None:
    log_manager(f"!!! ERROR !!! upd {upd} caused an error: {_context.error} ")


# handle RESPONSES

# ======================================================================================================================

# int main(void){
if __name__ == '__main__':
    log_manager("starting tbtKU TG bot")
    app_tbtku_tg_bot = Application.builder().token(_token).build()

    # Commands
    app_tbtku_tg_bot.add_handler(CommandHandler('start', start_command))
    app_tbtku_tg_bot.add_handler(CommandHandler('help', help_command))

    # Message Handler
    app_tbtku_tg_bot.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app_tbtku_tg_bot.add_error_handler(error)

    # Polls the bot
    log_manager("Polling... Working...")
    app_tbtku_tg_bot.run_polling(poll_interval=1)

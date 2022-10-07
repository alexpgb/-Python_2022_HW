# подключение логгеров:
# 1. https://habr.com/ru/company/wunderfund/blog/683880/?ysclid=l8xfo3ekeb846215106
# 2. https://python-scripts.com/logging-python?ysclid=l8xgushz5x630596710

print()

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, ContextTypes, Filters
import bots_command as bc
import logging 
import settings
from os.path import join, dirname

print()

program_action_logger = logging.getLogger('prog_action')
program_action_logger.setLevel(logging.INFO)
program_action_logger_handler = logging.FileHandler(join(dirname(__file__), 'prog_action.log'), mode = 'w', encoding='utf-8')
program_action_logger_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
program_action_logger_handler.setFormatter(program_action_logger_formatter)
program_action_logger.addHandler(program_action_logger_handler)

bot_logger = logging.getLogger('bot_action')
bot_logger.setLevel(logging.INFO)
bot_logger_logger_handler = logging.FileHandler(join(dirname(__file__), 'bot_action.log'), mode = 'w', encoding='utf-8')
bot_logger_logger_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
bot_logger_logger_handler.setFormatter(bot_logger_logger_formatter)
bot_logger.addHandler(bot_logger_logger_handler)


def main():

    program_action_logger.info(f'Модуль {__package__}{__name__}. Старт работы программы.')

    updater = Updater(token=settings.BOT_TOKEN)
    updater.dispatcher.add_handler(CommandHandler([bc.MSG_HELLO, bc.MSG_START, bc.MSG_HELP,\
         bc.MSG_CALC, bc.MSG_PHONE_BOOK, bc.MSG_QUIT, bc.MSG_UP, bc.MSG_CANCEL], bc.start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), bc.text_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, bc.unknown_handler))

    print('Сервер запущен')
    program_action_logger.info(f'Сервер запущен')

    updater.start_polling()
    updater.idle()

# print()

if __name__ == '__main__':
    main()
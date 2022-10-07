from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
import calc_bot.model_calc as cm
import phone_book_bot.model_pb as pbm
from main import bot_logger


MENU_CONTEXT_MAIN_MENU = 1
MENU_CONTEXT_CALC_MENU = 11
MENU_CONTEXT_PHONEBOOK_MENU = 12
MENU_CONTEXT_CALC_MENU_GET_FIRST_NUMBER = 111
MENU_CONTEXT_CALC_MENU_GET_SECOND_NUMBER = 112
MENU_CONTEXT_PHONEBOOK_MENU_GET_NEW_ITEM = 122
MENU_CONTEXT_PHONEBOOK_MENU_GET_NAME = 123
MENU_CONTEXT_PHONEBOOK_MENU_GET_PHONE = 124
MENU_CONTEXT_PHONEBOOK_MENU_GET_ID = 125
MENU_CONTEXT = MENU_CONTEXT_MAIN_MENU
MSG_START = 'start'
MSG_HELLO = 'hello'
MSG_HELP = 'help'
MSG_CALC = 'c'
MSG_PHONE_BOOK = 'p'
MSG_QUIT = 'q'
MSG_UP = 'up'
MSG_CANCEL = 'cancel'
CHOICE_ONE = '1'
CHOICE_TWO = '2'
CHOICE_THREE = '3'
CHOICE_FOUR = '4'
CHOICE_FIVE = '5'
CHOICE_SIX = '6'
CHOICE_SEVEN = '7'
CHOICE_EIGHT = '8'
MENU_CHOICE = ''
CALC_FIRST_OPERAND = ''
CALC_SECOND_OPERAND = ''
PHONE_BOOK_NAME = ''
PHONE_BOOK_PHONE = ''
MAIN_MENU = f'Введите команду:\n' \
          f'/{MSG_CALC} - Калькулятор комплексных чисел\n' \
          f'/{MSG_PHONE_BOOK}   - Телефонный справочник\n'\
          f'/{MSG_QUIT}    - завершение работы.'

CALC_MENU = \
    f'Выберите действие:\n' \
    f'{CHOICE_ONE} - сложение\n'\
    f'{CHOICE_TWO} - вычитание\n'\
    f'{CHOICE_THREE} - умножение\n'\
    f'{CHOICE_FOUR} - деление\n'\
    f'/{MSG_UP} - выход в главное меню'

PHONE_BOOK_MENU = \
    f'Выберите действие:\n' \
    f'{CHOICE_ONE} - отобразить все записи\n'\
    f'{CHOICE_TWO} - добавить запись\n'\
    f'{CHOICE_THREE} - отфильтровать по наименованию\n'\
    f'{CHOICE_FOUR} - отфильтровать по номеру\n'\
    f'{CHOICE_FIVE} - удалить запись\n'\
    f'/{MSG_UP} - выход в главное меню'

FIRST_OPERAND_NAME_DICT = {CHOICE_ONE:'первый операнд', CHOICE_TWO:'уменьшаемое', CHOICE_THREE:'первый операнд', CHOICE_FOUR: 'делимое'}
SECOND_OPERAND_NAME_DICT = {CHOICE_ONE:'второй операнд', CHOICE_TWO:'вычитаемое', CHOICE_THREE:'второй операнд', CHOICE_FOUR: 'делитель'}
PHONE_BOOK_TEXT_GET_NEW_ITEM = f'Укажите Имя и телефон через пробел :'
PHONE_BOOK_TEXT_GET_NAME = f'Укажите Имя :'
PHONE_BOOK_TEXT_GET_PHONE = f'Укажите Телефон :'
PHONE_BOOK_TEXT_GET_ID = f'Укажите ID записи :'

# обрабатывает команды "hello", "start", "help", "calc", "pb", "q", "up", "cancel"
def start(update: Update, context: CallbackContext):   # 
    print(f'Command_handler. {update.message.text}')
    bot_logger.info(f'{update.message.date} from: {update.effective_chat.id}, user: {update.effective_user.id}, send {update.message.text}')
    global MENU_CHOICE
    global MENU_CONTEXT
    reply_text = f'Команда не определена.'
    msg = update.message.text.strip().replace('/','')
    if msg in [MSG_QUIT]:
            MENU_CONTEXT = MENU_CONTEXT_MAIN_MENU
            MENU_CHOICE = ''
            reply_text = f'Bye'
    elif MENU_CONTEXT in [MENU_CONTEXT_MAIN_MENU]:
        if msg in [MSG_START, MSG_HELP, MSG_HELLO]:
            reply_text = MAIN_MENU
        elif msg in [MSG_CALC]:
            MENU_CONTEXT = MENU_CONTEXT_CALC_MENU
            reply_text = CALC_MENU
        elif msg == MSG_PHONE_BOOK:
            MENU_CONTEXT = MENU_CONTEXT_PHONEBOOK_MENU
            reply_text = PHONE_BOOK_MENU
    elif MENU_CONTEXT in [MENU_CONTEXT_CALC_MENU, MENU_CONTEXT_PHONEBOOK_MENU]:
        if msg == MSG_UP:
            MENU_CONTEXT = MENU_CONTEXT_MAIN_MENU
            MENU_CHOICE = ''
            reply_text = MAIN_MENU
    elif MENU_CONTEXT in [MENU_CONTEXT_CALC_MENU_GET_FIRST_NUMBER, MENU_CONTEXT_CALC_MENU_GET_SECOND_NUMBER,\
        MENU_CONTEXT_PHONEBOOK_MENU_GET_NEW_ITEM, MENU_CONTEXT_PHONEBOOK_MENU_GET_NAME, MENU_CONTEXT_PHONEBOOK_MENU_GET_PHONE] \
            and msg == MSG_CANCEL:
        if MENU_CONTEXT in [MENU_CONTEXT_CALC_MENU_GET_FIRST_NUMBER, MENU_CONTEXT_CALC_MENU_GET_SECOND_NUMBER]:
            MENU_CONTEXT = MENU_CONTEXT_CALC_MENU
            MENU_CHOICE = ''
            reply_text = CALC_MENU
        elif MENU_CONTEXT in [MENU_CONTEXT_PHONEBOOK_MENU_GET_NEW_ITEM, \
                MENU_CONTEXT_PHONEBOOK_MENU_GET_NAME, \
                MENU_CONTEXT_PHONEBOOK_MENU_GET_PHONE]:
            MENU_CHOICE = ''
            MENU_CONTEXT = MENU_CONTEXT_PHONEBOOK_MENU
            reply_text = PHONE_BOOK_MENU
    bot_logger.info(f'answer {reply_text}')
    update.message.reply_text(reply_text)

# обрабатывает любой текст полученный на вводе
def text_handler(update: Update, context: CallbackContext):
    print(f'Text_handler. {update.message.text}')
    bot_logger.info(f'{update.message.date} from: {update.effective_chat.id}, user: {update.effective_user.id}, send {update.message.text}')
    global MENU_CONTEXT
    global MENU_CHOICE
    global CALC_FIRST_OPERAND
    global CALC_SECOND_OPERAND
    item_list = []
    reply_text = f'Команда не определена.'
    msg = update.message.text.strip()
    # 
    if MENU_CONTEXT in [MENU_CONTEXT_CALC_MENU, MENU_CONTEXT_CALC_MENU_GET_FIRST_NUMBER, MENU_CONTEXT_CALC_MENU_GET_SECOND_NUMBER]:
        if MENU_CONTEXT == MENU_CONTEXT_CALC_MENU and msg in [CHOICE_ONE, CHOICE_TWO, CHOICE_THREE, CHOICE_FOUR]:                            # 
            MENU_CHOICE = msg                                                                   # запоминаем, какую операцию выбрали
            MENU_CONTEXT = MENU_CONTEXT_CALC_MENU_GET_FIRST_NUMBER
            reply_text = f'Укажите {FIRST_OPERAND_NAME_DICT[MENU_CHOICE]} в формате a + bi (/cancel - отмена):'
        else:
            if MENU_CONTEXT in [MENU_CONTEXT_CALC_MENU_GET_FIRST_NUMBER]:                          # пришел первый операнд
                if cm.complex_num_as_str_is_valid(msg):                                            # проверка первого операнда на корректность
                    # выводим запрос, переключаем контектст
                    CALC_FIRST_OPERAND = cm.complex_num_as_str_to_complex(msg)
                    reply_text = f'Укажите {SECOND_OPERAND_NAME_DICT[MENU_CHOICE]} в формате a + bi (/cancel - отмена):'
                    MENU_CONTEXT = MENU_CONTEXT_CALC_MENU_GET_SECOND_NUMBER
                else:
                    reply_text = f'Ошибка парсинга строки.'\
                        f'Укажите {FIRST_OPERAND_NAME_DICT[MENU_CHOICE]} в формате a + bi (/cancel - отмена):'
            elif MENU_CONTEXT in [MENU_CONTEXT_CALC_MENU_GET_SECOND_NUMBER]:                       # получили первый операнд
                if cm.complex_num_as_str_is_valid(msg):                                            # проверка  операнда на корректность
                    # выводим запрос
                    CALC_SECOND_OPERAND = cm.complex_num_as_str_to_complex(msg)
                    # вызываем нужный метод из калькулятора
                    if MENU_CHOICE == CHOICE_ONE:
                        r = cm.complex_num_sum(CALC_FIRST_OPERAND, CALC_SECOND_OPERAND)
                    elif MENU_CHOICE == CHOICE_TWO:
                        r = cm.complex_num_sub(CALC_FIRST_OPERAND, CALC_SECOND_OPERAND)
                    elif MENU_CHOICE == CHOICE_THREE:
                        r = cm.complex_num_mult(CALC_FIRST_OPERAND, CALC_SECOND_OPERAND)
                    elif MENU_CHOICE == CHOICE_FOUR:
                        r = cm.complex_num_div(CALC_FIRST_OPERAND, CALC_SECOND_OPERAND)
                    else:
                        r = None
                    if not r:
                        reply_text = f'Ошибка выполнения операции.'
                    else:
                        reply_text = str(r)
                    reply_text +=  f'\n\n' + CALC_MENU
                    # reply_text =  f'Операция выполнена\n\n' + CALC_MENU
                    # переключаем контектст
                    MENU_CONTEXT = MENU_CONTEXT_CALC_MENU
                    MENU_CHOICE = ''
                    CALC_FIRST_OPERAND = ''
                    CALC_SECOND_OPERAND =''
                else:                     
                    reply_text = f'Ошибка парсинга строки.'\
                        f'Укажите {SECOND_OPERAND_NAME_DICT[MENU_CHOICE]} в формате a + bi (/cancel - отмена):'
    elif MENU_CONTEXT in [MENU_CONTEXT_PHONEBOOK_MENU, \
        MENU_CONTEXT_PHONEBOOK_MENU_GET_NEW_ITEM, MENU_CONTEXT_PHONEBOOK_MENU_GET_NAME, MENU_CONTEXT_PHONEBOOK_MENU_GET_PHONE,\
             MENU_CONTEXT_PHONEBOOK_MENU_GET_ID]:
        if MENU_CONTEXT == MENU_CONTEXT_PHONEBOOK_MENU and msg in [CHOICE_ONE, CHOICE_TWO, CHOICE_THREE, CHOICE_FOUR, CHOICE_FIVE]:                            # 
            MENU_CHOICE = msg                                                                   # запоминаем, какую операцию выбрали
            if msg ==  CHOICE_ONE:                                                              # печать справочника
                item_list = pbm.get_item()
                reply_text = pbm.get_item_list_as_str(item_list)
                reply_text +=  '\n\n' + PHONE_BOOK_MENU
                MENU_CHOICE = ''
            elif msg == CHOICE_TWO:                                                             # добавление записи
                reply_text = PHONE_BOOK_TEXT_GET_NEW_ITEM
                MENU_CONTEXT = MENU_CONTEXT_PHONEBOOK_MENU_GET_NEW_ITEM
            elif msg == CHOICE_THREE:                                                           # поиск по наименованию
                reply_text = PHONE_BOOK_TEXT_GET_NAME
                MENU_CONTEXT = MENU_CONTEXT_PHONEBOOK_MENU_GET_NAME
            elif msg == CHOICE_FOUR:                                                            # поиск по номеру телефона
                reply_text = PHONE_BOOK_TEXT_GET_PHONE
                MENU_CONTEXT = MENU_CONTEXT_PHONEBOOK_MENU_GET_PHONE
            elif msg == CHOICE_FIVE:                                                            # удаление по ID
                reply_text = PHONE_BOOK_TEXT_GET_ID
                MENU_CONTEXT = MENU_CONTEXT_PHONEBOOK_MENU_GET_ID
        else:
            if MENU_CONTEXT in [MENU_CONTEXT_PHONEBOOK_MENU_GET_NEW_ITEM]:                       # пришло имя и телефон через пробел
                if pbm.msg_for_new_item_is_valid(msg):                                                                         # проверка на корректность
                    # добавляем в справочник 
                    item_as_dict = pbm.msg_to_dict(msg)
                    if pbm.save_item_to_bd(item_as_dict):
                        reply_text = f'Запись добавлена.'
                    else:
                        reply_text = f'Ошибка при добавлении записи.'
                    reply_text += '\n\n' + PHONE_BOOK_MENU
                    MENU_CONTEXT = MENU_CONTEXT_PHONEBOOK_MENU
                    MENU_CHOICE = ''
                else:
                    reply_text = f'Ошибка парсинга строки.\n' + PHONE_BOOK_TEXT_GET_NEW_ITEM
            elif MENU_CONTEXT in [MENU_CONTEXT_PHONEBOOK_MENU_GET_NAME]:                         # получили Имя
                if True:                                                                         # проверка  на корректность
                    # делаем запрос, выводим результат
                    item_list = pbm.get_item({'firstName': msg})
                    reply_text = pbm.get_item_list_as_str(item_list)
                    reply_text +=  '\n\n' + PHONE_BOOK_MENU
                    MENU_CONTEXT = MENU_CONTEXT_PHONEBOOK_MENU
                    MENU_CHOICE = ''
            elif MENU_CONTEXT in [MENU_CONTEXT_PHONEBOOK_MENU_GET_PHONE]:                        # получили Номер
                if True:                                                                         # проверка  на корректность
                    # делаем запрос, выводим результат
                    item_list = pbm.get_item({'phoneNumber': msg})
                    reply_text = pbm.get_item_list_as_str(item_list)
                    reply_text +=  '\n\n' + PHONE_BOOK_MENU
                    MENU_CONTEXT = MENU_CONTEXT_PHONEBOOK_MENU
                    MENU_CHOICE = ''
            elif MENU_CONTEXT in [MENU_CONTEXT_PHONEBOOK_MENU_GET_ID]:                           # получили ID
                if msg.isdigit():                                                                # проверка  на корректность
                    # делаем запрос, выводим результат
                    item_count = pbm.delete_item({'id': msg})
                    reply_text = f'Удалено {item_count} записей.'
                    reply_text +=  '\n\n' + PHONE_BOOK_MENU
                    MENU_CONTEXT = MENU_CONTEXT_PHONEBOOK_MENU
                    MENU_CHOICE = ''
                else:                     
                    reply_text = f'Ошибка парсинга строки.'\
                        f'Укажите {SECOND_OPERAND_NAME_DICT[MENU_CHOICE]} в формате a + bi (/cancel - отмена):'
    bot_logger.info(f'answer {reply_text}')
    update.message.reply_text(reply_text)

# обрабатывает команды не описанныее выше
def unknown_handler(update: Update, context: CallbackContext):
    print(f'Unkown_handler. {update.message.text}')
    update.message.reply_text(f'Команда не определена.')
# -*- coding: utf-8 -*-

from telebot import apihelper, TeleBot
from bot import states
from bot.config import States
from bot.private import TOKEN, HTTP_PROXY, HTTPS_PROXY
import time
from bot import dbworker


apihelper.proxy = {
    'http': HTTP_PROXY,
    'https': HTTPS_PROXY
}

bot = TeleBot(TOKEN, threaded=False)


@bot.message_handler(commands=["start", "help"])
def start(message):
    username = dbworker.get_user(message.from_user)[0][0]
    if not username:
        dbworker.add_user(message.from_user)
        username = message.from_user.first_name
    bot.send_message(message.chat.id, 'превед, {}! ^_^ \n'
                     'чтобы добавить прочитанную книгу, нажми: /add_my_book\n'
                     'ту, что планируешь / читаешь: /add'.format(username))


@bot.message_handler(commands=["add"])
def add(message):
    bot.send_message(message.chat.id, 'Введи название книги и автора через запятую')
    states.set_state(message.chat.id, States.S_ADD.value)


@bot.message_handler(commands=["add_my_book"])
def add_my(message):
    bot.send_message(message.chat.id, 'Введи название книги')
    states.set_state(message.chat.id, States.S_ADD_MY.value)


@bot.message_handler(func=lambda message: states.get_state(message.chat.id) == States.S_ADD_MY.value)
def exists(message):
    book = dbworker.get_book(message.text)
    if book:
        bid, author, name = book
        dbworker.add_user_books(user_id=message.from_user.id, book_id=bid, read=True)
        states.set_state(message.chat.id, States.S_DONE.value)
        bot.send_message(message.chat.id, 'Молодец! книга "{}" автора {} была отмечена как прочитанная.'
                         .format(name, author))

    else:
        bot.send_message(message.chat.id, 'Книга отсутствует в БД\n'
                                          'Введи полное название книги и автора через запятую^^')
        states.set_state(message.chat.id, States.S_NONE.value)


@bot.message_handler(func=lambda message: states.get_state(message.chat.id) == States.S_ADD.value)
@bot.message_handler(func=lambda message: states.get_state(message.chat.id) == States.S_NONE.value)
def insert(message):
    print('!')
    if ',' in message.text:
        book, author = message.text.split(', ')
        bid = dbworker.add_book(book, author)
        print('added')
        bot.send_message(message.chat.id, 'Книга {} добавлена'.format(book))
        if states.get_state(message.chat.id) == States.S_NONE.value:
            bid, author, name = dbworker.get_book_by_id(bid)
            dbworker.add_user_books(message.from_user.id, bid, True)
            bot.send_message(message.chat.id, 'Молодец! книга "{}" автора {} была отмечена как прочитанная.'
                             .format(name, author))
        states.set_state(message.chat.id, States.S_DONE.value)
    else:
        bot.send_message(message.chat.id, 'через запятую ! ')
        if not states.get_state(message.chat.id) == States.S_NONE.value:
            states.set_state(message.chat.id, States.S_ADD.value)


@bot.message_handler(func=lambda message: states.get_state(message.from_user.id) == States.S_DONE.value)
def done(message):
    bot.send_message(message.chat.id, 'Что ты хочешь? чтобы добавить книгу, нажми /add\n')


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, 'непонятно! ^_^')


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print('>_<:', e)
            time.sleep(1)


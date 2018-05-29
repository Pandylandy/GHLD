# -*- coding: utf-8 -*-

from telebot import apihelper, TeleBot
from bot.private import TOKEN, HTTP_PROXY, HTTPS_PROXY

apihelper.proxy = {
    'http': HTTP_PROXY,
    'https': HTTPS_PROXY
}

bot = TeleBot(TOKEN, threaded=False)


@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id, 'Hi! ^_^')


if __name__ == '__main__':
    bot.polling()

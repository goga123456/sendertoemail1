import telebot
import config # подключаем конфиг, чтобы взять с него токен бота

bot = telebot.TeleBot(config.config['TOKEN'])
print(bot.get_me())
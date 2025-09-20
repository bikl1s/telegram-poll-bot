import telebot
from telebot import types
from loguru import logger

bot = telebot.TeleBot("7920281966:AAGK6czGjA_--SIbnRXCoZKCoTixI85_Ltw")
logger.success("Экземпляр бота создан")
m = types.Message


@bot.message_handler(['start'])
def start(msg: m):
    logger.info(f"Пользователь {msg.chat.id} нажал /start")
    bot.send_message(msg.chat.id, "Пройти опрос - /lets_go")

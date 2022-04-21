
# Импортируем необходимые классы.
import logging
import random

from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler, dispatcher

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5331086748:AAHV-K3Q6H0G1IvQTx3EN9VI__BsZZqwkEE'

reply_keyboard = [['/prediction', '/horoscope'],
                  ['/advice', '/future']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def start(update, context):
    update.message.reply_text(
        "Добро пожаловать! Я бот-гадалка, ведьма в седьмом поколении. Вот, что я умею:"
    )
    update.message.reply_text(
        "- Сделать предсказание на день" '\n'
        "- Составить гороскоп на неделю" '\n'
        "- Попросить совета у шара судьбы" '\n'
        "- Сделать карточный расклад на будущее" '\n',
        reply_markup=markup
    )


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


f = open('predictions_day.txt', 'r', encoding='UTF-8')
predictions_day = f.read().split('\n')
f.close()


def prediction(update, context):
    if update.message.text == 'Предсказание':
        update.message.reply_text(
            "Хорошо! Дайте-ка подумать...",
        )
        answer = random.choice(predictions_day)

        update.message.reply_text(answer)


def horoscope(update, context):

    update.message.reply_text(
        "Хорошо! Какой у вас знак зодиака?",
    )


def advice(update, context):

    update.message.reply_text(
        "Хорошо! Какой у вас вопрос?",
    )


def future(update, context):

    update.message.reply_text(
        "Хорошо! Так, карты говорят...",
    )


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("prediction", prediction))
    dp.add_handler(CommandHandler("horoscope", horoscope))
    dp.add_handler(CommandHandler("advice", advice))
    dp.add_handler(CommandHandler("future", future))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))

    prediction_handler = MessageHandler(Filters.text, prediction)
    dp.add_handler(prediction_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
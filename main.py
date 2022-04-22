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


def go_text(update, context):
    if update.message.text == 'Предсказание' or update.message.text == 'предсказание' \
            or update.message.text == 'предсказание на день' \
            or update.message.text == 'Предсказание на день':
        prediction(update, context)
    elif update.message.text == 'гороскоп' or update.message.text == 'Гороскоп' or update.message.text == 'расскажи про гороскоп'\
            or update.message.text == 'Расскажи про гороскоп':
        horoscope(update, context)
    else:
        update.message.reply_text(
            "Не понимаю... Напишите, что вы хотите или попросите помощи.",
        )


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


f = open('predictions_day.txt', 'r', encoding='UTF-8')
predictions_day = f.read().split('\n')
f.close()


def prediction(update, context):
        update.message.reply_text(
            "Хорошо! Дайте-ка подумать...",
        )
        answer = random.choice(predictions_day)

        update.message.reply_text(answer)


def horoscope(update, context):
    update.message.reply_text(
        "Хорошо! Какой у вас знак зодиака?",
    )

    if update.message.text == 'овен' or update.message.text == 'Овен':
        update.message.reply_text(
            "Какой замечательный знак! Вам предстоит сделать много полезного. Не исключено, "
            "что в апреле вы будете принимать участие в каких-то общественных мероприятиях, решать вопросы, "
            "важные для всех. Старайтесь избегать любых проявлений легкомыслия: оно будет совершенно неуместным."
            "Поскольку дел будет необычно много, привычный вам жизненный ритм может измениться, от комфортного графика "
            "придется отказаться. Вы не пожалеете об этом, легко перенесете любые неудобства.",
        )
    if update.message.text == 'телец' or update.message.text == 'Телец':
        update.message.reply_text(
            "Тельцы просто прекрасны! Эта неделя хорошо подойдет для того, чтобы взяться за что-то новое и необычное."
            "Творческий потенциал будет"
            "высоким, у вас появятся хорошие идеи и не возникнет проблем с их осуществлением. "
            "Станет ясно, как справиться с непростыми задачами, возникшими в последнее время. Будет много неожиданных "
            "встреч, удивительных совпадений. Старайтесь обращать внимание на все, что выходит за рамки обычного и "
            "привычного."
        )
    if update.message.text == 'Близнецы' or update.message.text == 'близнецы':
        update.message.reply_text(
            "Даже привычные дела на этой неделе могут даваться вам сложнее, чем обычно. Это, конечно, не значит,"
            "что нужно все отложить и ничем не заниматься. Просто будьте готовы к трудностям, не требуйте от себя"
            "невозможного и не спешите. Неделя не подходит для того, чтобы принимать участие в каких-то авантюрах."
            "А вот на поддержку близких можно рассчитывать в течение всей недели. Да и в помощи вам не откажут, "
            "если вы за ней обратитесь. "
        )
    if update.message.text == '' or update.message.text == '':
        update.message.reply_text(

        )

    if update.message.text == '' or update.message.text == '':
        update.message.reply_text(

        )
    if update.message.text == '' or update.message.text == '':
        update.message.reply_text(

        )
    if update.message.text == '' or update.message.text == '':
        update.message.reply_text(

        )
    if update.message.text == '' or update.message.text == '':
        update.message.reply_text(

        )
    if update.message.text == '' or update.message.text == '':
        update.message.reply_text(

        )
    if update.message.text == '' or update.message.text == '':
        update.message.reply_text(

        )
    if update.message.text == '' or update.message.text == '':
        update.message.reply_text(

        )
    if update.message.text == '' or update.message.text == '':
        update.message.reply_text(

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

    start_handler = MessageHandler(Filters.text, go_text)
    dp.add_handler(start_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
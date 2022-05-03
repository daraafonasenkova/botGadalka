import logging
import random
import time
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler, dispatcher

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

# пример эмодзи, другие можно скачать в интернете

emoji = ['🛁', '🚴', '🚀', '🚁', '🚂', '🚃', '🚌', '🚎', '🚑', '🚒', '🚓', '🦆', '🚕', '🦚', '🦞', '🚗',
         '🦑', '🚚', '🦢', '🦟', '🦠', '🦅', '🦀', '🦗', '🦋', '🚜', '🦇', '🦔', '🦓', '🚣', '🦒', '🦎',
         '🚶', '🛌', '🛒', '🛩', '🛰', '🛸', '🤔', '🤐', '🤓', '🤡', '🤫', '🥐', '🥕', '🥝', '🥦', '🥾', '🔮']

logger = logging.getLogger(__name__)

TOKEN = '5331086748:AAHV-K3Q6H0G1IvQTx3EN9VI__BsZZqwkEE'
# TOKEN = '5309878405:AAH2Rqmp3R6m_d-3gjpvfhNqTM_Dh3QQSTM'

reply_keyboard = [['/prediction', '/horoscope'],
                  ['/advice', '/future'],
                  ['/help']]
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
    #return 1


def help(update, context):
    update.message.reply_text(
        "Вот более подробный список команд:"
    )
    update.message.reply_text(
        "/horoscope - составлю гороскоп специально для Вас" '\n'
        "/prediction - сделаю Вам предсказание" '\n'
        "/advice - попрошу совета у шара судьбы" '\n'
        "/future - сделаю расклад на будущее" '\n',
        reply_markup = markup
    )


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


f = open('predictions_day.txt', 'r', encoding='UTF-8')
predictions_day = f.read().split('\n')
f.close()

f = open('advice.txt', 'r', encoding='UTF-8')
advicetxt = f.read().split('\n')
f.close()

f = open('future_prediction.txt', 'r', encoding='UTF-8')
future_prediction = f.read().split('\n')
f.close()


def prediction(update, context):
        update.message.reply_text(
            "Хорошо! Дайте-ка подумать...",
        )
        time.sleep(2)
        update.message.reply_text(
            '😱',
        )
        answer = random.choice(predictions_day)

        update.message.reply_text(answer)


def horoscope1(update, context):
    reply_keyboard = [['Овен', 'Телец', 'Близнецы', 'Рак',
                       'Лев', 'Дева', 'Весы', 'Скорпион',
                       'Стрелец', 'Весы', 'Водолей']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        "Хорошо! Какой у вас знак зодиака?", reply_markup=markup_key)

    return 1


def horoscope(update, context):
    zodiac = update.message.text
    logger.info(zodiac)

    if zodiac == 'овен' or zodiac == 'Овен':
        update.message.reply_text(
            "Какой замечательный знак! Вам предстоит сделать много полезного. Не исключено, "
            "что в апреле вы будете принимать участие в каких-то общественных мероприятиях, решать вопросы, "
            "важные для всех. Старайтесь избегать любых проявлений легкомыслия: оно будет совершенно неуместным."
            "Поскольку дел будет необычно много, привычный вам жизненный ритм может измениться, от комфортного графика "
            "придется отказаться. Вы не пожалеете об этом, легко перенесете любые неудобства.",
        )
    elif zodiac == 'телец' or zodiac == 'Телец':
        update.message.reply_text(
            "Тельцы просто прекрасны! Эта неделя хорошо подойдет для того, чтобы взяться за что-то новое и необычное."
            "Творческий потенциал будет"
            "высоким, у вас появятся хорошие идеи и не возникнет проблем с их осуществлением. "
            "Станет ясно, как справиться с непростыми задачами, возникшими в последнее время. Будет много неожиданных "
            "встреч, удивительных совпадений. Старайтесь обращать внимание на все, что выходит за рамки обычного и "
            "привычного.", reply_markup=markup
        )
    elif zodiac == 'Близнецы' or zodiac == 'близнецы':
        update.message.reply_text(
            "Близнецы - очень хороший знак! Даже привычные дела на этой неделе могут даваться вам сложнее, чем обычно. "
            "Это, конечно, не значит,"
            "что нужно все отложить и ничем не заниматься. Просто будьте готовы к трудностям, не требуйте от себя"
            "невозможного и не спешите. Неделя не подходит для того, чтобы принимать участие в каких-то авантюрах."
            "А вот на поддержку близких можно рассчитывать в течение всей недели. Да и в помощи вам не откажут, "
            "если вы за ней обратитесь. ", reply_markup=markup
        )
    elif zodiac == 'Рак' or zodiac == 'рак':
        update.message.reply_text(
            "Замечательный знак! Придется потрудиться, и вас это, скорее всего, порадует. Появятся интересные дела и "
            "новые проекты. "
            "Благодаря им вы многому научитесь и познакомитесь с людьми, которые позже не раз вас поддержат. "
            "Вероятны какие-то неожиданные события, удивительные происшествия. Они могут повлиять на ваши планы. "
            "Не исключено, что вы решите сосредоточиться на совершенно новых делах, а все остальное отложить. Близкие "
            "будут этому очень рады и поддержат вас.", reply_markup=markup
        )

    elif zodiac == 'Лев' or zodiac == 'лев':
        update.message.reply_text(
            "Какой хороший знак! Старайтесь выполнять все обещания, которые дали раньше, не нарушать договоренностей, "
            "не подводить тех, кто "
            "на вас рассчитывает, даже если кажется, что речь идет о пустяках. Это позволит избежать проблем в "
            "отношениях с близкими и знакомыми.", reply_markup=markup
        )
    elif zodiac == 'Дева' or zodiac == 'дева':
        update.message.reply_text(
            "Все Девы такие хорошие! Стоит поторопиться: можно сделать много полезного. Важно не откладывать на потом "
            "решение сложных задач. "
            "Напротив, лучше начать день именно с них: так вы и справитесь быстрее, и результат получите превосходный."
            "Если возникнут трудности, близкие охотно помогут, но вы постараетесь не злоупотреблять их добротой.", reply_markup=markup
        )
    elif zodiac == 'Весы' or zodiac == 'весы':
        update.message.reply_text(
            "Какой прекрасный знак! Вы завершите то, над чем долго трудились, и останетесь довольны результатами "
            "своих стараний. "
            "Вероятны успехи в учебе. Информация будет запоминаться легко, ни одна важная деталь от вас не ускользнет. "
            "Благодаря новым знаниям и опыту, полученному раньше, вы вскоре сможете укрепить свои профессиональные "
            "позиции.", reply_markup=markup
        )
    elif zodiac == 'скорпион' or zodiac == 'Скорпион':
        update.message.reply_text(
            "Такой классный знак! Кажется, что нужно успеть очень многое, и это заставляет вас нервничать. Но стоит "
            "подумать, всеми ли "
            "запланированными делами нужно заниматься именно сейчас. "
            "Наверняка вы поймете, что что-то можно просто отложить. Ваших собственных знаний и навыков окажется "
            "достаточно, чтобы решить непростые задачи, и неважно, насколько новыми для вас они будут. Позже появится "
            "шанс договориться о сотрудничестве с человеком, которому многое по силам.", reply_markup=markup
        )
    elif zodiac == 'стрелец' or zodiac == 'Стрелец':
        update.message.reply_text(
            "Стрельцы такие замечательные! На этой неделе вы по-новому взглянете на то, что прежде казалось привычным, "
            "заметите вещи, на которые "
            "прежде не обращали внимания. Дел будет немало. Не исключено, что придется скорректировать привычки, чтобы "
            "успевать больше. Важной будет самодисциплина. Не всегда легко будет противостоять собственным слабостям, "
            "но вы справитесь.", reply_markup=markup
        )
    elif zodiac == 'Козерог' or zodiac == 'Козерог':
        update.message.reply_text(
            "Какой хороший знак! Трудновато будет смотреть на вещи реально: собственные мечты покажутся вам очень "
            "привлекательными и могут "
            "превратиться в иллюзии. Могут сбить с толку чужие слова и обещания. Вы склонны верить в то, что нравится, "
            "отметая любые сомнения. Здоровый скепсис вам сейчас не помешал бы. Самое важное – проверять любую "
            "информацию, отделять слухи и сплетни от фактов. Не стоит участвовать в интригах, они едва ли будут вам полезны.",
            reply_markup=markup
        )
    elif zodiac == 'Водолей' or zodiac == 'водолей':
        update.message.reply_text(
            "Водолеи такие хорошие! Неделя не принесет серьезных проблем, если вы не станете рассчитывать на везение, "
            "будете ответственно "
            "относиться ко всему, за что беретесь. Старайтесь не идти на поводу у своих капризов и мимолетных желаний."
            "Не поддавайтесь соблазну отложить все сложное и неприятное на потом. Умение сохранять самообладание и не "
            "поддаваться на провокации позволит избежать проблем в личных отношениях. Вы поможете близким справиться с "
            "трудностями, помирите тех, кто был в ссоре.", reply_markup=markup
        )

    elif zodiac == 'Рыбы' or zodiac == 'рыбы':
        update.message.reply_text(
            "Прекрасный знак! Вы сможете быстро найти общий язык с очень разными людьми, понравиться даже тем, кто "
            "прежде не испытывал "
            "к вам симпатии. Отношения, прежде складывавшиеся напряженно, станут гораздо гармоничнее. "
            "Будет много необычных встреч. Если вы захотите обзавестись новыми знакомыми, сделать это окажется "
            "нетрудно. Вам может не хватать усидчивости и усердия, порой будет появляться желание бросить начатое на "
            "полпути. Сделайте над собой усилие и доведите дело до конца, ведь оно того стоит.", reply_markup=markup
        )
    return ConversationHandler.END


def advice(update, context):
    update.message.reply_text(
        "Хорошо! Загадайте что-нибудь, только мне не говорите.",
    )
    update.message.reply_text(
        '🔮',
    )
    time.sleep(2)
    answer = random.choice(advicetxt)
    update.message.reply_text(f'Шар говорит: {answer}')


def future(update, context):
    update.message.reply_text(
        "Хорошо! Так, карты говорят...",
    )
    update.message.reply_text(
        '🤔',
    )
    time.sleep(2)
    answer = random.choice(future_prediction)
    update.message.reply_text(answer)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('horoscope', horoscope1)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, horoscope)],
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler("prediction", prediction))
    dp.add_handler(CommandHandler("horoscope", horoscope1))
    dp.add_handler(CommandHandler("advice", advice))
    dp.add_handler(CommandHandler("future", future))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
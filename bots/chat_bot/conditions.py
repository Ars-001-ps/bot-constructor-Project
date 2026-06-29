from bots.gpt_service import ask_gpt

def greeting(message):
    message = message.lower().strip()

    if message in (
        'привет',
        'здарова',
        'здравствуй',
        'здравствуйте',
        'добрый день',
        'доброе утро',
        'добрый вечер',
    ):
        return 'Привет! Чем могу помочь?'

    if message in (
        'пока',
        'до свидания',
        'до встречи',
    ):
        return 'До встречи!'

    return None

def how_are_you(message):
    message = message.lower().strip()

    if message in (
        'как дела',
        'как дела?',
        'как ты',
        'как ты?',
        'как поживаешь',
    ):
        return 'Отлично! Спасибо, что спросил.'

    return None

def who_are_you(message):
    message = message.lower().strip()

    if message in (
        'кто ты',
        'ты кто',
        'представься',
    ):
        return 'Я чат-бот, написанный на Python.'

    return None

def what_can_you_do(message):
    message = message.lower().strip()

    if message in (
        'что ты умеешь',
        'что умеешь',
        'что ты можешь',
        'твои возможности',
    ):
        return 'Я могу отвечать на вопросы и общаться с тобой.'

    return None

def who_created_you(message):
    message = message.lower().strip()

    if message in (
        'кто тебя создал',
        'кто тебя сделал',
        'кто твой создатель',
    ):
        return 'Меня создал мой разработчик - Арсений.'

    return None

def your_name(message):
    message = message.lower().strip()

    if message in (
        'как тебя зовут',
        'твое имя',
        'как твоё имя',
    ):
        return 'Я чат-бот, и у меня нет конкретного имени.'

    return None


def joke_request(message):
    message = message.lower().strip()

    if message in (
        'расскажи шутку',
        'пошути',
        'рассмеши меня',
    ):
        return 'Почему программисты любят Python? Потому что он не кусается'

    return None

def help_request(message):
    message = message.lower().strip()

    if message in (
        'помоги',
        'мне нужна помощь',
        'можешь помочь',
    ):
        return 'Конечно! Напиши подробнее, что тебе нужно.'

    return None

def handle_static_response(message):
    handlers = [
        greeting,
        how_are_you,
        who_are_you,
        what_can_you_do,
        who_created_you,
        your_name,
        joke_request,
        help_request,
    ]

    for handler in handlers:
        response = handler(message)
        if response:
            return response

    return None

def response(message):
    static = handle_static_response(message)
    if static:
        return static
    return ask_gpt(message)
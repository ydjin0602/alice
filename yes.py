# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}

# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])

def main():
# Функция получает тело запроса и возвращает ответ.
    logging.info('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )

# Функция для непосредственной обработки диалога.
def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new']:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.
        sessionStorage[user_id] = {
            'suggests': "Стоп"
        }


        res['response']['text'] = 'Привет, меня зовут Алиса и в этом диалоге я буду отвечать на любой ваш запрос "ДА". Чтобы закончить диалог со мной введите "СТОП".'
        return

    # Обрабатываем ответ пользователя.
    if req['request']['original_utterance'].lower() in ['стоп']:
        # Пользователь сказал стоп
        res['response']['text'] = 'Конец диалога'
        return

    # Если нет, то убеждаем его купить слона!
    res['response']['text'] = 'Да'
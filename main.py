import random
import openai
import vk_api
import sqlite3
from langdetect import detect
from datetime import datetime
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# Токен ВК необходим для связи бота с Вконтакте

VK_token = "vk1.a.mSnOxf521Eb-eUXTnlsopdrL3Q8Yzds_RgMhxdI4ZZNciAS07MqOHjSwz6ZEXSDwbM4Fr1CP7fmdYrRGh83WUScaGIO3fP9O3OKnCEzosRhNmqFuddl1VS0BeHoTxiPjrVDNmviJi_5CtOk1r8XAGQWWEMiVyb8WhWHMKEkLwx7O9DtA1bLRmVFPEtlORbcdOlfgvfU-fWAIv8FQBeY-LA"

database = None
cursor = None
vk_session = None
longpoll = None



# Функция создания таблицы в базе данных

# cursor.execute("CREATE TABLE messages(userid, message, answer, time)")

# Ключ openai - это ключ доступа к нейросети

openai.api_key = "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"

# Engine - используемый для получения ответов движок, всего таких движков около 10

engine = "text-davinci-003"



# Создание списка с сообщениями

messages = []

# Создание списка со временем сообщений

times = []

# Создание списка с ответами на сообщения

answers = []

# Предыдущее сообщение бота

previous_message = ''

# Флаг перевода

translate = False

# Сообщение для перевода

message_to_translate = ''


# Функция получения ответа от нейросети

def gpt_callback(text):
    prompt = text
    completion = openai.Completion.create(engine=engine,
                                          prompt=prompt,
                                          temperature=0.5,
                                          max_tokens=1000)
    return completion.choices[0]['text']



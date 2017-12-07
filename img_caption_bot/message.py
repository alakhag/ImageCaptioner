from telegram.ext import (MessageHandler)
from telegram.ext.filters import (Filters)
import os


def message(bot, update):

    photo_object = update.message.photo[-1]
    print photo_object.file_size
    photo_id = photo_object.file_id
    telegram_file = bot.getFile(photo_id)
    telegram_file.download(custom_path='./screenshot/downloadtemp')
    caption = os.popen('th eval.lua -model ./model/model_id1-501-1448236541.t7_cpu.t7 -image ./screenshot/downloadtemp -gpuid -1').read().strip()
    bot.send_message(chat_id=update.message.chat_id,
                         text=caption)


MESSAGE = MessageHandler(Filters.photo, message)

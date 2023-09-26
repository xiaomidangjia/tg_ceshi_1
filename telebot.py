#鲸鱼异动报警
import time
from pprint import pprint
import pandas as pd
import numpy as np
import datetime,time
# For formatted dictionary printing>>>
from whalealert.whalealert import WhaleAlert
whale=WhaleAlert()# Specify a single transaction from the last 10 minutes>>>
import telegram

bot = telegram.Bot(token='6343206405:AAHkaKIXCMvif0yqkzvTYWasYPEIsTmImgQ')

try:
    await bot.initialize()
    bot.sendMessage(chat_id='-1001975215255', text='测试',message_thread_id=4) #开仓信息同步
    # code
finally:
    await bot.shutdown()


#bot.sendMessage(chat_id='-1001975215255', text='测试',message_thread_id=3) #链上大额转账
#bot.sendMessage(chat_id='-1001975215255', text='测试',message_thread_id=5) #链上数据分享

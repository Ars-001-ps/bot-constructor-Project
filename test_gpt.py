from dotenv import load_dotenv
load_dotenv()
from bots.chat_bot.conditions import response

reply_1 = response('кто ты')
print('ответ 1:', reply_1)

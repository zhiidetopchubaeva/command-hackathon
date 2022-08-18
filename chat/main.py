import asyncio

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import defer_call, info as session_info, run_async, run_js
# import pywebio

# from config.wsgi import application

# import config




chat_msgs = []
online_users = set()

MAX_MESSAGES_COUNT = 100

import requests

async def main():
    global chat_msgs
    
    put_markdown("##  Добро пожаловать в онлайн чат!")

    msg_box = output()
    put_scrollable(msg_box, height=300, keep_bottom=True)
    nickname = await input("Войти в чат", required=True, placeholder="Ваше имя", validate=lambda n: "Такой ник уже используется!" if n in online_users or n == 'asdf' else None)
    online_users.add(nickname)


    chat_msgs.append(( f'`{nickname}` присоединился к чату!'))
    msg_box.append(put_markdown(f'`{nickname}` присоединился к чату'))

    refresh_task = run_async(refresh_msg(nickname, msg_box))

    while True:
        data = await input_group(" Новое сообщение", [
            input(placeholder="Текст сообщения ...", name="msg"),
            actions(name="cmd", buttons=["Отправить", {'label': "Выйти из чата", 'type': 'cancel'}])
        ], validate = lambda m: ('msg', "Введите текст сообщения!") if m["cmd"] == "Отправить" and not m['msg'] else None)

        if data is None:
            break

        msg_box.append(put_markdown(f"`{nickname}`: {data['msg']}"))
        chat_msgs.append((nickname, data['msg']))
        import json
        requests.post('http://127.0.0.1:8000/account/test/', json=json.dumps({'msg': data['msg']}))

    refresh_task.close()

    online_users.remove(nickname)
    toast("Вы вышли из чата!")
    msg_box.append(put_markdown(f' Пользователь `{nickname}` покинул чат!'))
    chat_msgs.append((f'Пользователь `{nickname}` покинул чат!'))

    put_buttons(['Перезайти'], onclick=lambda btn:run_js('window.location.reload()'))

async def refresh_msg(nickname, msg_box):
    global chat_msgs
    last_idx = len(chat_msgs)

    while True:
        await asyncio.sleep(1)
        
        for m in chat_msgs[last_idx:]:
            if m[0] != nickname:  
                msg_box.append(put_markdown(f"`{m[0]}`: {m[1]}"))
        
        if len(chat_msgs) > MAX_MESSAGES_COUNT:
            chat_msgs = chat_msgs[len(chat_msgs) // 2:]
        
        last_idx = len(chat_msgs)


def start_serv():
    start_server(main, debug=True, port=8001, cdn=False, host='127.0.0.1')


if __name__ == "__main__":
    start_serv()
    # start_server(main, debug=True, port=8001, cdn=False, host='127.0.0.1')



# pywebio.platform.django.webio_view(application, cdn = True , session_expire_seconds = None , session_cleanup_interval = None , allow_origins = None , check_origin = None )
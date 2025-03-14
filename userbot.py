from configparser import ConfigParser
from pyrogram.errors import FloodWait
from pyrogram import Client, filters
from time import sleep

config = ConfigParser()
config.read('config.ini')

api_id = config.get('pyrogram' , 'api_id')
api_hash = config.get('pyrogram' , 'api_hash')

app = Client(name='my_account', api_id=api_id, api_hash=api_hash)

text = "I'm busy now, I'll answer when I'm free"


#
# @app.on_message(filters.command("type", prefixes=".") & filters.me)
# def type(_, msg):
#     # Извлекаем текст после команды
#     orig_text = msg.text.split(".type ", maxsplit=1)[1] if len(msg.text.split(".type ", maxsplit=1)) > 1 else ""
#
#     # Проверяем, что текст не пустой
#     if not orig_text:
#         msg.reply("Ошибка: текст сообщения не может быть пустым.")
#         return
#
#     tbp = ""  # to be printed

    # for char in orig_text:
    #     try:
    #         tbp += char  # Добавляем следующий символ к tbp
    #         msg.edit(tbp)  # Редактируем сообщение с текущим текстом
    #         sleep(0.05)  # Задержка между символами
    #
    #     except FloodWait as e:
    #         sleep(e.x)  # Ждем, если превышен лимит
    #     except Exception as e:
    #         print(f"Произошла ошибка: {e}")
    #         break
    #

app = Client(name='my_account', api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type( _, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"

    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)

REPLACEMENT_MAP = {
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",
    "g": "ƃ",
    "h": "ɥ",
    "i": "ᴉ",
    "j": "ɾ",
    "k": "ʞ",
    "l": "l",
    "m": "ɯ",
    "n": "u",
    "o": "o",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "s": "s",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "x": "x",
    "y": "ʎ",
    "z": "z",
    "A": "∀",
    "B": "B",
    "C": "Ɔ",
    "D": "D",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "פ",
    "H": "H",
    "I": "I",
    "J": "ſ",
    "K": "K",
    "L": "˥",
    "M": "W",
    "N": "N",
    "O": "O",
    "P": "Ԁ",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "┴",
    "U": "∩",
    "V": "Λ",
    "W": "M",
    "X": "X",
    "Y": "⅄",
    "Z": "Z",
    "0": "0",
    "1": "Ɩ",
    "2": "ᄅ",
    "3": "Ɛ",
    "4": "ㄣ",
    "5": "ϛ",
    "6": "9",
    "7": "ㄥ",
    "8": "8",
    "9": "6",
    ",": "'",
    ".": "˙",
    "?": "¿",
    "!": "¡",
    '"': ",,",
    "'": ",",
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "<": ">",
    ">": "<",
    "&": "⅋",
    "_": "‾",
}


@app.on_message(filters.command("flip", prefixes=".") & filters.me)
def flip(_, msg):
    text = msg.text.split(".flip", maxsplit=1)[1]
    final_str = ""
    for char in text:
        if char in REPLACEMENT_MAP.keys():
            new_char = REPLACEMENT_MAP[char]
        else:
            new_char = char
        final_str += new_char
    if text != final_str:
        msg.edit(final_str)
    else:
        msg.edit(text)

@app.on_message(filters=filters.dice)
def dice(client, message):
    player_1 = message
    player_2 = app.send_dice(message.chat.id)

    if player_1.dice.value > player_2.dice.value:
        app.send_message(message.chat.id, 'You win :)')
    elif player_1.dice.value < player_2.dice.value:
        app.send_message(message.chat.id, 'You lose :(')
    else:
        app.send_message(message.chat.id, 'draw')

# @app.on_message(filters=filters.private)
# async def auto_answer(event, message):
#     await app.send_message(chat_id=message.chat.id, text=text)

app.run()
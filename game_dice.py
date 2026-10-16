from pyrogram import filters
from userbot import app


@app.on_message(filters.dice)
def dice(client, message):
    if not message.dice:
        return

    player_1 = message.dice.value
    player_2 = app.send_dice(message.chat.id).dice.value

    if player_1 > player_2:
        app.send_message(message.chat.id, 'You win :)')
    elif player_1 < player_2:
        app.send_message(message.chat.id, 'You lose :(')
    else:
        app.send_message(message.chat.id, 'draw')
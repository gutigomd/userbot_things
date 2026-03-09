@app.on_message(filters=filters.dice) #incomplete code!!!
def dice(client, message):
    player_1 = message
    player_2 = app.send_dice(message.chat.id)

   if player_1.dice.value > player_2.dice.value:
       app.send_message(message.chat.id, 'You win :)')
   elif player_1.dice.value < player_2.dice.value:
       app.send_message(message.chat.id, 'You lose :(')
   else:
       app.send_message(message.chat.id, 'draw')
text = "I'm busy now, I'll answer when I'm free" #incoplete code!!!
@app.on_message(filters=filters.private)
async def auto_answer(event, message):
    await app.send_message(chat_id=message.chat.id, text=text)
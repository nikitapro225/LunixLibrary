# created with рофлы лол
import asyncio
from moduless.base import register_command, register_help

async def spam(client, message, commandds:dict, config:dict):
    args = message.text.split(" ", 1)
    if len(args) == 3:
        await client.delete_messages(message.chat.id, [message.id])
        count = int(args[1])
        reply = message.reply_to_message

        if reply:
            if reply.media:
                for i in range(count):
                    await client.send_photo(message.chat.id, reply.photo.file_id)
                    if (i + 1) % 30 == 0:
                        sleep(3)
                return
            else:
                for i in range(count):
                    await client.send_message(message.chat.id, reply.text)
                    if (i + 1) % 30 == 0:
                        sleep(3)
        else:
            text_to_send = " ".join(args[1:])
            for i in range(count):
                await client.send_message(message.chat.id, text_to_send)
                if (i + 1) % 30 == 0:
                    sleep(3)
    else:
        await client.edit_message_text(message.chat.id, message.id, f"{config.prefix}spam (кол-во:int) (сообщение:str)")

register_help("Spam", "Spam", "lunix", {"spam (кол-во:int) (сообщение:str)": "Spams message"})
register_command("spam", spam)

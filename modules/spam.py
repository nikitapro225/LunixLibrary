import asyncio
from moduless.base import register_command, register_help

async def spam(client, message, commandds: dict, config: dict):
    args = message.text.split(" ", 2) 
    if len(args) == 3: 
        await client.delete_messages(message.chat.id, [message.id])
        try:
            count = int(args[1])
        except ValueError:
            await client.edit_message_text(message.chat.id, message.id, f"{config['prefix']}spam (кол-во:int) (сообщение:str)")
            return
        reply = message.reply_to_message

        if reply:
            if reply.media:
                for i in range(count):
                    await client.send_photo(message.chat.id, reply.photo.file_id)
                    await asyncio.sleep(0.1)
                    if (i + 1) % 30 == 0:
                        await asyncio.sleep(3)
                return
            else:
                for i in range(count):
                    await client.send_message(message.chat.id, reply.text)
                    await asyncio.sleep(0.1)
                    if (i + 1) % 30 == 0:
                        await asyncio.sleep(3)
        else:
            text_to_send = " ".join(args[2:])  # Use args[2:] to get the message part
            for i in range(count):
                await client.send_message(message.chat.id, text_to_send)
                await asyncio.sleep(0.1)
                if (i + 1) % 30 == 0:
                    await asyncio.sleep(3)
    else:
        await client.edit_message_text(message.chat.id, message.id, f"{config['prefix']}spam (кол-во:int) (сообщение:str)")

register_help("Spam", "spam", "lunix", {"spam (кол-во:int) (сообщение:str)": "Spams message"})
register_command("spam", spam)

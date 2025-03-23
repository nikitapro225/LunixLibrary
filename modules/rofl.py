# created with рофлы лол
import asyncio
from moduless.base import register_command, register_help


async def koravele(client, message, commandds:dict, config:dict):
    msg = "@Koravele is pidogog"
    for i in range(1, len(msg) + 1):
        new_content = msg[:i]
        try:
            if not new_content[:i].endswith(" "):
                await client.edit_message_text(message.chat.id, message.id, new_content)
        except Exception as e:
            print(f"{e}")
        await asyncio.sleep(0.4) 

async def vzlom(client, message, commandds:dict, config:dict):
    args = message.text.split(" ", 1)
    if len(args) == 2:
        await client.edit_message_text(message.chat.id, message.id, f"👿Взлом жопы @{message.chat.username}!")
        await asyncio.sleep(3)
        for i in range(1, 11):
            progress = "▓" * i + "░" * (10 - i) 
            new_content = f"👿Взлома жопы...\n{progress} {i * 10}%"
            await client.edit_message_text(message.chat.id, message.id, new_content)
            await asyncio.sleep(1)
        await client.edit_message_text(message.chat.id, message.id, "🪄")
        await asyncio.sleep(2)
        await client.edit_message_text(message.chat.id, message.id, "🔮")
        await asyncio.sleep(2)
        await client.edit_message_text(message.chat.id, message.id, f"🔮 @{message.chat.username} {args[1]}")
    else:
        await client.edit_message_text(message.chat.id, message.id, f"ты ебобо? пример: .vzlom <секретный текст>")

async def dox(client, message, commandds:dict, config:dict):
    neww = "Имя: ||блаблаблабла блабла блабл||\nНомер телефона: ||8800555353||\nАдрес: ||Туалет шрека, южная Гвинея||\nМама: ||лаблаблабла блабла лаблабла||\nПапа: ||лаблаблабла блабла ffdsffdf||"
    await client.edit_message_text(message.chat.id, message.id, f"🔮 Doксим...")
    await asyncio.sleep(2)
    await client.edit_message_text(message.chat.id, message.id, neww)

register_help("Rofl LUNIX", "rofl", "lunix", {"dox": "фейк d0кс xD", "vzlom (секретный текст)": "прикольный прикол)", "koravele": "Shhh..."})
register_command("dox", dox)
register_command("vzlom", vzlom)
register_command("koravele", koravele)

import os

from telethon import Button, events

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

NINJA_IMG = os.environ.get(
    "BOT_PING_PIC", "https://te.legra.ph/file/4f23f5ed98a7fb27db710.jpg"
)
ms = 4
ALIVE = Config.ALIVE_NAME

NinjaHacker = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("⚜ NINJABOT ⚜", "https://t.me/officialninjauserbot")]]
    await tgbot.send_file(event.chat_id, NINJA_IMG, caption=NinjaHacker, buttons=GOOD)

import os

from NINJABOT.utils import *
from userbot import *

from . import *

DELETE_TIMEOUT = 5
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "『NINJABOT』"
Ninja = bot.uid
NINJA = f"[{DEFAULTUSER}](tg://user?id={Ninja})"


@bot.on(admin_cmd(pattern=r"sends (?P<shortname>\w+)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"sends (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    thumb = NINJA_logo1
    input_str = event.pattern_match.group(1)
    omk = f"**⍟ 𝙿𝚕𝚞𝚐𝚒𝚗 𝚗𝚊𝚖𝚎 ≈** `{input_str}`\n**⍟ 𝚄𝚙𝚕𝚘𝚊𝚍𝚎𝚍 𝙱𝚢 ≈** {Ninja_mention}\n\n⚜ **[NINJABOT](https://t.me/officialninjauserbot)** ⚜"
    the_plugin_file = "./userbot/plugins/Spam{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        lauda = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            thumb=thumb,
            caption=omk,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        await event.delete()
    else:
        await edit_or_reply(event, "File not found..... Kek")

from telethon import version

from NINJABOT.utils import *
from userbot import *
from userbot.cmdhelp import CmdHelp

# -------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "NINJA"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

Ninja = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={Ninja})"


PM_IMG = "https://telegra.ph/file/4f03f6d4e9521902eb57f.jpg"
pm_caption = "**ninjaẞø✞︎ 𝙸𝚜 𝙾𝚗𝚕𝚒𝚗𝚎**\n\n"

pm_caption += f"**┏🔥✞t͛ẞ̸ ninjaẞø✞︎t🔥┓**\n"
pm_caption += f"**┣🚀 𝙼𝚢 𝙼𝚊𝚜𝚝𝚎𝚛    : {mention}**\n"
pm_caption += f"**┣🚀 𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗 : `{version.__version__}`**\n"
pm_caption += f"**┣🚀 ninjaẞø✞︎ : {NINJAversion}**\n"
pm_caption += f"**┣🚀 𝚂𝚞𝚍𝚘     : `{sudou}`**\n"
pm_caption += f"**┣🚀 𝙾𝚠𝚗𝚎𝚛     : [𝖑𝖊ɠêɳ̃d](https://t.me/The_NinjaHacker)**\n"
pm_caption += f"**┗[♦️𝙶𝚛𝚘𝚞𝚙♦️](https://t.me/officialninjauserbot)┛**\n"

pm_caption += "    [✨яєρο✨](https://github.com/NINJA-OS/NINJABOT) 🔹 [📜License📜](https://github.com/NINJA-OS/NINJABOT/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="bot$"))
@bot.on(sudo_cmd(pattern="bot$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alv").add_command(
    "alive", None, "Check weather the bot is alive or not"
).add_command(
    "bot",
    None,
    "Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg",
).add_warning(
    "Harmless Module"
).add_info(
    "Are u alive?"
).add_type(
    "Official"
).add()

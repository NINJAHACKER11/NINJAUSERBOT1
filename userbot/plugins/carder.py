from faker import Faker
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from NINJABOT import CmdHelp
from NINJABOT import bot as NINJABOT
from NINJABOT.utils import admin_cmd, edit_or_reply, sudo_cmd


@NINJABOT.on(admin_cmd("gencc$"))
@NINJABOT.on(sudo_cmd("gencc$", allow_sudo=True))
async def _(NINJAevent):
    if NINJAevent.fwd_from:
        return
    NINJAcc = Faker()
    NINJAname = NINJAcc.name()
    NINJAadre = NINJAcc.address()
    NINJAcard = NINJAcc.credit_card_full()

    await edit_or_reply(
        NINJAevent,
        f"__**👤 NAME :- **__\n`{NINJAname}`\n\n__**🏡 ADDRESS :- **__\n`{NINJAadre}`\n\n__**💸 CARD :- **__\n`{NINJAcard}`",
    )


@NINJABOT.on(admin_cmd(pattern="bin ?(.*)"))
@NINJABOT.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    NINJA_input = event.pattern_match.group(1)
    chat = "@szbinscheckerbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2143004427)
            )
            await event.client.send_message(chat, f"/bin {NINJA_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @szbinscheckerbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@NINJABOT.on(admin_cmd(pattern="register ?(.*)"))
@NINJABOT.on(sudo_cmd(pattern="register ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    NINJA_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/register {NINJA_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@NINJABOT.on(admin_cmd(pattern="password ?(.*)"))
@NINJABOT.on(sudo_cmd(pattern="password ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    NINJA_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/password {NINJA_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


CmdHelp("carder").add_command("gencc", None, "Generates fake cc...").add_command(
    "register", None, "Register Ur Account Here"
).add_command("password", "<enter>", "Set ur Account Password On CXM.CARDS").add()

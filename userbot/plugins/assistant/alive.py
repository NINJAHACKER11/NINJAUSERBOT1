from telethon import events

from userbot import *

from . import *

PM_IMG = "https://telegra.ph/file/c26fc61e904476083baa7.jpg"
pm_caption = f"⚜『NINJABOT』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{Ninja_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『NINJABOT』~ `{NINJAversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/officialninjabotsupport)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/NINJAHACKER11/NINJAUSERBOT1/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『NINJABOT』 ](https://t.me/officialninjauserbot)\n"
pm_caption += f"┣Assistant ~ By [『NINJAHACKER』 ](https://t.me/officialninjauserbot)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『NINJABOT』](https://t.me/officialninjauserbot) «««"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)

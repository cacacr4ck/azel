import importlib
import time
from datetime import datetime
import asyncio
from pyrogram import idle

from uvloop import install
from ubotlibs import *
from Azazel import BOTLOG_CHATID, aiosession, bot1, bots, app, ids, LOOP, event_loop
from platform import python_version as py
from Azazel.logging import LOGGER
from pyrogram import __version__ as pyro
from Azazel.core.SQL.botlogsql import *
from Azazel.modules import ALL_MODULES
from config import SUPPORT, CHANNEL
import os
from dotenv import load_dotenv



MSG_ON = """
**Zull Project Actived ✅**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
◉ **Versi** : `{}`
◉ **Phython** : `{}`
◉ **Pyrogram** : `{}`
**Ketik** `alive`
**untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    LOGGER("Zull Project").info("Memulai Ubot Pyro..")
    for all_module in ALL_MODULES:
        importlib.import_module("Azazel.modules" + all_module)
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            user_id = ex.id
            await ajg(bot)
            await buat_log(bot)
            botlog_group_id = get_botlog(str(user_id))
            try:
            	await bot.send_message(botlog_group_id, MSG_ON.format(BOT_VER, py, pyro))
            except BaseException as a:
                LOGGER("✓").warning(f"{a}")
            LOGGER("✓").info("Startup Completed")
            LOGGER("✓").info(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("X").info(f"{e}")
    await idle()
    await aiosession.close()
    await app.stop()


              

if __name__ == "__main__":
    LOGGER("Zull Project").info("Starting  Ubot")
    install()
#    LOOP.run_until_complete(main())
    event_loop.run_until_complete(main())

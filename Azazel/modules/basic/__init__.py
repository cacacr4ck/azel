from pyrogram import Client, filters
from Azazel import cmds, app, BOTLOG_CHATID
from Azazel.core import *
from Azazel.logging import LOGGER
from ubotlibs.ubot import Ubot
import os
import sys
from os import environ, execle, path, remove
from Azazel.modules.basic.help import add_command_help
add_command_help = add_command_help

ADMINS = [1086365745, 5569440742 ]

BL_GCAST = [-1002085560648]


BL_UBOT = [-1001812143750]
DEVS = [
  1086365745,
  5569440742,
  ]

def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Azazel"])

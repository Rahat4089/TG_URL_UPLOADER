import random
import os
import time
import psutil
import shutil
import string
import asyncio
from pyrogram import Client, filters
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from plugins.config import Config
from plugins.script import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.database.add import add_user_to_database
from plugins.functions.forcesub import handle_force_subscribe

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update): 
    # Check if the user is the owner
    #start_pics = Config.START_PIC.split(',')
    
        
    if not update.from_user:
        return await update.reply_text("I don't know about you sar :(")
    await add_user_to_database(bot, update)
    await bot.send_message(
        Config.LOG_CHANNEL,
           f"#NEW_USER: \n\nNew User [{update.from_user.first_name}](tg://user?id={update.from_user.id}) started @{Config.BOT_USERNAME} !!"
    )
    start_pics = Config.START_PIC
    
    if Config.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, update)
      if fsub == 400:
        return
    if update.from_user.id not in Config.AUTH_USERS:
        return await update.reply_photo(random.choice(start_pics), caption=Translation.SORRY_TEXT.format(update.from_user.mention), reply_markup=Translation.START_BUTTONS)
    if start_pics:
        await update.reply_photo(random.choice(start_pics), caption=Translation.START_TEXT.format(update.from_user.mention), reply_markup=Translation.START_BUTTONS, message_effect_id=5159385139981059251)       
    else:
        await update.reply_text(text=Translation.START_TEXT.format(update.from_user.mention), reply_markup=Translation.START_BUTTONS, message_effect_id=5159385139981059251, disable_web_page_preview=True)



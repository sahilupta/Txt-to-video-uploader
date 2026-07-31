import os
import re
import sys
import json
import time
from vars import CREDIT
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, PeerIdInvalid, UserIsBlocked, InputUserDeactivated
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Message
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,

# commands button
def register_commands_handlers(bot):
    # .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("cmd_command"))
    async def cmd(client, callback_query):
        user_id = callback_query.from_user.id
        first_name = callback_query.from_user.first_name
        caption = (
            f"🌟  **Welcome** [{first_name}](tg://user?id={user_id})! 🌟\n"
            f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
            f"**🔘 Tap a button for Commands**\n"
            f"<blockquote><b>🕵 Users | 👑 Owner</b></blockquote>\n"
            f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
            f"🚀 Let’s start powerful features!"
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🕵 Users", callback_data="user_command"), InlineKeyboardButton("👑 Owner", callback_data="owner_command")],
            [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back_to_main_menu")]
        ])
        await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://tinypic.host/images/2025/07/14/file_00000000fc2461fbbdd6bc500cecbff8_conversation_id6874702c-9760-800e-b0bf-8e0bcf8a3833message_id964012ce-7ef5-4ad4-88e0-1c41ed240c03-1-1.jpg",
          caption=caption
        ),
        reply_markup=keyboard
        )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("user_command"))
    async def help_button(client, callback_query):
      user_id = callback_query.from_user.id
      first_name = callback_query.from_user.first_name
      keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Commands", callback_data="cmd_command")]])
      caption = (
            f"💥 𝐁𝐎𝐓𝐒 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒\n"
            f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n\n" 
            f"📌 𝗠𝗮𝗶𝗻 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀:\n"  
            f"➥ /start – Bot Status Check\n"
            f"➥ /y2t – YouTube → .txt Converter\n"  
            f"➥ /ytm – YouTube → .mp3 downloader\n"  
            f"➥ /t2t – Text → .txt Generator\n"
            f"➥ /t2h – .txt → .html Converter\n" 
            f"➥ /stop – Cancel Running Task\n"
            f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ \n\n" 
            f"⚙️ 𝗧𝗼𝗼𝗹𝘀 & 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀:\n" 
            f"➥ /cookies – Update YT Cookies\n" 
            f"➥ /id – Get Chat/User ID\n"  
            f"➥ /info – User Details\n"  
            f"➥ /logs – View Bot Activity\n"
            f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n\n"
            f"💡 𝗡𝗼𝘁𝗲:\n"  
            f"• Send any link for auto-extraction\n"
            f"• Send direct .txt file for auto-extraction\n"
            f"• Supports batch processing\n"
            f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n\n"
            f"╭────────⊰◆⊱────────╮\n"   
            f" ➠ 𝐌𝐚𝐝𝐞 𝐁𝐲 : {𝒮𝒶𝒽𝒾𝓁 } 💻\n"
            f"╰────────⊰◆⊱────────╯\n"
      )
    
      await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://tinypic.host/images/2025/07/14/file_00000000fc2461fbbdd6bc500cecbff8_conversation_id6874702c-9760-800e-b0bf-8e0bcf8a3833message_id964012ce-7ef5-4ad4-88e0-1c41ed240c03-1-1.jpg",
          caption=caption
        ),
        reply_markup=keyboard
        )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("owner_command"))
    async def help_button(client, callback_query):
      user_id = callback_query.from_user.id
      first_name = callback_query.from_user.first_name
      keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Commands", callback_data="cmd_command")]])
      caption = (
            f"👤 𝐁𝐨𝐭 𝐎𝐰𝐧𝐞𝐫 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬\n\n" 
            f"➥ /addauth xxxx – Add User ID\n" 
            f"➥ /rmauth xxxx – Remove User ID\n"  
            f"➥ /users – Total User List\n"  
            f"➥ /broadcast – For Broadcasting\n"  
            f"➥ /broadusers – All Broadcasting Users\n"  
            f"➥ /reset – Reset Bot\n"
            f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"  
            f"╭────────⊰◆⊱────────╮\n"   
            f" ➠ 𝐌𝐚𝐝𝐞 𝐁𝐲 : {𝒮𝒶𝒽𝒾𝓁 } 💻\n"
            f"╰────────⊰◆⊱────────╯\n"
      )
    
      await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://tinypic.host/images/2025/07/14/file_00000000fc2461fbbdd6bc500cecbff8_conversation_id6874702c-9760-800e-b0bf-8e0bcf8a3833message_id964012ce-7ef5-4ad4-88e0-1c41ed240c03-1-1.jpg",
          caption=caption
        ),
        reply_markup=keyboard
      )
  

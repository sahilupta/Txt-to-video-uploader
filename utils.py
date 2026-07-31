import random #SAHIL BOTS
import time #SAHIL BOTS
import math #SAHIL BOTS
import os #SAHIL BOTS
from vars import CREDIT #SAHIL BOTS
from pyrogram.errors import FloodWait #SAHIL BOTS
from datetime import datetime,timedelta #SAHIL BOTS

class Timer: #SAHIL BOTS
    def __init__(self, time_between=5): #SAHIL BOTS
        self.start_time = time.time() #SAHIL BOTS
        self.time_between = time_between #SAHIL BOTS

    def can_send(self): #SAHILBOTS
        if time.time() > (self.start_time + self.time_between): #NIKHIL SAINI BOTS
            self.start_time = time.time() #SAHIL BOTS
            return True #SAHIL BOTS
        return False #SAHIL BOTS

#lets do calculations #SAHIL BOTS
def hrb(value, digits= 2, delim= "", postfix=""): #SAHIL BOTS
    """Return a human-readable file size. #SAHIL BOTS
    """ #SAHIL BOTS
    if value is None: #SAHIL BOTS
        return None #SAHIL BOTS
    chosen_unit = "B" #SAHIL BOTS
    for unit in ("KB", "MB", "GB", "TB"): #SAHIL BOTS
       if value > 1000: #SAHIL BOTS
            value /= 1024 #SAHIL BOTS
            chosen_unit = unit #SAHIL BOTS
        else: #SAHIL BOTS
            break #SAHIL BOTS
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix #SAHIL BOTS

def hrt(seconds, precision = 0): #SAHIL BOTS
    """Return a human-readable time delta as a string. #SAHIL BOTS
    """ #SAHIL BOTS
    pieces = [] #SAHIL BOTS
    value = timedelta(seconds=seconds) #SAHIL BOTS

    if value.days: #SAHIL BOTS
        pieces.append(f"{value.days}day") #SAHIL BOTS

    seconds = value.seconds #SAHIL BOTS

    if seconds >= 3600: #SAHIL BOTS
        hours = int(seconds / 3600) #SAHIL BOTS
        pieces.append(f"{hours}hr") #SAHIL BOTS
        seconds -= hours * 3600 #SAHIL BOTS

    if seconds >= 60: #SAHIL BOTS
        minutes = int(seconds / 60) #SAHIL BOTS
        pieces.append(f"{minutes}min") #SAHIL BOTS
        seconds -= minutes * 60 #SAHIL BOTS

    if seconds > 0 or not pieces: #SAHIL BOTS
        pieces.append(f"{seconds}sec") #SAHIL BOTS

    if not precision: #SAHIL BOTS
        return "".join(pieces) #SAHIL BOTS

    return "".join(pieces[:precision]) #SAHIL BOTS

timer = Timer() #SAHIL BOTS

async def progress_bar(current, total, reply, start): #NIKHIL SAINI BOTS
    if timer.can_send(): #NIKHIL SAINI BOTS
        now = time.time() #NIKHIL SAINI BOTS
        diff = now - start #NIKHIL SAINI BOTS
        if diff < 1: #NIKHIL SAINI BOTS
            return #NIKHIL SAINI BOTS
        else: #NIKHIL SAINI BOTS
            perc = f"{current * 100 / total:.1f}%" #SAHIL BOTS
            elapsed_time = round(diff) #SAHILBOTS
            speed = current / elapsed_time #SAHIL BOTS
            remaining_bytes = total - current #SAHIL BOTS
            if speed > 0: #SAHIL BOTS
                eta_seconds = remaining_bytes / speed #NIKHIL SAINI BOTS
                eta = hrt(eta_seconds, precision=1) #SAHIL BOTS
            else: #SAHIL BOTS
                eta = "-" #SAHIL BOTS
            sp = str(hrb(speed)) + "/s" #SAHIL BOTS
            tot = hrb(total) #SAHIL BOTS
            cur = hrb(current) #SAHIL BOTS
            bar_length = 10 #SAHIL BOTS
            completed_length = int(current * bar_length / total) #SAHIL BOTS
            remaining_length = bar_length - completed_length #SAHIL BOTS

            symbol_pairs = [ #SAHIL BOTS
                #("🟢", "⚪"), #SAHIL BOTS
                #("⚫", "⚪"), #SAHIL BOTS
                #("🔵", "⚪"), #SAHIL BOTS
                #("🔴", "⚪"), #SAHIL BOTS
                #("🔘", "⚪"), #SAHIL BOTS
                ("🟩", "⬜") #SAHIL BOTS
            ] #SAHIL BOTS
            chosen_pair = random.choice(symbol_pairs) #SAHIL BOTS
            completed_symbol, remaining_symbol = chosen_pair #SAHIL BOTS

            progress_bar = completed_symbol * completed_length + remaining_symbol * remaining_length #SAHIL BOTS

            try: #SAHIL BOTS
                #await reply.edit(f'`╭──⌯═════𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋𝙎AHIL BOTS 🦋✨═══─╯`') 
                await reply.edit(f'<blockquote>`╭──⌯═════𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐢𝐜𝐬══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋{𝒮𝒶𝒽𝒾𝓁}🦋✨═══─╯`</blockquote>') 
            except FloodWait as e: #SAHIL BOTS
                time.sleep(e.x) #SAHIL BOTS 

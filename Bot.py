#sanmanasullavar errors fix akki tharanam π

import pyrogram
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import User, Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from info import API_ID
from info import API_HASH
from info import BOT_TOKEN
from OMDB import get_movie_info
#=======================================================================

Sam = Client(
    session_name="OMDb-Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

print("Starting Bot..")

#=======================================================================

@Sam.on_message(filters.command('start'))
async def bot_info(bot, message):
    buttons = [
        [
            InlineKeyboardButton('Groupβ»οΈ', url='https://t.me/m_Discussion_Group'),
            InlineKeyboardButton('ChannelπΏ', url='https://t.me/m2feed')
        ]
        ]
    await message.reply(text = """ππ»ββοΈ   Hellooo
    
               
@Sam.on_message(filters.text)
async def imdbcmd(client, message):
    movie_name = message.text
    movie_info = get_movie_info(movie_name)
    if movie_info:
                  poster = movie_info["pimage"]
                  urlid = movie_info['imdb_id']
                  buttons=[[InlineKeyboardButton('π π¨π¬π£π»', url=f"https://www.imdb.com/title/{urlid}")]] 
                                                     
                  text=f""π³ππππΎ : <b>{movie_info['title']}</b>
                            
β±οΈ Runtime : <b>{movie_info['duration']}</b>
π Rating : <b>{movie_info['imdb_rating']}/10</b>
π³οΈ Votes : <b>{movie_info['votes']}</b>

π Release : <b>{movie_info['release']}</b>
π­ Genre : <b>{movie_info['genre']}</b>
π Language : <b>{movie_info['language']}</b>
π Country : <b>{movie_info['country']}</b>

π₯ Directors : <b>{movie_info['director']}</b>
π Writers : <b>{movie_info['writer']}</b>
π Actors : <b>{movie_info['actors']}</b>

π Plot : <code>{movie_info['plot']}</code>"""
                  
                  if poster.startswith("https"):
                                                m = await message.reply_text("π₯πππ½πππ π£πΎππΊπππ..")
                                                await message.reply_photo(photo=poster.replace("_SX300","_"), caption=text, reply_markup=InlineKeyboardMarkup(buttons))
                                                await m.delete()
                  else:
                       m = await message.reply_text("π²ππππ,\nπ¨ π’πΊπ'π π₯πππ½ π―ππππΎππ.\nπ²πΎππ½πππ π ππΊπππΊπ»ππΎ π£πΎππΊπππ..")
                       await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
                       await sleep(4)
                       await m.delete()
    else:
        omdbbuttons=[[InlineKeyboardButton('π π²πΎπΊππΌπ π?π π¦πππππΎ.', url=f'https://google.com/search?q={movie_name.replace(" ","+")}')]]
        await message.reply_text(text="π’ππππ½π'π π₯πΎππΌπ π£πΎππΊπππ\nπ³ππ π³π π’ππΎπΌπ πΈπππ π²ππΎπππππ.", reply_markup=InlineKeyboardMarkup(omdbbuttons))       


#=======================================================================
print("Bot Started!")
#=======================================================================

Sam.run()

#=======================================================================

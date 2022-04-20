from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery
import random 

Alen=Client(
    "Alen Bot",
    bot_token=" ",
    api_id=" ",
    api_hash=" "
)



ALL_PICS = [
 "https://telegra.ph/file/bcc7a52fdaa01a1873a42.jpg",
 "https://telegra.ph/file/8cf46b896b34edcab30fe.jpg",
 "https://telegra.ph/file/32c6266fdfe637fdb2794.jpg"
]

START_MESSAGE = """
**💤💤start അടിച്ചിട്ട് കാര്യം ഇല്ല
{} bro, /more command use ചെയ് എന്നിട്ട്
സ്ഥലം കാലി ആക്ക് എനിക്ക്
ഉറങ്ങേണം...**
"""



MORE_BUTTON = [[
            InlineKeyboardButton("⚠️Don't Click Here⚠️", url="t.me/space4movies"),
            InlineKeyboardButton("⚠️Don't Click Here⚠️", url="t.me/space4movies")
            ],[
            InlineKeyboardButton("CLICK HERE", url="https://t.me/space4cinemas")
            ],[
            InlineKeyboardButton("💢", url="https://t.me/space4cinemas"),
            InlineKeyboardButton("Next", callback_data="start")
            ]]
            
        


@Alen.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PICS),
        caption=START_MESSAGE.format(message.from_user.mention)
    )
        
@Alen.on_message(filters.command("more"))
async def more_message(bot, message):
    await message.reply_text(
        text="/id command use ചെയ്താൽ chat ID കിട്ടുന്നത് ആണ്.ധ്യരീയം ഉണ്ടെങ്കിൽ താഴെ തൊട്ട് നോക്ക്😜",
        reply_markup=InlineKeyboardMarkup(MORE_BUTTON) 
   
    )
    

@Alen.on_message(filters.command("id"))
async def id_message(bot, message):
    text = f"""
**✔️Title     : {message.chat.title}

✔️Username  : @{message.chat.username}

✔️ID        :
{message.chat.id}
**"""

    await message.reply_text(text=text)
   



@Alen.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "start":
        await msg.message.edit(
            text="text"
        )





Alen.run()

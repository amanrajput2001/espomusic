import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/a0f27a6db57911bf3df71.jpg",
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 🎶 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜 𝐎𝐰𝐧𝐞𝐫 = [ 𝐀𝐌𝐀𝐍 𝐑𝐀𝐉𝐏𝐔𝐓 𝐀𝐍𝐃 𝐓𝐒𝐆 𝐌𝐔𝐒𝐈𝐂 ❤️](https://t.me/itzamanrajput)

𝐂𝐫𝐞𝐚𝐭𝐨𝐫 :- [✨ 𝐀𝐌𝐀𝐍  💜](https://t.me/Itzamanarjput)
𝐓𝐒𝐆 𝐆𝐑𝐎𝐔𝐏 :- [✨ 𝐓𝐒𝐆  ❤️🎸](https://t.me/Friends_Chatting_Group3)
𝑻𝒐𝒕𝒂𝒍 𝒑𝒂𝒈𝒂𝒍𝒑𝒂𝒏𝒕𝒊 𝑮𝒓𝒐𝒖𝒑 :- [✨𝐓𝐏𝐆 ❤️](https://t.me/india_chat_00)
𝐒𝐨𝐮𝐫𝐜𝐞  :- [✨  𝗖𝗹𝗶𝗰𝗸 ☑️ 𝗥𝗲𝗽𝗼 🌍](https://te.legra.ph/file/7ca878a87eb74e36254c7.jpg)
𝐂𝐨𝐦𝐦𝐚𝐧𝐝 :- [✨𝗖𝗹𝗶𝗰𝗸 ☑️ 𝗡𝗼𝘄 🚩](https://telegra.ph/%F0%9D%90%80%F0%9D%90%8C%F0%9D%90%80%F0%9D%90%8D-%F0%9D%90%91%F0%9D%90%80%F0%9D%90%89%F0%9D%90%8F%F0%9D%90%94%F0%9D%90%93-%F0%9D%90%8C%F0%9D%90%94%F0%9D%90%92%F0%9D%90%88%F0%9D%90%82-%F0%9D%90%81%F0%9D%90%8E%F0%9D%90%93-%F0%9D%90%82%F0%9D%90%8E%F0%9D%90%8C%F0%9D%90%8C%F0%9D%90%80%F0%9D%90%8D%F0%9D%90%83%F0%9D%90%92-02-25)
𝐓𝐬𝐠 𝐎𝐰𝐧𝐞𝐫 :- [✨ 𝐀𝐁𝐇𝐀𝐘 ❤️🥀](https://t.me/An_innocent_boy)

𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [◧𝐀𝐌𝐀𝐍 👿❤️](https://t.me/itzamanrajput)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 《 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ 》 ➕", url=f"https://t.me/Music_tsgbot?startgroup=true")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/afc66f54a8c2a2002ec3a.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝐂𝐥𝐢𝐜𝐤 ☑️  𝐑𝐞𝐩𝐨 🌍 💞", url=f"https://te.legra.ph/file/7ca878a87eb74e36254c7.jpg")
                ]
            ]
        ),
    )

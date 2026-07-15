import asyncio
from pyrogram import Client, filters

SUDO_USERS = []  # Ye main.py se populate hoga

active_spams = {}

@filters.command("spam", prefixes=".")
async def spam_command(client, message):
    if message.from_user.id not in SUDO_USERS:
        return
    
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.reply("❌ `.spam <count> <message>`")
        return
    
    try:
        count = int(args[1])
        text = args[2]
    except:
        await message.reply("❌ Count number do!")
        return
    
    active_spams[message.chat.id] = True
    sent = 0
    for i in range(count):
        if not active_spams.get(message.chat.id):
            break
        await client.send_message(message.chat.id, text)
        sent += 1
        await asyncio.sleep(0.1)
    
    await message.reply(f"✅ {sent} messages bheje gaye")

@filters.command("stop", prefixes=".")
async def stop_command(client, message):
    if message.from_user.id not in SUDO_USERS:
        return
    active_spams[message.chat.id] = False
    await message.reply("⛔ Spam stopped")

@filters.command("replyraid", prefixes=".")
async def replyraid_command(client, message):
    if message.from_user.id not in SUDO_USERS:
        return
    
    if message.reply_to_message:
        target = message.reply_to_message.from_user.id
    else:
        await message.reply("❌ Reply karo kisi message ko!")
        return
    
    active_spams[target] = True
    await message.reply(f"🎯 ReplyRaid started on {target}")

@filters.command("stopraid", prefixes=".")
async def stopraid_command(client, message):
    if message.from_user.id not in SUDO_USERS:
        return
    active_spams.clear()
    await message.reply("⛔ ReplyRaid stopped")

import asyncio
import os
import importlib
import glob
from pyrogram import Client, filters
from pyrogram.types import Message

# API Config
API_ID = 1234567        # YEH BADALO — apna daalo
API_HASH = "your_api_hash_here"  # YEH BADALO

# Jitne chahe utne sessions yahan add karo
SESSIONS = ["account1", "account2", "account3"]

clients = []
SUDO_USERS = []

async def load_plugins(client):
    plugins = glob.glob("plugins/*.py")
    for path in plugins:
        name = os.path.basename(path)[:-3]
        if name == "__init__":
            continue
        mod = importlib.import_module(f"plugins.{name}")
        if hasattr(mod, "register"):
            mod.register(client)

async def start_bots():
    for session in SESSIONS:
        client = Client(session, api_id=API_ID, api_hash=API_HASH)
        await client.start()
        clients.append(client)
        me = await client.get_me()
        SUDO_USERS.append(me.id)
        await load_plugins(client)
        print(f"✅ {me.first_name} online — ID: {me.id}")
    
    print(f"\n🟢 Total {len(clients)} accounts ready!")
    print("👑 Sudo Users:", SUDO_USERS)
    await asyncio.Event().wait()

async def main():
    await start_bots()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        for c in clients:
            asyncio.get_event_loop().run_until_complete(c.stop())

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
from pyrogram import Client

API_ID = 1234567         # YEH BADALO
API_HASH = "your_api_hash_here"

SESSIONS = ["account1", "account2", "account3"]

async def create_session(name):
    app = Client(name, api_id=API_ID, api_hash=API_HASH)
    await app.start()
    print(f"✅ Session '{name}' ban gaya! Phone: {app.me.phone_number}")
    await app.stop()

async def main():
    for name in SESSIONS:
        await create_session(name)

asyncio.run(main())

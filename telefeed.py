import os, asyncio
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session = os.getenv("SESSION", "telefeed")
dest = int(os.environ["DEST_CHAT_ID"])
source_ids = [int(x) for x in os.getenv("SOURCE_USERNAMES","").split(",") if x]

client = TelegramClient(session, api_id, api_hash)

@client.on(events.NewMessage())
async def handler(event):
    if event.chat_id in source_ids:
        print(f"➡️ {event.chat.title} → {dest}: {event.message.text or '[media]'}")
        await client.forward_messages(dest, event.message)

async def main():
    await client.start()
    print("📡 Userbot running…")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())

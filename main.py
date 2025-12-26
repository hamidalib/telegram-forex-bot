import asyncio

from telethon import TelegramClient
from telethon.network.connection.tcpmtproxy import ConnectionTcpMTProxyAbridged

from config.settings import (
    API_ID,
    API_HASH,
    SESSION_NAME,
    SOURCE_CHANNEL,
    FORWARD_TO,
    PROXY
)

from core.detector import is_forex_signal
from core.forwarder import forward_message

client = TelegramClient(
    SESSION_NAME,
    API_ID,
    API_HASH,
    connection=ConnectionTcpMTProxyAbridged,
    proxy=PROXY
)

last_message_id = None

async def main():
    global last_message_id

    await client.start()
    print("🤖 Signal bot started...")

    channel = await client.get_entity(SOURCE_CHANNEL)

    while True:
        messages = await client.get_messages(channel, limit=1)

        if messages:
            message = messages[0]

            if message.id != last_message_id:
                last_message_id = message.id

                if is_forex_signal(message.text):
                    print("📈 Forex signal detected. Forwarding...")
                    await forward_message(client, message, FORWARD_TO)
                else:
                    print("❌ Not a signal. Ignored.")

        await asyncio.sleep(5)

with client:
    client.loop.run_until_complete(main())

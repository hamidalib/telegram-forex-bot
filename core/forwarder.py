async def forward_message(client, message, target):
    await client.forward_messages(target, message)

from pyrogram import Client, filters
from pyrogram.types import Message

# Delete new member join messages
@app.on_message(filters.new_chat_members)
async def delete_join_message(client: Client, message: Message):
    try:
        await message.delete()
        print(f"Deleted join message in {message.chat.id}")
    except Exception as e:
        print(f"Error deleting join message: {e}")

# Delete left member messages
@app.on_message(filters.left_chat_member)
async def delete_leave_message(client: Client, message: Message):
    try:
        await message.delete()
        print(f"Deleted leave message in {message.chat.id}")
    except Exception as e:
        print(f"Error deleting leave message: {e}")

# Delete video chat (voice chat) start/stop messages
@app.on_message(filters.service)
async def delete_vc_message(client: Client, message: Message):
    try:
        await message.delete()
        print(f"Deleted voice chat message in {message.chat.id}")
    except Exception as e:
        print(f"Error deleting voice chat message: {e}")


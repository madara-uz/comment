# Telegram kanalga post tashlanganda birinchi bo'lib comment yozadigan bot
# Muallif: madara-uz
# GitHub: https://github.com/madara-uz/postcommenter
# 
# Ushbu bot yordamida siz istalgan Telegram kanalga yangi post qo‘yilganda avtomatik tarzda izoh yozishingiz mumkin.
# Foydalanuvchi quyidagilarni kiritadi:
# - API ID va API HASH (https://my.telegram.org orqali olinadi)
# - Sessiya nomi (fayl nomi sifatida)
# - Kuzatiladigan kanallar (masalan: @kanal1, @yangiliklar)
# - Yuboriladigan izoh matni (kommentariy)
#
# Ushbu bot `Telethon` kutubxonasi asosida ishlaydi va Termuxda yoki kompyuterda bemalol ishlaydi.

from telethon import TelegramClient, events
import asyncio

# === Intro terminalga chiqarish ===
def print_intro():
    print("""
==============================
🤖 TELEGRAM AUTO COMMENT BOT
==============================
Muallif: @originalprofil
GitHub: https://github.com/madara-uz/postcommenter
Bu bot yangi post chiqishi bilan avtomatik izoh yozadi.
""")

# === Foydalanuvchidan ma'lumot olish ===
print_intro()
api_id = int(input("API ID: "))
api_hash = input("API HASH: ")
session_name = input("Sessiya nomi (masalan: komentchi): ")
channels = input("Kuzatiladigan kanallar (@kanal1, @kanal2): ").split(',')
comment_text = input("Yoziladigan izoh matni: ").strip()

# === TelegramClient yaratish ===
client = TelegramClient(session_name, api_id, api_hash)

# === Har bir yangi xabarni tekshirish ===
@client.on(events.NewMessage(chats=[ch.strip() for ch in channels]))
async def handler(event):
    if event.is_channel and event.chat and event.message:
        try:
            print(f"✅ Post topildi: {event.chat.title}")
            await asyncio.sleep(3)  # biroz kutish (rate limit uchun)
            await client.send_message(entity=event.chat_id, message=comment_text, comment_to=event.id)
            print(f"💬 Izoh yuborildi: {comment_text}\n")
        except Exception as e:
            print(f"❌ Xatolik yuz berdi: {e}\n")

# === Botni ishga tushirish ===
async def main():
    await client.start()
    print("🤖 Bot ishga tushdi. Postlar kuzatilmoqda...")
    await client.run_until_disconnected()

asyncio.run(main())

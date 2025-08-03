#!/data/data/com.termux/files/usr/bin/bash

# Python va kerakli paketlarni o‘rnatish
pkg update -y
pkg install python -y
pip install --upgrade pip
pip install telethon

echo "✅ O‘rnatish yakunlandi. Endi python comment_autobot.py buyrug‘i bilan ishga tushiring."

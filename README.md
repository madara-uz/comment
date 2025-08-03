# 🤖 Telegram Kanalga Avtomatik Comment Bot

Bu Python dastur yordamida siz belgilagan Telegram kanallarda yangi post chiqishi bilan avtomatik tarzda **birinchi comment** yoziladi.

## 🔧 Xususiyatlar
- Foydalanuvchi kiritgan API ID va HASH orqali ishlaydi
- Bir nechta kanallarni kuzatadi
- Har bir yangi postga birinchi bo‘lib izoh yozadi

---

## 📦 O‘rnatish

### 1. Termux yoki kompyuterda quyidagilarni bajaring:
```bash
pkg update -y
pkg install git -y
pkg install python -y
```

### 2. Kodni yuklab oling:
```bash
git clone https://github.com/madara-uz/postcommenter.git
cd postcommenter
bash install.sh
```

### 3. Ishga tushiring:
```bash
python comment_autobot.py
```

---

## 📝 Ma’lumotlarni kiriting
- API ID: Telegram’dan oling (https://my.telegram.org)
- API HASH: shu joydan beriladi
- Sessiya nomi: o‘zingizga qulay nom
- Kuzatiladigan kanallar: `@kanal1, @kanal2`
- Yoziladigan izoh matni: `Assalomu alaykum!`

---

## 📎 Namuna
```bash
API ID: 1234567
API HASH: abcd1234abcd5678
Sessiya nomi: komentchi
Kuzatiladigan kanallar: @test_kanal, @yangiliklar
Izoh matni: Assalomu alaykum!
```

---

## ℹ️ Kontakt
Telegram: [@your_username](https://t.me/your_username)

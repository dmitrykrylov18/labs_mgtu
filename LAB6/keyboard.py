from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton


def menu():
    download_button_tiktok = KeyboardButton('📕 TikTok')
    download_button_youtube = KeyboardButton('📗 YouTube')
    download_button_instagram = KeyboardButton('📘 Instagram')
    menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    menu_kb.add(download_button_tiktok, download_button_youtube)
    menu_kb.add(download_button_instagram)
    return menu_kb


def menu_admin():
    download_button_tiktok = KeyboardButton('📕 TikTok')
    download_button_youtube = KeyboardButton('📗 YouTube')
    download_button_instagram = KeyboardButton('📘 Instagram')
    info = KeyboardButton('🤖 Info')
    ban = KeyboardButton('🤖 Ban')
    sender = KeyboardButton('🤖 Sender')
    menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    menu_kb.add(download_button_tiktok, download_button_youtube)
    #menu_kb.add(download_button_youtube)
    menu_kb.add(download_button_instagram)
    menu_kb.add(info)
    menu_kb.add(ban)
    menu_kb.add(sender)
    return menu_kb


def back():
    button_back = KeyboardButton('🚫 Отмена')
    back_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    back_kb.add(button_back)
    return back_kb


def make_keyboards(url):
    inline_kb1 = InlineKeyboardMarkup()
    button = InlineKeyboardButton('▪️Лучшее качество до 720p (со звуком)', callback_data=f'best_with_audio|{url}')
    button2 = InlineKeyboardButton('▫️Лучшее качество до 720p (без звука)', callback_data=f'best_video|{url}')
    button3 = InlineKeyboardButton('▪️Чистый звук в лучшем качестве', callback_data=f'best_audio|{url}')
    button4 = InlineKeyboardButton('🚫 Отмена', callback_data=f'cancel')
    inline_kb1.add(button)
    inline_kb1.add(button2)
    inline_kb1.add(button3)
    inline_kb1.add(button4)
    return inline_kb1
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup ,  ReplyKeyboardMarkup



async def choose_lang_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton("pastlives", callback_data=""),
        InlineKeyboardButton("ivan kupala", callback_data=""),
        InlineKeyboardButton("2pac-all eyes on me", callback_data=""),
    )
    return btn



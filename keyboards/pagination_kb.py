from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON, LEXICON_TASKS

# Функция, генерирующая клавиатуру для страницы книги
def create_pagination_keyboard(*buttons: str, chapter: int=0) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    kb_builder.row(*[InlineKeyboardButton(
                    text=LEXICON[button] if button in LEXICON else button,
                    callback_data=button) for button in buttons], width = 3)
    kb_builder.row(*[InlineKeyboardButton(
                    text=LEXICON_TASKS[chapter][button],
                    callback_data=button) for button in LEXICON_TASKS.get(chapter, [])], width = 1)
    kb_builder.row(InlineKeyboardButton(
                    text=LEXICON['main_return'],
                    callback_data='main_return'), width = 1)
    kb_builder.row(InlineKeyboardButton(
                    text=LEXICON['audio'],
                    callback_data='audio'))
    other_bot = 'txt716bot'
    url_button : InlineKeyboardButton = InlineKeyboardButton(
        text = LEXICON['test'], url=f'http://t.me/{other_bot}')


    kb_builder.add(url_button)

    return kb_builder.as_markup()

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from image_service import ImageService


class Handlers:
    def __init__(self):
        self.image_service = ImageService()

    def start_command(self, update, context):
        keyboard = [[
            InlineKeyboardButton("🐶 Dog", callback_data="dog"),
            InlineKeyboardButton("🐱 Cat", callback_data="cat"),
            InlineKeyboardButton("🦊 Fox", callback_data="fox"),
        ]]

        update.message.reply_text(
            "Tanlang:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    def button_handler(self, update, context):
        query = update.callback_query
        query.answer()

        image_type = query.data
        url = self.image_service.fetch_random_image(image_type)

        query.message.reply_photo(photo=url)

    def dog_command(self, update, context):
        url = self.image_service.fetch_random_image("dog")
        update.message.reply_photo(photo=url)

    def cat_command(self, update, context):
        url = self.image_service.fetch_random_image("cat")
        update.message.reply_photo(photo=url)

    def fox_command(self, update, context):
        url = self.image_service.fetch_random_image("fox")
        update.message.reply_photo(photo=url)

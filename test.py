from telegram.ext import Updater, MessageHandler, Filters


def forward_message(update, context):
    context.bot.forward_message(
        chat_id='DESTINATION_CHAT_ID',  # ID чата, куда будет отправлено пересылаемое сообщение
        from_chat_id=update.message.chat_id,  # ID чата, из которого получено сообщение
        message_id=update.message.message_id  # ID пересылаемого сообщения
    )


updater = Updater('BOT_TOKEN')
updater.dispatcher.add_handler(MessageHandler(Filters.text, forward_message))
updater.start_polling()
updater.idle()
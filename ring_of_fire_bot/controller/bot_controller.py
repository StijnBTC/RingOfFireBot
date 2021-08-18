from telegram import Update
from telegram.ext import ConversationHandler, CommandHandler, CallbackContext, CallbackQueryHandler, Updater

from ring_of_fire_bot.controller.poll_controller import PollController
from ring_of_fire_bot.view.message_sender import MessageSender
from ring_of_fire_bot.view.welcome_view import WelcomeView


class BotController:
    def __init__(self, updater: Updater, message_sender: MessageSender) -> None:
        self.updater = updater
        self.dispatcher = self.updater.dispatcher

        self.message_sender: MessageSender = message_sender
        self.dispatcher.add_handler(CallbackQueryHandler(self.__process_callbacks))
        self.welcome_view: WelcomeView = WelcomeView(message_sender)
        self.poll_controller = PollController()
        self.__process_handlers()

    def welcome_message(self, update: Update, context: CallbackContext):
        self.welcome_view.send_welcome_message(update.effective_chat.id)

    def __process_callbacks(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()

    def __process_handlers(self):
        conversation_handler = ConversationHandler(entry_points=[
            CommandHandler("start", self.welcome_message),
            CommandHandler("new_ring", self.poll_controller.join_ring),
            CommandHandler("ringleader", self.poll_controller.want_to_be_ring_manager)
        ],
                                                   states={}, fallbacks=[], allow_reentry=True)
        self.dispatcher.add_handler(conversation_handler)

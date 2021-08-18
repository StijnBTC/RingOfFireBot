from telegram import Update
from telegram.ext import CallbackContext


class PollController:
    def __init__(self):
        pass

    def join_ring(self, update: Update, context: CallbackContext):
        answers = ["Yes", "No"]
        info = update.message.text.split(' ', 1)
        if len(info) < 2:
            context.bot.send_message(
                update.effective_chat.id,
                "Add ring info!"
            )
            return
        ring_size = info[1]
        message = context.bot.send_poll(
            update.effective_chat.id,
            f"Do you want to join the {ring_size}",
            answers,
            is_anonymous=False
        )

    def want_to_be_ring_manager(self, update: Update, context: CallbackContext):
        answers = ["Yes", "No", "If nobody else wants to be ringleader"]
        message = context.bot.send_poll(
            update.effective_chat.id,
            "Can you take up the RingLeader role?",
            answers,
            is_anonymous=False
        )

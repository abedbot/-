import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = os.environ.get("TELEGRAM_TOKEN")
latest_message = ""

def start(update, context):
    update.message.reply_text("أهلا بيك! ابعتلي المحاضرة نص، وأنا هطلعلك منها أسئلة.")

def handle_message(update, context):
    global latest_message
    latest_message = update.message.text
    update.message.reply_text("✅ استلمت المحاضرة! ابعت /quiz علشان أطلعلك منها أسئلة.")

def quiz(update, context):
    global latest_message
    if latest_message:
        question = "ما لون السماء؟\nأ) أحمر\nب) أزرق\nج) أخضر\nد) أصفر\n*الإجابة: ب"
        update.message.reply_text(question)
    else:
        update.message.reply_text("❌ مفيش محاضرة عندي! ابعتها الأول.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("quiz", quiz))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    print("✅ البوت بيشتغل ومستني أوامر...")
    updater.idle()

if __name__ == '__main__':
    main()

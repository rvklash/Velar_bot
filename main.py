
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7899349810:AAGJDV3ulWW2ic_0KrTNx1jdxc4ZNsm1fM4"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Сәлеметсіз бе! Менің атым Шалкар, VelAr құрылыс компаниясынан. Қандай сұрағыңыз бар?")

async def azattyq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Azattyq Avenue: 1-комн от 40 млн тг. Рассрочка 50/50, ипотека от Altyn Bank. Сдача: 3 кв. 2026")

async def ipoteka(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Ипотека от Altyn Bank: первоначалка от 20% до 60%. Залог обязателен, но не обязательно на ваше имя.")

async def kommerciya(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Коммерция: Azattyq Avenue от 80 кв.м по 500–600 тыс/кв.м. В Dostyk 1 — три помещения: 2 по 100 кв.м и 1 на 85 кв.м, от 400 тыс/кв.м, черновая.")

async def srok(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Рассрочка до конца стройки. Сдача Azattyq Avenue — 3 квартал 2026 года.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("азаттык", azattyq))
    app.add_handler(CommandHandler("ипотека", ipoteka))
    app.add_handler(CommandHandler("коммерция", kommerciya))
    app.add_handler(CommandHandler("срок", srok))
    app.run_polling()

if __name__ == "__main__":
    main()

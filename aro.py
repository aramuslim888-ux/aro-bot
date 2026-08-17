import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import yt_dlp

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text and text.startswith("http"):
        await update.message.reply_text("⏳ بەڕێزم، خەریکی داگرتنم...")
        file_name = f"video_{update.message.message_id}.mp4"
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': file_name,
                'quiet': True,
                'extractor-args': {'tiktok': {'web_app': True}}
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([text])
            
            await update.message.reply_video(video=open(file_name, 'rb'))
            if os.path.exists(file_name):
                os.remove(file_name)
        except Exception as e:
            await update.message.reply_text(f"هەڵە ڕوویدا: {e}")
            if os.path.exists(file_name):
                os.remove(file_name)

def main():
    TOKEN = "8538940780:AAGKrV6L1TtXrRlDLkkKEkkVtyE2P5CmGaU"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), download_video))
    print("بۆتەی ئارۆ هەڵبوو و کار دەکات...")
    app.run_polling()

main()

import os
import asyncio
from bot import DarkMusicBot
from dotenv import load_dotenv
from threading import Thread
from flask import Flask, jsonify

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Dark Music Bot</title>
            <style>
                body {
                    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
                    color: #eee;
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    text-align: center;
                }
                h1 { color: #00d9ff; text-shadow: 0 0 10px rgba(0, 217, 255, 0.5); }
                p { font-size: 1.2em; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎵 Dark Music Bot</h1>
                <p>Bot is running and ready to play!</p>
                <p style="color: #888;">High-quality audio • Advanced effects • Multi-channel support</p>
            </div>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "bot": "Dark Music Bot", "version": "2.0"})

def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

async def main():
    bot = DarkMusicBot()
    token = os.getenv('DISCORD_TOKEN')
    
    if not token:
        print("❌ Error: DISCORD_TOKEN not found in environment variables!")
        print("Please set your Discord bot token in the Secrets tab.")
        print("\n📝 To set up your Discord bot:")
        print("1. Go to the Secrets tab (lock icon) in Replit")
        print("2. Add DISCORD_TOKEN with your bot token")
        print("3. Add LAVALINK_HOST, LAVALINK_PORT, and LAVALINK_PASSWORD")
        print("4. Restart the bot")
        return
    
    try:
        flask_thread = Thread(target=run_flask, daemon=True)
        flask_thread.start()
        print("🌐 Keep-alive server started on port 5000")
        
        await bot.start(token)
    except KeyboardInterrupt:
        print("\n👋 Bot shutting down...")
    except Exception as e:
        print(f"❌ Error starting bot: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🎵 Starting Dark Music Bot...")
    print("━" * 50)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

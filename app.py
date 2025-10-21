import os
import asyncio
import sys
from threading import Thread
from flask import Flask, jsonify

# Add current directory to Python path to find your modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from bot import DarkMusicBot
    from dotenv import load_dotenv
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("📁 Current directory:", os.getcwd())
    print("📁 Files in current directory:")
    for file in os.listdir('.'):
        print(f"  - {file}")
    sys.exit(1)

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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

async def main():
    # Print debug info
    print("📁 Current working directory:", os.getcwd())
    print("📁 Files in directory:")
    for file in os.listdir('.'):
        print(f"  - {file}")
    
    bot = DarkMusicBot()
    token = os.getenv('DISCORD_TOKEN')
    
    if not token:
        print("❌ Error: DISCORD_TOKEN not found in environment variables!")
        print("Please set your Discord bot token in Render environment variables.")
        return
    
    print("✅ Discord token found!")
    print("🔧 Lavalink configuration:")
    print(f"   Host: {os.getenv('LAVALINK_HOST', 'Not set')}")
    print(f"   Port: {os.getenv('LAVALINK_PORT', 'Not set')}")
    
    try:
        flask_thread = Thread(target=run_flask, daemon=True)
        flask_thread.start()
        print(f"🌐 Keep-alive server started on port {os.environ.get('PORT', 5000)}")
        
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
# 🎵 Dark Music Bot

A powerful Discord music bot with high-quality audio playback, advanced effects, and a modern dark-themed interface.

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Status](https://img.shields.io/badge/status-active-success)

## ✨ Features

### 🎵 Music Playback
- **High-Quality Audio**: Powered by Lavalink for crystal-clear sound
- **YouTube Support**: Play any song or playlist from YouTube
- **Smart Search**: Interactive search with song selection
- **Queue Management**: Full control over your music queue
- **Volume Control**: Adjust from 0-200% for maximum flexibility

### 🎨 Modern Interface
- **Dark Theme**: Beautiful cyan-glowing embeds
- **Progress Bars**: Visual track progress indicators
- **Rich Information**: Album art, artist info, duration, and more
- **User-Friendly**: Intuitive commands with helpful feedback

### 🎚️ Audio Effects
Transform your music with professional-grade effects:
- **🌙 Nightcore**: Faster tempo + higher pitch
- **🎧 8D Audio**: Immersive surround sound simulation
- **🔊 Bass Boost**: 5 intensity levels (Low to Maximum)
- **🌊 Vaporwave**: Slowed aesthetic vibes
- **〰️ Tremolo**: Volume oscillation effect
- **⚡ Speed Control**: 0.25x to 3.0x playback speed
- **🎼 Pitch Shift**: Independent pitch adjustment

### ❤️ Favorites System
- Save your favorite songs
- Quick replay with one command
- Add entire favorites list to queue
- Personal library for each user

### 🎮 Advanced Controls
- **Interactive Buttons**: ⏮️ Previous, ⏯️ Play/Pause, ⏹️ Stop, ⏭️ Skip, 🔀 Shuffle, 🔁 Loop, 🔊 Volume
- **Loop Modes**: Track, Queue, or Off (toggle with button)
- **Shuffle**: Randomize queue order (button click)
- **Seek**: Jump to any position in a track
- **Now Playing**: Large album artwork with detailed track info
- **24/7 Operation**: Bot stays in voice channel permanently

## 📋 Commands

### 🎮 Main Command (Recommended)
| Command | Description |
|---------|-------------|
| `/music <song>` | **🎵 Unified music player with GUI controls**<br>Opens a beautiful control panel with buttons for all features<br>Includes large album artwork and interactive buttons |

### Music Playback (Alternative Commands)
| Command | Description |
|---------|-------------|
| `/play <query>` | Play a song or playlist |
| `/search <query>` | Search and select from results |
| `/pause` | Pause current song |
| `/resume` | Resume playback |
| `/skip` | Skip current song |
| `/stop` | Stop and clear queue |
| `/disconnect` | Leave voice channel |

### Queue Management
| Command | Description |
|---------|-------------|
| `/queue` | View current queue |
| `/nowplaying` | Show current song details |
| `/shuffle` | Shuffle the queue |
| `/loop <mode>` | Set loop mode (track/queue/off) |
| `/seek <seconds>` | Jump to position |
| `/volume <0-200>` | Adjust volume |

### Audio Effects
| Command | Description |
|---------|-------------|
| `/nightcore` | Enable nightcore effect |
| `/8d` | Enable 8D audio (use headphones!) |
| `/bassboost <level>` | Boost bass (1-5) |
| `/vaporwave` | Enable vaporwave effect |
| `/tremolo` | Enable tremolo effect |
| `/speed <multiplier>` | Change playback speed |
| `/pitch <multiplier>` | Change pitch |
| `/cleareffects` | Remove all effects |

### Favorites
| Command | Description |
|---------|-------------|
| `/addfavorite` | Add current song to favorites |
| `/favorites` | View your favorites list |
| `/playfavorite <index>` | Play a favorite song |
| `/playallfavorites` | Add all favorites to queue |
| `/removefavorite <index>` | Remove from favorites |

## 🚀 Setup Guide

### Prerequisites
- Python 3.11+
- Discord Bot Token
- Lavalink Server

### Step 1: Discord Bot Setup
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and name it "Dark Music"
3. Navigate to "Bot" section and click "Add Bot"
4. Copy the bot token
5. Enable these Privileged Gateway Intents:
   - ✅ Message Content Intent
   - ✅ Server Members Intent
6. Go to OAuth2 > URL Generator
   - Select scopes: `bot`, `applications.commands`
   - Select permissions: Read Messages, Send Messages, Embed Links, Connect, Speak
7. Use the generated URL to invite bot to your server

### Step 2: Lavalink Server
You can use a public Lavalink server or host your own.

**Public Lavalink Servers:**
- `lavalink.devz.cloud:443` (Password: `youtube.com/@Dev_Codes`)
- Search for more: "free public lavalink servers"

### Step 3: Configuration
Add these secrets in Replit Secrets tab:

```
DISCORD_TOKEN=your_discord_bot_token_here
LAVALINK_HOST=lavalink_server_host
LAVALINK_PORT=lavalink_server_port
LAVALINK_PASSWORD=lavalink_server_password
```

### Step 4: Run the Bot
The bot will automatically start when you run the Repl. You'll see:
```
✅ Connected to Lavalink successfully!
✅ Bot is ready!
✅ Synced 26 slash command(s)
```

## 🎯 Usage Examples

### Playing Music (Recommended - GUI Method)
```
/music lofi hip hop          # Opens player with buttons and album art
/music never gonna give you up
/music https://youtube.com/watch?v=...
```
Then use the interactive buttons that appear:
- ⏮️ Previous | ⏯️ Play/Pause | ⏹️ Stop | ⏭️ Skip
- 🔀 Shuffle | 🔁 Loop | 🔊 Vol+ | 🔉 Vol-

### Alternative (Classic Commands)
```
/play never gonna give you up
/search lofi hip hop beats
/volume 150
/loop track
```

### Applying Effects
```
/nightcore
/bassboost High
/8d
/cleareffects
```

### Managing Favorites
```
/addfavorite
/favorites
/playfavorite 1
```

## 📁 Project Structure
```
dark-music-bot/
├── app.py              # Main entry point
├── bot.py              # Discord bot class
├── cogs/
│   ├── music.py        # Music playback commands
│   ├── effects.py      # Audio effects
│   └── favorites.py    # Favorites system
├── data/
│   └── favorites.json  # User favorites storage
└── README.md
```

## 🎨 Color Scheme
The bot uses a dark theme with cyan accents:
- Primary: `#00d9ff` (Cyan)
- Success: `#6bcf7f` (Green)
- Warning: `#ffd93d` (Yellow)
- Error: `#ff6b6b` (Red)
- Special: `#c77dff` (Purple)

## 🔧 Technical Details

### Built With
- **discord.py**: Discord API wrapper
- **wavelink**: Lavalink client for Python
- **Flask**: Keep-alive web server
- **Python 3.11**: Core programming language

### Audio Processing
- Lavalink handles all audio processing
- Supports multiple audio effects simultaneously
- High-quality streaming with minimal latency

### Data Storage
- Favorites stored in JSON format
- Per-user favorite tracking
- Persistent across bot restarts

## 🐛 Troubleshooting

### Bot Not Responding
- Check if bot is online in Discord
- Verify bot has proper permissions
- Ensure Lavalink server is accessible

### Music Not Playing
- Confirm Lavalink connection in logs
- Check voice channel permissions
- Verify you're in a voice channel

### Commands Not Showing
- Wait a few minutes for slash commands to sync
- Try kicking and re-inviting the bot
- Check bot has `applications.commands` scope

## 📝 License
This project is open source and available for personal use.

## 🤝 Support
For issues or questions, check the Replit console logs or Discord bot status.

---

**Made with ❤️ using Python and Discord.py**

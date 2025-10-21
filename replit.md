# Dark Music Bot

## Overview
Dark Music is an advanced Discord music bot built with Python, featuring high-quality audio playback through Lavalink, modern dark-themed embeds, and extensive audio effects capabilities.

## Features
- 🎵 **High-Quality Music Playback**: Powered by Lavalink for superior audio quality
- 🎨 **Modern Dark-Themed UI**: Beautiful cyan-glowing embeds with progress bars
- 🎚️ **Advanced Audio Effects**:
  - Nightcore (speed + pitch increase)
  - 8D Audio (surround sound simulation)
  - Bass Boost (5 levels)
  - Vaporwave (slowed aesthetic)
  - Tremolo, Speed, and Pitch control
- ❤️ **Favorites System**: Save and quickly replay your favorite songs
- 📋 **Queue Management**: Full control over playback queue
- 🔁 **Loop Modes**: Track loop, queue loop, or disabled
- 🔀 **Shuffle**: Randomize queue order
- 🔊 **Volume Control**: 0-200% volume range

## Project Structure
```
├── app.py                 # Main entry point (Flask + Discord bot)
├── bot.py                 # Discord bot class with Dark Music branding
├── cogs/
│   ├── music.py          # Music playback commands
│   ├── effects.py        # Audio effects (nightcore, 8D, bassboost, etc.)
│   └── favorites.py      # Favorites system
├── data/
│   └── favorites.json    # User favorites storage
└── utils/                # Helper utilities
```

## Commands

### Music Playback
- `/play <query>` - Play a song or playlist
- `/search <query>` - Search and choose from results
- `/pause` - Pause current song
- `/resume` - Resume playback
- `/skip` - Skip current song
- `/stop` - Stop and clear queue
- `/disconnect` - Leave voice channel

### Queue Management
- `/queue` - View current queue
- `/nowplaying` - Show current song details
- `/shuffle` - Shuffle the queue
- `/loop <mode>` - Set loop mode (track/queue/off)
- `/seek <seconds>` - Jump to position
- `/volume <0-200>` - Adjust volume

### Audio Effects
- `/nightcore` - Enable nightcore effect
- `/8d` - Enable 8D audio effect
- `/bassboost <level>` - Boost bass (1-5)
- `/vaporwave` - Enable vaporwave effect
- `/tremolo` - Enable tremolo effect
- `/speed <multiplier>` - Change playback speed
- `/pitch <multiplier>` - Change pitch
- `/cleareffects` - Remove all effects

### Favorites
- `/addfavorite` - Add current song to favorites
- `/favorites` - View your favorites list
- `/playfavorite <index>` - Play a favorite song
- `/playallfavorites` - Add all favorites to queue
- `/removefavorite <index>` - Remove from favorites

## Setup Instructions

### 1. Discord Bot Token
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to "Bot" section and create a bot
4. Copy the bot token
5. Add `DISCORD_TOKEN` to Replit Secrets

### 2. Lavalink Server
You need a Lavalink server for audio processing. Options:

**Option A: Use Public Lavalink Server**
- Add these to Secrets:
  - `LAVALINK_HOST`: lavalink server host
  - `LAVALINK_PORT`: server port
  - `LAVALINK_PASSWORD`: server password

**Option B: Host Your Own**
- Run Lavalink in a separate server
- Configure with your server details

### 3. Bot Permissions
Invite the bot with these permissions:
- Read Messages/View Channels
- Send Messages
- Embed Links
- Connect to Voice
- Speak

## Recent Changes
- **2025-10-19 v2.0.1**: GUI player complete with real-time updates
  - **FIXED**: Real-time GUI updates - player panel now updates for ALL events:
    - Button clicks (play/pause, skip, stop, shuffle, loop, volume)
    - Track starts (auto-updates when new song begins)
    - Track ends (auto-updates when queue empties)
    - Idle state (shows "Player Idle" when no music playing)
  - **FIXED**: Idle state handling - proper UI when playback stops
  - **FIXED**: GUI lifecycle - panel stays in sync throughout entire playback cycle
  
- **2025-10-19 v2.0**: Enhanced Dark Music bot with unified GUI player
  - **NEW**: Unified `/music` command with interactive button controls
  - **NEW**: 24/7 operation - bot stays in VC without auto-disconnect
  - **NEW**: Large album artwork display in player panel
  - **NEW**: 8 interactive buttons (⏮️ ⏯️ ⏹️ ⏭️ 🔀 🔁 🔊 🔉)
  - Implemented all core music commands
  - Added 8 audio effects (nightcore, 8D, bassboost, etc.)
  - Implemented favorites system with persistence
  - Dark-themed embeds with cyan accent color (#00d9ff)
  - Fixed app.py entry point for container hosting

## Configuration
All configuration is managed through environment variables (Replit Secrets):
- `DISCORD_TOKEN`: Your Discord bot token
- `LAVALINK_HOST`: Lavalink server hostname
- `LAVALINK_PORT`: Lavalink server port
- `LAVALINK_PASSWORD`: Lavalink server password

## Next Phase Features (Future)
- Multi-bot architecture for simultaneous voice channels
- Unified control panel for managing multiple bot instances
- Advanced lossless audio format support
- Playlist import/export functionality
- Persistent listening history database
- Auto-DJ mode with recommendations

## Notes
- Bot requires Lavalink server to function
- Uses wavelink 3.4.1 for Lavalink integration
- Favorites are stored in `data/favorites.json`
- Keep-alive Flask server runs on port 5000

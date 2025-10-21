import discord
from discord.ext import commands
import wavelink
import os
import asyncio

class DarkMusicBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        intents.voice_states = True
        
        super().__init__(
            command_prefix='!',
            intents=intents,
            help_command=None
        )
        
        self.lavalink_connected = False
        
    async def setup_hook(self):
        await self.load_extension('cogs.music')
        await self.load_extension('cogs.effects')
        await self.load_extension('cogs.favorites')
        await self.load_extension('cogs.player')
        
        lavalink_host = os.getenv('LAVALINK_HOST', 'localhost')
        lavalink_port = int(os.getenv('LAVALINK_PORT', '2333'))
        lavalink_password = os.getenv('LAVALINK_PASSWORD', 'youshallnotpass')
        
        print(f"🔌 Connecting to Lavalink at {lavalink_host}:{lavalink_port}")
        
        try:
            node = wavelink.Node(
                uri=f'http://{lavalink_host}:{lavalink_port}',
                password=lavalink_password
            )
            
            await wavelink.Pool.connect(client=self, nodes=[node])
            self.lavalink_connected = True
            print("✅ Connected to Lavalink successfully!")
        except Exception as e:
            print(f"❌ Failed to connect to Lavalink: {e}")
            print("⚠️  Bot will start but music commands won't work until Lavalink is connected.")
    
    async def on_ready(self):
        print(f"✅ Bot is ready!")
        print(f"📝 Logged in as: {self.user.name} (ID: {self.user.id})")
        print(f"🎵 Dark Music Bot - Version 2.0")
        print(f"🌐 Connected to {len(self.guilds)} server(s)")
        print("━" * 50)
        
        try:
            synced = await self.tree.sync()
            print(f"✅ Synced {len(synced)} slash command(s)")
        except Exception as e:
            print(f"❌ Failed to sync commands: {e}")
        
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name="🎵 /play | Dark Music"
            ),
            status=discord.Status.online
        )
    
    async def on_wavelink_node_ready(self, payload: wavelink.NodeReadyEventPayload):
        print(f"✅ Wavelink Node connected: {payload.node.identifier} | Resumed: {payload.resumed}")
        self.lavalink_connected = True
    
    async def on_wavelink_track_start(self, payload: wavelink.TrackStartEventPayload):
        player = payload.player
        if not player:
            return
        
        track = payload.track
        
        # Skip auto-announcement - player cog will handle UI
        pass
    
    async def on_wavelink_track_end(self, payload: wavelink.TrackEndEventPayload):
        player = payload.player
        if not player:
            return
        
        # Auto-play next track in queue (no disconnect - stay 24/7)
        if not player.queue.is_empty:
            try:
                next_track = await player.queue.get_wait()
                await player.play(next_track)
            except Exception as e:
                print(f"Error playing next track: {e}")
    
    @staticmethod
    def format_time(milliseconds: int) -> str:
        seconds = milliseconds // 1000
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return f"{minutes:02d}:{seconds:02d}"

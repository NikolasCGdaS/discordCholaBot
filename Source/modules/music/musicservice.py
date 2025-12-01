import discord
import yt_dlp
<<<<<<< HEAD
from collections import deque
=======
>>>>>>> a17bb87cd98ccfe0725622ed89470b83f4a4067f

class MusicService:

    def __init__(self):
<<<<<<< HEAD
=======
        # Dicionário para armazenar fila por servidor
>>>>>>> a17bb87cd98ccfe0725622ed89470b83f4a4067f
        self.queues = {}

    async def join_voice(self, ctx):
        if ctx.author.voice is None:
<<<<<<< HEAD
            await ctx.send("❗ Você precisa entrar em um canal de voz.")
=======
            await ctx.send("Você não está em um canal de voz.")
>>>>>>> a17bb87cd98ccfe0725622ed89470b83f4a4067f
            return None

        channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            return await channel.connect()
<<<<<<< HEAD

        return ctx.voice_client

    # =============================
    # 🎵 PLAY (COM BUSCA)
    # =============================
    async def play_music(self, ctx, query):

        guild_id = ctx.guild.id

        # cria fila se não existir
        if guild_id not in self.queues:
            self.queues[guild_id] = deque()

        # transforma TEXTO em busca do YouTube
        query = self.format_query(query)

        # obtém info do áudio
        info = self.get_audio_info(query)

        if info is None:
            await ctx.send("❌ Não consegui encontrar essa música.")
            return

        # adiciona na fila
        self.queues[guild_id].append(info)

        vc = await self.join_voice(ctx)

        # se nada está tocando → tocar imediatamente
        if not vc.is_playing() and not vc.is_paused():
            await self.start_next_in_queue(ctx)
            return

        await ctx.send(f"🎶 **Adicionado à fila:** {info['title']}")

    # =============================
    # 🔍 TRANSFORMA TEXTO EM BUSCA
    # =============================
    def format_query(self, query):
        # se for URL → devolve como está
        if query.startswith("http"):
            return query

        # se for texto → vira busca ytsearch
        return f"ytsearch1:{query}"

    # =============================
    # 📥 PEGA INFO DA MÚSICA
    # =============================
    def get_audio_info(self, query):

        ydl_opts = {
            "format": "bestaudio/best",
            "noplaylist": True,
            "extractor_args": {
                "youtube": {
                    "player_client": ["web_root"]
            }
        },
            "default_search": "ytsearch",
            "quiet": True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                data = ydl.extract_info(query, download=False)

                # quando ytsearch → vem lista "entries"
                if "entries" in data:
                    data = data["entries"][0]

            return {
                "title": data.get("title"),
                "url": data["url"]
            }

        except Exception as e:
            print("Erro YDL:", e)
            return None

    # =============================
    # ▶ TOCAR PRÓXIMA
    # =============================
    async def start_next_in_queue(self, ctx):

        guild_id = ctx.guild.id

        if len(self.queues[guild_id]) == 0:
            await ctx.send("📭 A fila acabou.")
            return

        vc = await self.join_voice(ctx)

        info = self.queues[guild_id].popleft()

        source = await discord.FFmpegOpusAudio.from_probe(
            info["url"], executable="ffmpeg"
        )

        def after_play(err):
            ctx.bot.loop.create_task(self.start_next_in_queue(ctx))

        vc.play(source, after=after_play)

        await ctx.send(f"🎵 Tocando agora: **{info['title']}**")

    # =============================
    # ⏭ SKIP
    # =============================
    async def skip(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("⏭ Pulando música...")
        else:
            await ctx.send("❗ Não há música tocando.")

    # =============================
    # ⏸ / ▶ PAUSE & RESUME
    # =============================
    async def pause(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("⏸ Música pausada.")
=======
        else:
            return ctx.voice_client
        
    #tocar musica

    async def play_music(self, ctx, url):
        vc = await self.join_voice(ctx)
        if vc is None:
            return

        ydl_opts = {
            'format': 'bestaudio',
            'noplaylist': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info['url']

        source = await discord.FFmpegOpusAudio.from_probe(
            audio_url,
            executable="ffmpeg"
        )

        vc.play(source)
        await ctx.send(f"Tocando agora: {info.get('title')}")

    #pausar/despausar musica

    async def pause(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("Música pausada.")
>>>>>>> a17bb87cd98ccfe0725622ed89470b83f4a4067f

    async def resume(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
<<<<<<< HEAD
            await ctx.send("▶ Música retomada.")

    # =============================
    # 🛑 STOP
    # =============================
    async def stop(self, ctx):
        if ctx.voice_client:
            ctx.voice_client.stop()

        self.queues[ctx.guild.id] = deque()

        await ctx.send("🛑 Música parada e fila limpa.")

    # =============================
    # 📜 QUEUE
    # =============================
    async def queue(self, ctx):
        guild_id = ctx.guild.id

        if len(self.queues[guild_id]) == 0:
            await ctx.send("📭 A fila está vazia.")
            return

        queue_text = "\n".join(
            [f"{i+1}. {music['title']}" for i, music in enumerate(self.queues[guild_id])]
        )

        await ctx.send(f"🎼 **Fila atual:**\n{queue_text}")
=======
            await ctx.send("Música retomada.")
            
    #parar musica

    async def stop(self, ctx):
        if ctx.voice_client:
            ctx.voice_client.stop()
            await ctx.send("Música parada.")
>>>>>>> a17bb87cd98ccfe0725622ed89470b83f4a4067f

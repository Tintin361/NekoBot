import discord
from discord.ext import commands
from discord import app_commands
import var
import path

class Basic(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Démarrage de NekoBot")
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=var.online_message))
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if self.bot.user.mentioned_in(message) and message.mention_everyone == False:
            await message.channel.send(f"Hey {message.author.mention}, utilise **/** pour afficher la liste des commandes.")
            
    # Permet de charger un cog
    @commands.command(name="load")
    async def load(self, ctx, extention):
        await ctx.message.delete()
        await self.bot.load_extension(f"cogs.{extention}")
        var.add_module(extention)
        await ctx.send(f"Le module {extention} a bien été chargé")
        
    # Permet de décharger un cog
    @commands.command(name="unload")
    async def unload(self, ctx, extention):
        await ctx.message.delete()
        await self.bot.unload_extension(f"cogs.{extention}")
        var.remove_module(extention)
        await ctx.send(f"Le module {extention} a bien été déchargé")
        
    # Permet de recharger un cog
    @commands.command(name="reload")
    async def reload(self, ctx, extention):
        await ctx.message.delete()
        await self.bot.unload_extension(f"cogs.{extention}")
        await self.bot.load_extension(f"cogs.{extention}")
        await ctx.send(f"Le module {extention} a bien été rechargé")
        
    # Pour synchroniser les commandes slash
    @commands.command(name="sync")
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f"{len(fmt)} commandes ont été synchronisées.")
        
        
    # Affiche une photo du Papa de Proxy
    @app_commands.command(name="proxynekodad", description="Le papa de Proxy, oui oui !")
    async def proxy(self, interaction: discord.Interaction) -> None:
        img = discord.File(f"{path.kiri_path}images/proxydad.png")
        await interaction.response.send_message(content="Proxy's dad be like:", file=img)
        
    # Affiche la version du Bot
    @app_commands.command(name="version", description="Affiche la version du NekoBot.")
    async def ver(self, interaction: discord.Integration) -> None:
        await interaction.response.send_message(content=f"Je suis en en version **{var.version}**.", ephemeral=True)
        
    # Envoie le Lien du Github du Bot
    @app_commands.command(name="github", description="Récupère le lien mon repo Github.")
    async def git(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content=f"Lien du repo: https://github.com/Tintin361/NekoBot", ephemeral=True)
        
    
async def setup(bot):
    await bot.add_cog(Basic(bot))

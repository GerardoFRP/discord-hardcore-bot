import discord
from discord.ext import commands
import os

# Token é lido da variável de ambiente (seguro no Render)
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Dicionário de metas (você pode adicionar mais depois)
metas = {
    "Sobreviver 3 dias": "I",
    "Construir base segura": "I",
    "Conseguir full ferro": "I",
    "Fazer farm de comida": "I",
    "Matar o Dragão do End": "I"
}

def gerar_lista():
    """Gera uma lista de metas com emojis de status."""
    msg = "**📜 Metas Hardcore:**\n\n"
    for nome, status in metas.items():
        icone = "✅" if status == "C" else "❌"
        msg += f"{icone} {nome}\n"
    return msg

@bot.event
async def on_ready():
    print(f"🤖 Bot conectado como {bot.user}")

@bot.command()
async def metas(ctx):
    """Mostra todas as metas."""
    await ctx.send(gerar_lista())

@bot.command()
async def concluir(ctx, *, nome):
    """Marca uma meta como concluída."""
    if nome in metas:
        metas[nome] = "C"
        await ctx.send(f"✅ Meta **{nome}** marcada como concluída!")
    else:
        await ctx.send("❌ Meta não encontrada. Verifique o nome exato.")

@bot.command()
async def resetar(ctx):
    """Reseta todas as metas para incompletas."""
    for nome in metas:
        metas[nome] = "I"
    await ctx.send("🔁 Todas as metas foram resetadas!")

bot.run(TOKEN)

import discord
from discord.ext import commands
import requests
import pyttsx3

# Inicializa o sintetizador de voz
engine = pyttsx3.init()

# Configura o bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

def speak(texto):
    engine.say(texto)
    engine.runAndWait()

def obter_curiosidade():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        return dados["text"]

    else: 
        return None 

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command(name="start")
async def start(ctx):
    await ctx.send(
        f"Olá, {ctx.author.mention}!\n"
        "Eu sou um bot de curiosidades.\n\n"
        "Comandos disponíveis:\n"
        "!start - Exibe esta mensagem\n"
        "!fact - Mostra uma curiosidade"
    )

@bot.command(name="fact")
async def fact(ctx):
    fato = obter_curiosidade()
    if fato:
        await ctx.send(f"Curiosidade:\n\n{fato}")
        speak(fato)
    else:
        await ctx.send("Não foi possível obter uma curiosidade no momento.")

bot.run("Token")

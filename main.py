import requests
import json
import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.model import SlashContext
from IPython import embed

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
slash = SlashCommand(bot)

with open('token.txt', 'r') as f:
    token = f.read().strip()
application_id = 788998991395160133
guild_id = 788995280095150080


def get_headers():
    return {
        'Authorization': f'Bot {token}'
    }


def add_slash_command(name: str, description: str, options=[]):
    url = f'https://discord.com/api/v8/applications/{application_id}/guilds/{guild_id}/commands'

    json = {
        'name': name,
        'description': description,
        'options': options,
    }

    r = requests.post(url, headers=get_headers(), json=json)


def add_slash_commands():
    add_slash_command('hello', 'get a welcoming response', options=[{'name':'hidden', 'description':'Should other people see your welcome message?', 'type': 5, 'required': True}])

def get_slash_commands(guild_id=None):
    url = f'https://discord.com/api/v8/applications/{application_id}/commands'
    if guild_id is not None:
        url = f'https://discord.com/api/v8/applications/{application_id}/guilds/{guild_id}/commands'
    return json.loads(requests.get(url, headers=get_headers()).content)

@slash.slash(name='hello')
async def _test(ctx: SlashContext, should_hide):
    embed = discord.Embed(title='embed test', description=f'hidden: `{should_hide}`')
    await ctx.send(send_type=3, embeds=[embed], hidden=should_hide)

def run():
    bot.run(token)

embed(colors='neutral')

from discord.utils import get
import commands
from bt_utils.console import *
from bt_utils import handleJson
from bt_utils.config import cfg
from dhooks import Webhook, Embed
from others import welcome, role_reaction
from others.message_conditions import check_message
import discord

client = discord.Client()
SHL = Console(prefix="BundestagsBot")
handleJson.BASE_PATH = __file__
cfg.reload()


@client.event
async def on_member_join(member):
    try:
        await member.send(embed=welcome.create_embed())
    except:
        pass  # member did not accept dm
    for role in cfg.options["roles_on_join"]:
        r = get(client.get_guild(531445761733296130).roles, id=int(role))  # TODO: replace guildID
        await member.add_roles(r)


@client.event
async def on_raw_reaction_add(payload):
    await role_reaction.reaction_add(client, payload)


@client.event
async def on_raw_reaction_remove(payload):
    await role_reaction.reaction_remove(client, payload)


@client.event
async def on_message(message):
    if not await check_message(client, message):  # check basic conditions like length and not responding to himself
        return 0

    if message.content.lower().startswith(str(cfg.options["invoke_normal"]).lower()):
        params = commands.parse(message.content, False)
        if params[0].lower() in commands.commands.keys():
            await commands.commands[params[0].lower()](client, message, params[1:])

    elif message.content.lower().startswith(str(cfg.options["invoke_mod"]).lower()):
        params = commands.parse(message.content, True)
        if params[0].lower() in commands.mod_commands.keys():
            await commands.mod_commands[params[0].lower()](client, message, params[1:])


@client.event
async def on_ready():
    # console related
    # ================================================
    SHL.output("Logged in as")
    SHL.output(client.user.name)
    SHL.output(f"Online in {len(client.guilds)} Guilds.")
    SHL.output(f"{red}========================{white}")

    # discord related
    # ================================================
    if cfg.options["use_game"]:
        game = discord.Game(name=cfg.options["game_name"])
        await client.change_presence(activity=game)
        SHL.output(f"{game.name} als Status gesetzt.")

    # WebHooks
    # ================================================
    if cfg.options["use_webhooks"]:
        template = cfg.options["on_ready"]
        embed = Embed(
            title=template["title"],
            description=template["description"],
            thumbnail_url=template["thumbnail_url"],
            color=int(template["color"], 16)
        )
        for name, link in cfg.options["webhooks"].items():
            Webhook(link).send(embed=embed)
            SHL.output(f"Webhook {name} sent.")

client.run(cfg.options["BOT_TOKEN"], reconnect=cfg.options["use_reconnect"])

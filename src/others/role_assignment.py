from discord.utils import get

from bt_utils.config import cfg
from bt_utils.embed_templates import InfoEmbed


async def reaction_add(client, payload):
    if payload.channel_id == cfg.options["channel_ids"]["roles"]:
        if str(payload.emoji.id) in cfg.options["roles"].keys():
            role = get(client.get_guild(payload.guild_id).roles, name=cfg.options["roles"][str(payload.emoji.id)])
            user = client.get_guild(payload.guild_id).get_member(payload.user_id)
            if role not in user.roles:
                await user.add_roles(role)
                try:
                    info_embed = InfoEmbed(title=role.name, description=f"Assigned role {role.name}")
                    await user.send(embed=info_embed)
                except:  # if users privacy settings do not allow dm
                    pass


async def reaction_remove(client, payload):
    if payload.channel_id == cfg.options["channel_ids"]["roles"]:
        if str(payload.emoji.id) in cfg.options["roles"].keys():
            role = get(client.get_guild(payload.guild_id).roles, name=cfg.options["roles"][str(payload.emoji.id)])
            user = client.get_guild(payload.guild_id).get_member(payload.user_id)
            if role in user.roles:
                await user.remove_roles(role)
                try:
                    info_embed = InfoEmbed(title=role.name, description=f"Removed role {role.name}")
                    await user.send(embed=info_embed)
                except:  # if users privacy settings do not allow dm
                    pass

from datetime import datetime

from discord import Embed, Color

from bt_utils.config import cfg
from bt_utils.console import Console, red, white

SHL = Console("WelcomeEmbed")

welcome_de = """
    Unter <#{}> kannst du dir Rollen zuweisen. 
    Beispielsweise Themen, die dich interessieren, oder deine politische Ausrichtung
    
    Oder sag doch einfach in <#{}> hallo :smiley:
    
    In <#{}> kannst du den Bot verwenden.
    Versuche doch mal `>umfrage` um aktuelle Wahlumfragen zu sehen :)
    
    Gerne kannst du mir hier mit `>submit text` ein Feedback oder ein Hinweis hinterlassen, die ich anonym ans Serverteam weiterleite.
    Wenn du Themen öffentlich ansprechen willst,
    kannst du das aber auch gerne in <#{}> tun.
    
    Lies dir bitte alle Regeln und Ankündigungen in <#{}> und <#{}> durch.
    
    
    Beteilige dich gerne an der Entwicklung des BundestagsBot:\n https://github.com/bundestagsBot/bundestagsBot
    """


def create_embed(lang="de"):
    embed = Embed(title=f'Willkommen!', color=Color.green(),
                  url="https://github.com/bundestagsBot/bundestagsBot")
    embed.timestamp = datetime.utcnow()
    try:
        if lang == "de":
            embed.description = welcome_de.format(cfg.options["channel_ids"]["roles"],
                                                  cfg.options["channel_ids"]["welcome"],
                                                  cfg.options["channel_ids"]["bot"][0],
                                                  cfg.options["channel_ids"]["suggestions"],
                                                  cfg.options["channel_ids"]["rules"],
                                                  cfg.options["channel_ids"]["announcement"])
    except KeyError:
        SHL.output(f"{red}Could not send full Embed. Please check if you applied all needed configuration.{white}")
        embed.description = "__**Welcome**__"
    except IndexError:
        SHL.output(f"{red}Could not send full Embed. Please check if you applied all needed configuration.{white}")
        embed.description = "__**Welcome**__"
    return embed

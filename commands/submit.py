from discord.utils import get
import discord
import datetime
from utils import handleJson

settings = {
    'name': 'submit',
    'channels': ['dm'],
    'log': False
}

path = 'C:/server/settings/BoB/submits.json'


async def main(client, message, params):
    id = savejson(message)
    embed = createembed(' '.join(str(message.content).split(' ')[1:]), id)

    channel = get(client.get_guild(531445761733296130).channels, id=545330367150817310)
    await channel.send(embed=embed)
    await message.channel.send(content="Danke für deine Nachricht. Sie wurde ans Team weitergeleitet.\n" +
                                       "Sobald ein Teammitglied antwortet, benachrichtige ich dich.")


def createembed(content, id):
    embed = discord.Embed(title=f'Anfrage #{id} ans Serverteam', color=discord.Color.dark_red())
    embed.timestamp = datetime.datetime.utcnow()
    embed.description = content

    return embed


def savejson(message):

    data = handleJson.readjson(path)
    id = int(data["latestID"]) + 1
    data[id] = {}
    data[id]["author"] = str(message.author)
    data[id]["authorID"] = str(message.author.id)
    data[id]["text"] = ' '.join(str(message.content).split(' ')[1:])
    data[id]["answer"] = ""
    data[id]["answerfrom"] = ""
    data["latestID"] += 1

    handleJson.saveasjson(path, data)
    return id
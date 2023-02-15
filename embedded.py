import discord

# Create a new Discord client
client = discord.Client()


# Send the message
@client.event
async def on_message(message):
    if message.content.startswith('!TEST'):
        # Get the channel you want to send the message to
        channel = client.get_channel(1062121251532984372)
        # await channel.send(embed=embed)
        desc = "List of all the op.gg's of teams"

        # Add fields to the embed
        desc += "\n[Eclipse Fury](https://www.op.gg/multisearch/na?summoners=Transspike%2CMageseeker%2CTheCookieGod%2CHusckarvana%2CAstrotekt%2CNighthunterRook%2CTaengyuyu)"
        desc += "\n[Soyboys](https://www.op.gg/multisearch/na?summoners=Cubstep%2CImabaddkid%2CREELOY+KENJINS%2CD00mcaller%2CFiretoblaze%2CPestilencę)"
        desc += "\n[The Church of Gromp](https://www.op.gg/multisearch/na?summoners=Fallentine,Lotheman,Azen,Kyamya,Fifthbusiness)"
        desc += "\n[Social credit brokers](https://www.op.gg/multisearch/na?summoners=zhong+lu+dui+ju%2CMik%C3%A1%2CNatsukii%2Ci+dont+like+top%2CQu%C3%A8+Sh%C3%AD%2CHanny%C3%A4)"
        desc += "\n[Utah Varsity](https://www.op.gg/multisearch/na?summoners=setije%2CQTshark%2CSentrial%2CFungalpants%2CMeszi)"
        desc += "\n[UvU fanatics](https://www.op.gg/multisearch/na?summoners=T%C3%95T%C3%95R%C3%95%2CN0bleVI%2CCH0PPER%2CHardcorelollipop%2CSentienceee%2CPBDOOM%2CUniaTQ)"
        desc += "\n[Should Have Warded](https://www.op.gg/multisearch/na?summoners=713shade,Elyot,Lan,Colgrim,Kolgrim,UVU%20Scotty,%20Jhed)"
        desc += "\n[Weber State University](https://www.op.gg/multisearch/na?summoners=cendi,%20tibs2,%20zhadox,%20saint%20daniel,%20mother%20gooose)"
        desc += "\n[Utah Red](https://www.op.gg/multisearch/na?summoners=hero+stratos%2Cfundipstik%2Catyu%2Cfaleng%2Cgoatmilkyumyum%2Cnosam4055)"
        desc += "\n[UofU Senior Living Community](https://www.op.gg/multisearch/na?summoners=Rich+homie+jayms%2CReyne%2CDrakar%2CNever+ever+die%2Csoulrush) :older_adult:"
        desc += "\n[BYU eSports](https://www.op.gg/multisearch/na?summoners=heptastrike%2Cthebraddad%2Cpianobruh%2Candeloth%2C+boafpha%2C)"
        desc += "\n[The Gromp Orthodoxy](https://www.op.gg/multisearch/na?summoners=lolDaddyVladdy%2CLightningHolt1%2CMedvede%2CCNG+A+Narwhal%2CMrBlckthrn)"
        embed = discord.Embed(title="OP.GGs", description=desc, color=0x5383e8)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/997532552132829204/1061700415365849159/image.png")

        # Get the channel you want to send the message to
        await channel.send(embed=embed)

# Log in to Discord
client.run('MTAwNzQ4NTcwNTc3MTA0NDkyNA.GwrGNe.y2qw99HFMXflgEpitT668HjzS9Ec2MuuAbz4i8')

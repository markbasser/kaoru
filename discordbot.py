
from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord
from datetime import datetime 

token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID =698653628176531478  #チャンネルID

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    
    if now == '00:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:kaoru:712646431957319770> hello!') 
    
    if now == '00:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:kaoru:712646431957319770> <:cafe:699769671234355230>')  
    
    if now == '01:28':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳<:yeah1:721319707482914877> ')     

    if now == '01:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone <:heart_gal:723894380301123614> これから少し🍬⛈はじまりますよ /n 💜準備はいいですか💜')     

    if now == '02:20':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 60 10 AttenuationDistributed  <:good01:699581068285706301><:JPYNdisco:698471276498649168>⚾Plz receive→/catch')
    
    if now == '02:25':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BGPT 150 15 EquallyDistributed  <:BGPT02:698471366004965406><:good:699580636448423936>⚾Plz receive→/catch')
    
    if now == '03:05':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:heart_gal:723894380301123614> ⚾Plz receive→/catch')
    
    if now == '03:08':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:ty01:721642675274776618> 💦みんな仲良くちゃんと挨拶してよね💛\n Everyone, please speak with your greetings and thanks. \n @here Otherwise I will kick～lol <:heart_gal:723894380301123614> 💛')
    
    if now == '03:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:yeah_gal:723830119919124501> 🎉 ') 
    
    if now == '03:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 0.1 AttenuationDistributed  <:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>Pls receive→/catch')  
    
    if now == '03:39':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BGPT 200 25 EquallyDistributed  <:BGPT02:698471366004965406><:BGPT02:698471366004965406>Pls receive→/catch') 
            
    if now == '03:38':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 100 25 AttenuationDistributed  <:JPYNdisco:698471276498649168><:JPYNdisco:698471276498649168><:JPYNdisco:698471276498649168>Pls receive→/catch')
    
    if now == '03:43':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳')
        
    if now == '03:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BGPT 200 25 EquallyDistributed  <:BGPT02:698471366004965406><:BGPT02:698471366004965406>Pls receive→/catch') 
        
    if now == '05:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('JPXコミュニティ<:jpxdis1:710400520434745425> では、挨拶とお礼はしっかりと相手に伝えましょうね💜 \n Let,s say Hello and Thank you in the JPX <:jpxdis1:710400520434745425> community 💛 ') 
        
    if now == '06:39':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BGPT 100 25 EquallyDistributed  <:BGPT02:698471366004965406><:BGPT02:698471366004965406>Pls receive→/catch') 
        
    if now == '07:39':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BGPT 200 25 EquallyDistributed  <:BGPT02:698471366004965406><:BGPT02:698471366004965406>Pls receive→/catch') 
        
    if now == '07:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/727510173039460382/747662891057938493/attention.png') 

    if now == '07:47':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:goodluck:724101036255608852>')
        
    if now == '08:10':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:aloha:699581550777597992>Hello,how are you❓ ') 
        
    if now == '08:20':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('HELLO ALL💛') 
    
    if now == '10:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:yeah_gal:723830119919124501> <:otsukare:722438703410053160>') 
     
    if now == '10:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BEN 0.1 15 EquallyDistributed  <:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>⚾Plz receive→/catch')
    
    if now == '10:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:goodfriend:731381691192574022> <:otsukare:722438703410053160>') 
        
    if now == '10:56':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('JPXコミュニティ<:jpxdis1:710400520434745425> では、挨拶とお礼はしっかりと伝えましょうね💚<:goodfriend:731381691192574022>  \n Let,s say Hello and Thank you in the JPX <:jpxdis1:710400520434745425> community 💛<:goodfriend:731381691192574022>  ') 

    if now == '12:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('=dance') 
    
    if now == '12:36':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:kaoru:712646431957319770> 🎉 ') 
    
    if now == '12:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:goodfriend:731381691192574022> receive→/catch??')  
    
    if now == '12:50':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BGPT 333 30 EquallyDistributed  <:BGPT02:698471366004965406><:BGPT02:698471366004965406>Pls receive→/catch') 
            
    if now == '12:55':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('Let,s say **Hello** and **Thank you!** in the JPX <:jpxdis1:710400520434745425> community💜\n Pls receive?→/catch \n <:pondering:723818284721635449>')
    
    if now == '13:55':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:ty01:721642675274776618>') 
    
    if now == '14:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳<:goodfriend:731381691192574022>')
        
    if now == '14:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 0.1 AttenuationDistributed  <:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>Pls receive→/catch')  
    
    if now == '14:39':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw BGPT 200 25 EquallyDistributed  <:BGPT02:698471366004965406><:BGPT02:698471366004965406>Pls receive→/catch') 
            
    if now == '14:38':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 100 25 AttenuationDistributed  <:JPYNdisco:698471276498649168><:JPYNdisco:698471276498649168><:JPYNdisco:698471276498649168>Pls receive→/catch')
    
    if now == '14:43':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳')
        
    if now == '14:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/727510173039460382/747662891057938493/attention.png') 
        
    if now == '14:46':
        channel = client.get_channel(741553045481062461)
        await channel.send('@everyone \n https://cdn.discordapp.com/attachments/727510173039460382/747662891057938493/attention.png') 
        
    if now == '15:00':
        channel = client.get_channel(741553045481062461)
        await channel.send('/rain BEN 0.1 AttenuationDistributed  <:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>Pls receive→/catch')  
    
    if now == '15:02':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw BGPT 200 25 EquallyDistributed  <:BGPT02:698471366004965406><:BGPT02:698471366004965406>Pls receive→/catch') 
            
    if now == '15:04':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw JPYN 100 25 AttenuationDistributed  <:JPYNdisco:698471276498649168><:JPYNdisco:698471276498649168><:JPYNdisco:698471276498649168>Pls receive→/catch')
    
    if now == '15:06':
        channel = client.get_channel(741553045481062461)
        await channel.send('<:nicewave:741982210630090763> <:nicewave:741982210630090763> <:nicewave:741982210630090763>')
    
    if now == '16:00':
        channel = client.get_channel(741553045481062461)
        await channel.send('/rain BEN 0.1 AttenuationDistributed  <:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>Pls receive→/catch')  
    
    if now == '16:02':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw BGPT 200 25 EquallyDistributed  <:BGPT02:698471366004965406><:BGPT02:698471366004965406>Pls receive→/catch') 
            
    if now == '16:04':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw JPYN 100 25 AttenuationDistributed  <:JPYNdisco:698471276498649168><:JPYNdisco:698471276498649168><:JPYNdisco:698471276498649168>Pls receive→/catch')
    
    if now == '16:06':
        channel = client.get_channel(741553045481062461)
        await channel.send('<:nicewave:741982210630090763> <:nicewave:741982210630090763> <:nicewave:741982210630090763>')  
        
    if now == '18:43':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pondering:723818284721635449> \n <:kaoru:712646431957319770>JPXコミュニティ<:jpxdis1:710400520434745425> では、挨拶とお礼はしっかりと伝えましょうね💚 \n Let,s say Hello and Thank you in the JPX <:jpxdis1:710400520434745425> community 💛 ') 
   
    if now == '21:56':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:gm:699792760651120671><:yeah_gal:723830119919124501>')

#ループ処理実行
loop.start()

@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

        
    if message.content == "<:otsukare:722438703410053160> <:otsukare:722438703410053160> <:otsukare:722438703410053160>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:otsukare:722438703410053160> <:tyvm:723702293706440765> <:otsukare:722438703410053160>")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "<:nicewave:746273079457611776> <:nicewave:746273079457611776> <:nicewave:746273079457611776>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:nicewave:746273079457611776> <:yeah1:721319707482914877> <:nicewave:746273079457611776>")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "<:yeah1:721319707482914877> <:yeah1:721319707482914877>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:heart_gal:723894380301123614> <:goodfriend:731381691192574022>")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "<:gm:699792760651120671> <:gm:699792760651120671>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:gm:699792760651120671> <:happy:723835203717562418> <:gm:699792760651120671>")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "<:ty01:721642675274776618> <:ty01:721642675274776618> <:ty01:721642675274776618>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:ty:721639183432548394> <:heart_gal2:723825806484308000> <:ty:721639183432548394>")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "<:1000:728799666858360862> <:1000:728799666858360862> <:1000:728799666858360862>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:1000:728799666858360862> <:heart_gal2:723825806484308000> <:amazing:723509952630489110> <:1000:728799666858360862>")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "<:bigmuscle:723842188118589510> <:bigmuscle:723842188118589510> <:bigmuscle:723842188118589510>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"💪 :mechanical_arm: <:yeah1:721319707482914877>")  # f文字列（フォーマット済み文字列リテラル）
    
    elif message.content == "r/link":
        # リアクションアイコンを付けたい
        q = await message.channel.send("/link ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "r/language":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /language EN ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記
              
    elif message.content == "r/accept":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /accept ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記

    elif message.content == "b/benzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info ben ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
        
    elif message.content == "b/jpynzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info jpyn ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記      
        
    elif message.content == "b/bgptzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info bgpt ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
    
    elif message.content == "b/kenjzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info kenj ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
             
    elif message.content == "b/sprtszan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info sprts ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 

    elif message.content == "b/29zan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info 29coin ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 
  
# Botの起動とDiscordサーバーへの接続
client.run(token)

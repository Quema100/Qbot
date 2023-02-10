import random
from discord.ui import Button ,View
import discord
import datetime
import pytz 
from discord.ext import commands
from discord import app_commands


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='', intents=intents)
Token ="Token"




    
@client.event 
async def on_ready():
    print('starting...')
    sus = discord.Streaming(name="퀘마", url="https://www.twitch.tv/quema_100")
    await client.change_presence(status=discord.Status.online, activity= sus)
    try:
        synced= await client.tree.sync()
        print(f"synced {len(synced)} command(s)")
    except Exception as e :
        print(e)
                    
        
      
@client.tree.command(name="랜덤_비번_생성",description="랜덤 비번 생성")
@app_commands.describe(비밀번호_수="비밀번호 수(1 ~ n)")
async def 랜덤_비번_생성(interaction: discord.Interaction, 비밀번호_수:int):
    English= "abcdefghijklmnopqrstuvwxyz"
    big_English= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number= "0123456789"
    user_for= English + big_English + number
    length_for_pass = int(비밀번호_수)
    pass_word= "".join(random.sample(user_for,length_for_pass))
    await interaction.response.send_message(f"생성된 비번은\"{pass_word}\"입니다",ephemeral=True)

    

@client.tree.command(name="암호화",description="암호화 메시지 만들기")
@app_commands.describe(내용="암호화 내용")
async def 암호화(interaction: discord.Interaction,내용:str):
    a= f"{내용}"
    encrypted_text=""
    for c in a:
        x=ord(c)
        x=x+1
        cc=chr(x)
        encrypted_text=encrypted_text+cc
    await interaction.response.send_message(f"암호화된 내용은\"{encrypted_text}\"입니다")
        
@client.tree.command(name="암호해제",description="암호화 메시지 해제")
@app_commands.describe(내용="암호화 해제할 내용")
async def 암호화(interaction: discord.Interaction,내용:str):
    plain_text=""
    for c in f"{내용}":
        x=ord(c)
        x=x-1
        cc=chr(x)
        plain_text=plain_text+cc
    await interaction.response.send_message(f"암호화 해제된 내용은\"{plain_text}\"입니다")
              
        
@client.tree.command(name="공지",description="공지 보내기")
@app_commands.describe(내용="공지 내용")
async def 공지(interaction: discord.Interaction,내용:str):
     channel = client.get_channel(채널 코드)  
     await channel.send("@everyone\n{}".format(내용))
     await interaction.response.send_message(f"\"{내용}\"을 정상적으로 보냈습니다",ephemeral=True)    

            
@client.tree.command(name="서버장",description="서버장 정보")
async def 서버장(interaction: discord.Interaction):
        embed = discord.Embed(title="제목", description="설명", color=0x62c1cc)
        embed.add_field(name="이름", value=용내용", inline=False)
        embed.set_footer(text="명령어가 추가될수도 있습니다.")
        await interaction.response.send_message(embed=embed,ephemeral=True)
        
@client.tree.command(name="투표",description="투표 보내기")
@app_commands.describe(내용="투표 내용")
async def 투표(interaction: discord.Interaction,내용:str):
    channel = client.get_channel(채널 코드)
    channel2 = client.get_channel(채널 코드)
    button=Button(label="찬성",style=discord.ButtonStyle.blurple)
    button2=Button(label="반대",style=discord.ButtonStyle.red)
    
    async def button_callback(interaction):
        await interaction.response.send_message(f"{interaction.user.name}님이 찬성하셨습니다",ephemeral=True)
        await channel2.send(f"{interaction.user.name}님이 찬성하셨습니다")

            

        
    button.callback = button_callback
    async def button_callback2(interaction):
        await interaction.response.send_message(f"{interaction.user.name}님이 반대하셨습니다",ephemeral=True)
        await channel2.send(f"{interaction.user.name}님이 반대하셨습니다")
        
    button2.callback = button_callback2
    view=View()
       
    embed = discord.Embed(title="**투표**", description=f"\n\n{내용}\n\n-----------\n\nBot Made by Quema | 담당 관리자 : {interaction.user}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xB22222)
    view.add_item(button)
    view.add_item(button2)
    await channel.send("<@&982994660303712256>",embed=embed,view=view)
    await interaction.response.send_message(f"{내용}을 보냈습니다",ephemeral=True)

@client.tree.command(name="help",description="명령어 종류")
async def help(interaction: discord.Interaction):
        embed = discord.Embed(title="\"명령어 목록\"", description="**규칙** 읽기는 필수입니다", color=0xE6E6FA)
        embed.add_field(name="명령어", value="> 청소 \n> 규칙", inline=False)
        embed.set_footer(text="그외 명령어는 \"/\"를 사용해서 확인하세요")
        await interaction.response.send_message(embed=embed,ephemeral=True)
    


@client.event
async def on_message(message):       
            
    if message.content.startswith ("규칙"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True: 
           embed = discord.Embed(title="\"환영합니다!\"", description="설명", color=0xB22222)
           embed.add_field(name="이름", value="내용", inline=False)
           embed.set_footer(text="마지막 내용")
           msg =await message.channel.send(embed=embed)
 

 
    
        if i is False:
            await message.channel.send("{}, HEY you aren\'t Admin".format(message.author.mention))    



    if message.content.startswith ("청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[3:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))           
            await message.author.send("```\n디스코드 채팅 {}개가 관리자 {}님의 권한으로 인해 삭제 되었습니다\n```".format(amount, message.author))
            
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, HEY you aren\'t Admin".format(message.author.mention))

         
    
       

client.run(Token)

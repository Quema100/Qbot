# Import module
```python
import random
from discord.ui import Button ,View
import discord
import datetime
import pytz 
from discord.ext import commands
from discord import app_commands
```
# Slash command
```python
@client.tree.command(name="slash_command_name",description="explain briefly")
@app_commands.describe(title="explain briefly")
async def slash_command_name(interaction: discord.Interaction, title:str):
    await interaction.response.send_message(f"{title}",ephemeral=True)
```
```slash_command_name``` 부분에 원하시는 이름

```explain briefly``` 부분에 간단한 설명

```title``` 부분에 원하는 글

## another

봇 코드에 일부 입니다 모듈중에 필요없는 모듈이 있을 수 있습니다.


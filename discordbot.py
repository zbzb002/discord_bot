import discord

# 你的 Discord 机器人的令牌
TOKEN = 'MTI1Njg4MTQzODAyNDc5NDEzMg.GCAF9z.DCJKiqJfVC543Qm6lOIPmqYPUQxDszuM1SorKc'  # 替换为你获取的机器人令牌

# 要监控的频道 ID
CHANNEL_ID = 1240069759563731085

# 要监控的关键字
KEYWORD = '4ga'

# 你的用户 ID
USER_ID = 699738069594800209

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # 忽略机器人自己的消息
        if message.author == self.user:
            return

        # 检查消息是否在指定频道中，并且包含关键字
        if message.channel.id == CHANNEL_ID and KEYWORD in message.content:
            # 发送通知给你（例如通过私信）
            user = await self.fetch_user(USER_ID)
            await user.send(f'通知: 在 {message.channel.name} 频道中找到关键字: {message.content}')

client = MyClient(intents=intents)
client.run(TOKEN)
import discord
from discord.ext import commands
from discord.ui import View, Modal, TextInput
from discord.ui import Select

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

CANAL_PEDIDOS_ID = 1471941914759663729

class CompraModal(discord.ui.Modal, title="Compra de Loomian"):
    nome = discord.ui.TextInput(label="Nome do Loomian", placeholder="Digite o nome do loomian", required=True)
    quantidade = discord.ui.TextInput(label="Quantidade", placeholder="Ex: 1", required=True)

    async def on_submit(self, interaction: discord.Interaction):

        canal = interaction.guild.get_channel(CANAL_PEDIDOS_ID)
        
        if canal:
            embed_pedido = discord.Embed(
            title="📦 PEDIDO",
            color=discord.Color.green()
        )
        embed_pedido.description = (
            f"{interaction.user.mention} pediu:\n"
            f"**Loomian:** {self.nome.value}\n"
            f"**Quantidade:** {self.quantidade.value}"
        )

        await canal.send(embed=embed_pedido)

        file = discord.File(
            r"C:\Users\otavi\OneDrive\Área de Trabalho\bot discord\a\pix.png",
            filename="pix.png"
        )

        embed = discord.Embed(
            title="Pagamento via Pix",
            description=(
                f"**Loomian:** {self.nome.value}\n"
                f"**Quantidade:** {self.quantidade.value}\n\n"
                "Escaneie o QR Code abaixo para pagar."
            ),
            color=discord.Color.green()
        )

        embed.set_image(url="")

        await interaction.response.send_message(
            embed=embed,
            file=file,
            ephemeral=True
        )


class MatchView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Compre seu loomian", style=discord.ButtonStyle.green, custom_id="join_match")
    async def join_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.bot:
            await interaction.response.send_message("Bots não podem entrar.", ephemeral=True)
            return

        await interaction.response.send_modal(CompraModal())


@bot.command()
async def vendal(ctx: commands.Context):
    view = MatchView()
    embed = discord.Embed(
        title="VENDA DE LOOMIANS",
        description="Compre seus loomians aqui\nClique no botão abaixo.",
        color=discord.Color.green()
    )
    embed.set_image(url="https://media.tenor.com/LwfpUq5ZagUAAAAj/spin-it-dancing.gif")
    await ctx.send(embed=embed, view=view)

@bot.command()
async def vendalt(ctx: commands.Context):
    embed = discord.Embed(
        title="Tabela de preços:",
          description=(
        "🟢 Loomian normal (comum) — **1 R$**\n"
        "🟢 Loomian padrão PvP — **1 R$**\n"
        "🟡 Loomian lendário padrão — **3 R$**\n"
        "🟠 Loomian lendário PvP — **5 R$**\n"
        "🔵 Loomian padrão evento — **10 R$**\n"
        "🔴 Loomian evento PvP — **15 R$**"
    ),
        color=discord.Color.dark_purple()
    )

    embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRajvI1_INsAuBD51CKrwTADKzpmTnBXbmieg&s")
    await ctx.send(embed=embed)

bot.run("")

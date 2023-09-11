@client.tree.command(name="purge", description="Removes the given ammount of messages")
@app_commands.checks.has_permissions(manage_messages = True)
@app_commands.describe(amount="How much messages should be purged?")
async def purge_command(interaction: discord.Interaction, amount:int):
    await interaction.response.send_message(f"Purging {amount} message(s)!", ephemeral=True)
    await interaction.channel.purge(limit=amount)
    await interaction.channel.send(f"Successfully purged {amount} messages! ✨", delete_after=3)
@purge_command.error
async def test_error(interaction : discord.Interaction, error):
  if isinstance(error, discord.app_commands.MissingPermissions):
    await interaction.response.send_message(embed=nopermemb)
  else :
    errorembed = discord.Embed(title="There was an error running the command!", description="")
    errorembed.add_field(name="ERROR", value=f"Please contact the developer ``{username}``! \nThe error is:{error}")
    await interaction.response.send_message(embed=errorembed)

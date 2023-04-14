from discord.ext import commands


class CustomHelpCommand(commands.MinimalHelpCommand):
    async def send_error_message(self, error):
        # This method is called if the command raises an error
        # We can customize the error message that is sent here
        # !help send_error_message
        await self.get_destination().send(f'Error: {error}')


    async def send_command_help(self, command):
        # This method is called if a specific command is requested in the help command
        # We can customize the message that is sent here
        message = f'''  Help for command {command}: {command.help}\n  
                        Function for command '''
        await self.get_destination().send(message)
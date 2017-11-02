from .joebot import JoeBot


@JoeBot.handles('testing')
def testing(bot, message, event):
    bot.post_message('No, you\'re testing me.', event['channel'])

@JoeBot.handles('help')
def help(bot, message, event):
    pass

@JoeBot.handles('show')
def show(bot, message, event):
    pass

@JoeBot.handles('echo')
def echo(bot, message, event):
    command = message.split()[0]
    content = message.lstrip(command)
    bot.post_message(content, event['channel'])

@JoeBot.handles('')
def no_retort(bot, message, event):
    pass
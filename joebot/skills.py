from .joebot import JoeBot


@JoeBot.handles('testing')
def testing():
    return 'No, you\'re testing me.'

@JoeBot.handles('help')
def help():
    pass

@JoeBot.handles('show')
def show():
    pass

@JoeBot.handles('')
def no_retort():
    pass
from .joebot import JoeBot


@JoeBot.handles('testing')
def testing():
    return 'No you\'re testing me.'

@JoeBot.handles('')
def no_retort():
    pass
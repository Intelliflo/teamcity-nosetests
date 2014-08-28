import traceback
import operator
from nose.plugins import Plugin


def make_service_message(message_name, **kwargs):
    """Create service message"""
    out = ''
    if kwargs is not None:
        for key, value in iter(sorted(kwargs.items())):
            out += "{0}='{1}' ".format(key, escape_message(str(value)))
        out = out.strip()
    if len(kwargs) > 0:
        out = ' ' + out
    return "##teamcity[{0}{1}]".format(message_name, out)

def escape_message(toescape):
    """Escape message according to team city service message specification"""
    out = ''
    for char in list(toescape):
        codepoint = ord(char)
        if codepoint > 127:
            out += "|0x{0:04x}".format(codepoint)
        elif codepoint == 0x0d:
            out += '|r'
        elif codepoint == 0x0a:
            out += '|n'
        elif char == '|':
            out += "||"
        elif char == '[':
            out += '|['
        elif char == ']':
            out += '|]'
        elif char == "'":
            out += "|'"
        else:
            out += char
    return out


class TeamCityOutput(Plugin):
    """Output test results as team city service messages"""

    name = 'teamcity-output'
    score = 2

    def __init__(self):
        super(TeamCityOutput, self).__init__()

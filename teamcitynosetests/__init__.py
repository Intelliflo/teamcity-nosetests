import traceback
import operator
from nose.plugins import Plugin

def escape_message(toescape):
    out = ''
    for d in list(toescape):
        c = ord(d)
        if c > 127:
            out += "|0x{0:04x}".format(c)
        elif c == 0x0d:
            out += '|r'
        elif c == 0x0a:
            out += '|n'
        elif d == '|':
            out += "||"
        elif d == '[':
            out += '|['
        elif d == ']':
            out += '|]'
        elif d == "'":
            out += "|'"
        else:
            out += d
    return out


class TeamCityOutput(Plugin):
    """Output test results as team city service messages"""

    name = 'teamcity-output'
    score = 2

    def __init__(self):
        super(TeamCityOutput, self).__init__()

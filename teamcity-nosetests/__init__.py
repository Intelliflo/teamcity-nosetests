import traceback
from nose.plugins import Plugin

class TeamCityOutput(Plugin):
    """Output test results as team city service messages"""

    name = 'teamcity-output'
    score = 2

    def __init__(self)
        super(TeamCityOutput, self).__init__()
        
    def _escape(self, toescape):
        pass
        

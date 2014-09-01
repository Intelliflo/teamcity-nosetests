# teamcity-nosetests

Team City nosetests plugin that generates service messages containing test result metadata.

## Requirements

1. Python 3.4 (may work on other versions but is untested)
2. Team city 

## Usage

1. `pip install teamcity-nosetests`
2. From your build steps configuration in TC: `nosetests --with-teamcitynosetests`

## References

http://confluence.jetbrains.com/display/TCD8/Build+Script+Interaction+with+TeamCity


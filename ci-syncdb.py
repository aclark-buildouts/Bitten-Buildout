import commands
import re

south_failure = 'These migrations are in the database but not on disk:'
pattern = re.compile(south_failure)
results = commands.getoutput('bin/django syncdb --migrate')

if not pattern.match(results):
    return True
else:
    return False

import commands
import re

SUCCESS=0
FAILURE=-1

south_failure = 'these migrations are in the database but not on disk'
pattern = re.compile(south_failure)
results = commands.getoutput('bin/django syncdb --migrate')

if not results.match(pattern):
    exit(SUCCESS)
else:
    exit(FAILURE)

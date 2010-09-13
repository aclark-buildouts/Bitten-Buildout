import commands
import re

SUCCESS=0
FAILURE=-1

south_failure = 'these migrations are in the database but not on disk'
generic_traceback = 'Traceback (most recent call last)'

check_for = south_failure, generic_traceback

results = commands.getoutput('bin/django syncdb --migrate')

for error in check_for:
    pattern = re.compile(error)
    if not pattern.match(results):
        print results
        exit(SUCCESS)
    else:
        print results
        exit(FAILURE)

import os
import pep8
import fnmatch
from pprint import pprint

args = '--ignore=E501'

pyfiles = []
results = {}

for path, subdirs, files in os.walk('src/django-project'):
    for file in fnmatch.filter(files, '*.py'):
        pyfiles.append(os.path.join(path, file)) 

for file in pyfiles:
    arglist = [args, file]
    pep8.process_options(arglist)
    pep8.input_file(file)
    results[file] = pep8.get_error_statistics(), pep8.get_warning_statistics()

import os
import pep8
import fnmatch

SUCCESS=0
FAILURE=-1

args = '--ignore=E501'
pyfiles = []
results = {}

line = ('----------------------------------------' +
        '----------------------------------------')

load_max = 4
load_avg = os.getloadavg()[0]
thresh = 0

if load_avg < load_max:
    for path, subdirs, files in os.walk('./src'):
        for file in fnmatch.filter(files, '*.py'):
            pyfiles.append(os.path.join(path, file))
    count = 0
    for file in pyfiles:
        count += 1
        arglist = [args, file]
        pep8.process_options(arglist)
        print '[%d] %s:' % (count, file)
        pep8.input_file(file)
    print line
    print 'Ran PEP8 on %d files' % count
    print line

    if count <= thresh:
        exit(SUCCESS)
    else
        print 'Too many pep8 failures, threshold is set to: %s.' % thresh
        exit(FAILURE)

else:
    print line
    print 'Ran PEP8 on %d files, load average is too high (%f)' % (0, load_avg)
    print line
    exit(FAILURE)

# encode = UTF-8

import sys
import os
import commands

path = sys.path[0].split('/footscript')[0]
print path
# print path.split('/')

# os.system('pip list')
cmd = 'source %s/venv/bin/activate' % path
print cmd
os.system(cmd)

print '------------'

os.system('pip list')

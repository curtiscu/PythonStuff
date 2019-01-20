

#=== pg.8 start ===

'''

Code executed on first load of a module, skipped on
subsequent loads.

Be aware of differences in available modules
between python 2x and 3x

See: https://docs.python.org/3.7/py-modindex.html

'''


# utility function by curtiscu
# nice/ pretty print stuff ...
def pp(tab_count, str):
    print('\t'*tab_count, str)


pp(0,'#=== pg.8 start ===')

import sys
import os
import random
import math

pp(0,'==== SYS ====')
pp(1,'flegs: {0}'.format(sys.flags))
pp(1,'base_prefix: {0}'.format(sys.base_prefix))
#pp(0,'copyright: {0}'.format(sys.copyright))
pp(1,'platform: {0}'.format(sys.platform))
pp(1,'version: {0}'.format(sys.version))
pp(1,'path: {0}'.format(sys.path))
pp(1,'threadinfo: {0}\n'.format(sys.flags))

pp(0,'==== OS ====')
pp(1,'environ: {0}'.format(os.environ))
pp(1,'getcwd: {0}'.format(os.getcwd()))
pp(1,'getpid: {0}'.format(os.getpid()))

pp(0,'\n==== RANDOM ====')
pp(1,'random(): {0}'.format(random.random()))
pp(1,'randint(2, 7): {0}'.format(random.randint(2, 7)))
#pp(1,'getstate(): {0}'.format(random.getstate()))


pp(0,'\n==== MATH ====')
pp(1,'factorial(6): {0}'.format(math.factorial(6)))
pp(1,'pi: {0}'.format(math.pi))
pp(1,'e: {0}'.format(math.e))



pp(0,'\n\n#=== pg.9 start ===')
pp(0,'\n==== PACKAGES ====')

pp(1,'>>>> TODO <<<< sample code on packages ...') # TODO



## Q. 1 (EASY) list, dicts, lotto numbers - TODO
'''
Write script to ...
- Import the platform module. 
- Find out the machine(), node, operating system
- ‘PATH’ plus other related config 
- pretty print/ layout the results.
'''




## Q. 2 (MEDIUM) list, dicts, lotto numbers - TODO
'''
Review API to create a password encryption script.
Time the operation using the 'timeit' function.
'''
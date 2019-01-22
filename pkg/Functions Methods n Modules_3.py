

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


pp(0,'\n==== QUESTIONS ====')
## Q. 1 - TODO
'''
Write script to ...
- Import the platform module. 
- Find out the machine(), node, operating system
- ‘PATH’ plus other related config 
- pretty print/ layout the results.
'''

pp(1,'Q.1 (EASY) platform & PATH stuff..') # TODO

import platform as pl
pp(2,'platform: {0}'.format(pl.machine()))
pp(2,'node: {0}'.format(pl.node()))
pp(2,'platform: {0}'.format(pl.platform()))
pp(2, 'os PATH: {0}'.format(os.environ['PATH']))

## Q. 2 (MEDIUM) - TODO
'''
Review API to create a password encryption script.
Time the operation using the 'timeit' function.
'''

pp(1,'>>>> TODO <<<< Q. 2 (MEDIUM) encryption and timing stuff ...') # TODO

'''
From: https://blog.ruanbekker.com/blog/2018/04/29/encryption-and-decryption-with-simple-crypt-using-python/
$ pip install simple-crypt
'''

from simplecrypt import encrypt, decrypt
passwurd = 'p@ssW0rd'
msg = 'somethingToB3K3ptS3cr3t'

def encMyString(my_string):
    return encrypt(passwurd, my_string)



# encText = encrypt(passwurd, msg)

encText = encMyString(msg)

pp(1, 'My encrypted text is: {0}'.format(encText))

'''
See: https://docs.python.org/3.7/library/timeit.html?highlight=timeit#timeit.Timer.timeit

'''
from timeit import timeit as ti

ti(encText)


#=== pg.8 start ===

'''

On the first instance of loading the module is initialised by
executing the code in the module. If another module in the code
imports the same module it is not loaded a second time. There
are many commonly used modules in python. It is worth noting that
some modules are only available for Python 2.X and others are
available for Python 3.

'''

# utility function by curtiscu
# nice/ pretty print stuff ...
def pp(tab_count, str):
    print('\t'*tab_count, str)


pp(0,'#=== pg.8 start ===')

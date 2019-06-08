#!/usr/bin/env python
# coding: utf-8

# 
# # LEARNING PYTHON STUFF
# 
# Testing some stuff I'm learning from... <br>
#     - https://www.youtube.com/watch?v=cKPlPJyQrt4&t=1016s
#     
# 
#     
# Dunder methods - or "Double Underscore" methods reference the "Python Data Model", dictates how the object should behave in common scenarios, e.g. printing, adding, etc. <br>
#     - https://docs.python.org/3/reference/datamodel.html
#     - https://stackoverflow.com/questions/38418070/what-does-r-do-in-str-and-repr
#    
#     

# ## Key python patterns/ things to know to get started..
# - protocol/ dunder methods to implement behaviour
# - class/ inheritance protocol or hierarchy to find someting in an object
# - key caveats around how Python OO works

# In[ ]:


# x + y -> __add__
# init x -> __init__
# print/ repr(x)  -> __repr__
# len(x) -> __len__


# In[ ]:



# imports and whatnot

# Jupyter config: show value of multiple cell statements at once..
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[ ]:




class Polynomnom:
    def __init__(self, *coeffs):
        self.coeffs = coeffs
        
    # this should show information that allows
    # recreating a new instance with same config
    # from scratch..
    def __repr__(self):
        return "Polynomnom(*{!r})".format(self.coeffs)
    
    def __add__(self, other):
        return Polynomnom(*(x + y for x, y in zip (self.coeffs, other.coeffs)))
    
    def __len__(self):
        return len(self.coeffs)
        


# In[ ]:


p1 = Polynomnom(1,2,3)
p2 = Polynomnom(7,4,3)


# In[ ]:


p1
p2


# In[ ]:


p1 + p2


# In[ ]:


len(p1)


# ## Python metaclasses
# 
# .. leading to the following features..
# - decorators
# - generators
# - context managers

# First, setup assertions in derived class to ensure that the parent/ base class has the required methods we need to function properly, i.e. user-level derived class enforcing constraints on library-level code.

# In[ ]:


class Base:
    def foo(self):
        return 'foo'
    
    def __repr__(self):
        print("hello from base!")
        bloop()
    


# In[ ]:



# typically import code (e.g. 'Derived') from a separate file
# into where it's going to be used, use 'assert' to test
# superclass has what we need for our class 'Dervied'
# to work properly ... 
assert hasattr(Base, 'foo'), "super class is bust!!"

class Dervived(Base):
    def bar(self):
        return self.foo()
    


# In[ ]:


d1 = Dervived()
d1.bar()


# ### Testing dissassembling stuff...
# 

# In[ ]:


def blah():
    class Base2:
        pass
    
from dis import dis # dissassemble some code...

dis(blah)


# ### Hooking into class creation mechanism..

# In[ ]:


old_bc = __build_class__

def my_build_class(fun, name, base=None, **kw):
    if base is Base:
        print("Check that 'bar' method defined!!!")
    
    if base is not None:
        return old_bc(fun, name, base, **kw)
    
    return old_bc(fun, name, **kw)

import builtins
builtins.__build_class__ = my_build_class


# In[ ]:


class Derived2(Base):
    def bar(self):
        print("Hello from Derived2.bar :)")
    
    


# In[ ]:


d2 = Derived2()
d2


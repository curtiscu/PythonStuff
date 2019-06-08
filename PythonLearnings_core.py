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

# In[1]:


# x + y -> __add__
# init x -> __init__
# print/ repr(x)  -> __repr__
# len(x) -> __len__


# In[2]:



# imports and whatnot

# Jupyter config: show value of multiple cell statements at once..
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[3]:




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
        


# In[4]:


p1 = Polynomnom(1,2,3)
p2 = Polynomnom(7,4,3)


# In[5]:


p1
p2


# In[6]:


p1 + p2


# In[7]:


len(p1)


# ## Python metaclasses
# 
# .. leading to the following features..
# - decorators
# - generators
# - context managers

# First, setup assertions in derived class to ensure that the parent/ base class has the required methods we need to function properly, i.e. user-level derived class enforcing constraints on library-level code.

# In[22]:


class Base:
    def foo(self):
        return 'foo'
    
    def __repr__(self):
        return "hello from base!"
        
        
    


# In[23]:



# typically import code (e.g. 'Derived') from a separate file
# into where it's going to be used, use 'assert' to test
# superclass has what we need for our class 'Dervied'
# to work properly ... 
assert hasattr(Base, 'foo'), "super class is bust!!"

class Dervived(Base):
    def bar(self):
        return self.foo()
    


# In[24]:


d1 = Dervived()
d1.bar()


# ### Exploring dissassembling stuff...
# 

# In[11]:


def blah():
    class Base2:
        pass
    
from dis import dis # dissassemble some code...

dis(blah)


# ### Hooking into class creation mechanism..
# This is not a solution you'd typically use, apparently, but exploring it anyways...

# In[12]:


old_bc = __build_class__

def my_build_class(fun, name, base=None, **kw):
    if base is Base:
        print("Check that 'bar' method defined!!!")
    
    if base is not None:
        return old_bc(fun, name, base, **kw)
    
    return old_bc(fun, name, **kw)

import builtins
builtins.__build_class__ = my_build_class


# In[35]:


class Derived2(Base):
    def bar(self):
        print("Hello from Derived2.bar :)")
        
    # example of calling parent class functions
    # that have been overridden in subclass...
    def __repr__(self):
        return super().__repr__() + "; hello from Derived2!"
    


# In[36]:


d2 = Derived2()
d2


# NOTE: d2 -> instanceof -> Dervived2 -> instanceof -> type

# In[39]:


isinstance(d2, Derived2)

isinstance(Derived2, type)


# Return default class builder...
# 

# In[49]:


builtins.__build_class__ = old_bc


# ### Use metaclass to enforce constraints on subclass....
# 

# In[99]:


class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print('BaseMeta.__new__', cls, name, bases, body)
        m = 'bar'
        if not m in body:
            raise TypeError("Bad subclass, missing '{0}' in subclass '{1}' bad user!".format(m, name))
        return super().__new__(cls, name, bases, body)
    
    def __init_subclass__():
        print('BaseMeta.__init_subclass() called ..')
        

class MyBase(metaclass=BaseMeta):
    def foo(self):
        return self.bar()
    
    # required to compile as all subclasses of BaseMeta
    # must have this method implemented, but just using
    # a stub here for now ...
    def bar(self):
        pass
    
    def __init_subclass__(self, *a, **kw):
        print("MyBase.__init_subclass__ called...")
        


# In[100]:


class MyDerivedMeta(MyBase):
    def bar(self):
       return 'bar'


# In[66]:


mdm = MyDerivedMeta()
mdm.bar()


# In[83]:


mdm.


# ## Exploring functions, live...
# 

# In[101]:


def add(x, y=10):
    return x + y


# In[103]:


add(5, 9) 
add(2)


# In[104]:


add


# In[111]:


# show default params..
add.__defaults__

# ask name
add.__name__

# get varianble names
add.__code__.co_varnames

from inspect import getsource, getfile
print(getsource(add))  # get the actual function code...
getfile(add)  # find out file it's defined in...


# ## Decorators

# In[112]:


# TODO ...


# ## Generators
# 
# ::TODO:: ...
# 
# Can be used to  ...
# * do step by step computation and yield result and/ or control after each step
# * force sequencing of code.
# 
# https://wiki.python.org/moin/Generators
# 
# .. TODO finish fleshing this out!
# 

# In[115]:


# very different implementations, hard to see
# difference when using them, give same result

def add1(x, y):
    return x + y

class Adder:
    def __call__(self, x, y):
        return x + y
    
add2 = Adder()
    
    


# In[114]:


add1(2, 7)
add2(2, 7)


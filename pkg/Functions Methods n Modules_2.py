
#=== pg.5 start ===

'''
python is pass by name, not pass by reference/ value
if you change what the variable points to inside a
function, the outside/ external pointer to that object
remains unchanged. if you modify the contents of what's
pointed to, that change is persisted outside the function

see:
https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference
https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/

'''

# utility function by curtiscu
# nice/ pretty print stuff ...
def pp(tab_count, str):
    print('\t'*tab_count, str)


pp(0,'#=== pg.5 start ===')

def changeup_list(sList):
    sList = [100,101,102,103,104,105]
    pp(1,'sList changed in func: {}'.format(sList))

def append_to_list(aList):
    aList.append(666)
    pp(1,'sList appended to in func: {0}'.format(aList))

def main():
    sList = [0, 1, 2, 3, 4, 5]
    pp(0,'sList before changeup: {}'.format(sList))
    changeup_list(sList)
    pp(0,'sList after changeup: {}'.format(sList))
    append_to_list(sList)
    pp(0, 'sList after append: {}'.format(sList))

main()


# === pg.5, Global and Local vars ===
pp(0,'\n# === pg.5, Global and Local vars ===')

def overload_1(n1, n2=25):
    t_total = 0  # local var only
    t_total = n1 + n2
    pp(1,'inside func t_total: {}'.format(t_total))
    return;

t_total = 0  # global scope
overload_1(999,111000)
overload_1(21)
pp(0,'outside t_total func: {}'.format(t_total))

'''

To make a global variable accessible and modifiable
within the local scope requires the use of the 
‘global’ statement.

'''

# === pg.7, Global and Local vars ===
pp(0,'\n# === pg.7, Global and Local vars ===')
def overload_2(n1, n2=21):
    global t_total2
    pp(1, 'OID prior to modification: {}'.format(id(t_total2)))
    t_total2 = n1 + n2
    pp(1,'inside func overload2: {}'.format(t_total2))
    return;

t_total2 = 0
pp(0,'OID outside method, pre-mod: {}'.format(id(t_total2)))
overload_2(999,1111)
overload_2(6666)
pp(0,'OID outside method, post-mod: {}'.format(id(t_total2)))
pp(0,'outside func t_total2: {}'.format(t_total2))
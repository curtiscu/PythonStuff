
#=== pg.5 start ===

'''

 ..if we pass by reference and then change the reference within
 the function then the original reference remains unchanged.
 For example if a list is created and it is assign a new
 reference the old list is unchanged. If the function simply
 updates, or modifies the list then the reference remains the same.

'''

# utility function by curtiscu
# nice/ pretty print stuff ...
def pp(tab_count, str):
    print('\t'*tab_count, str)


pp(0,'#=== pg.5 start ===')

def changeup_list(sList):
    sList = [100,101,102,103,104,105]
    pp(1,'sList changed in func: {}'.format(sList))


def main():
    sList = [0, 1, 2, 3, 4, 5]
    pp(0,'sList before: {}'.format(sList))
    changeup_list(sList)
    pp(0,'sList after: {}'.format(sList))

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
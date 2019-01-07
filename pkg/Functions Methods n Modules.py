'''

Python file for practical "3.3 Functions Methods n Modules.pdf"

'''

# utility function by curtiscu
# nice/ pretty print stuff ...
def pp(tab_count, str):
    print('\t'*tab_count, str)



# when the file is run, functions are defined but code
# isn't executed. it *ay* be executed later in the file
# if the defined function is actually called....

# === pg.1 follows ===

# the following is not run as never called
def print_sum_num(sum_num):
    print("sum_num is: {}".format(sum_num))
    return;

# only run when called, below, in 'main'...
def print_student_handle(stu_handle):
    furst_name, end_name = str(stu_handle).split(' ')
    print("furst_name is: {}".format(furst_name))
    print("end_name is: {}".format(end_name))
    return;


print('___prints right away!')

def main():
    print('Runs when file executed..')
    print_student_handle('curtis ccc')


# new 'main' mechanism
# old fashioned way was 'if __name__ == "__main__":  '

main()

#=== pg.2 follows ===

pp(0,"\n#=== pg.2 follows ===")

pp(0,">> Passing vars <<")

# nom = 5
orig_val = 5
ink_bye = 2

def increase_val(orig_val, ink_val):
    pp(1,"Inside method...")
    pp(1,"orig_val: {0}; id(orig_val): {1}".format(orig_val, id(orig_val)))
    pp(1,"ink_val: {0}; id(ink_val): {1}".format(ink_val, id(ink_val)))
    orig_val+=ink_val
    pp(1,'__(updated) orig_val: {0}; new id(orig_val): {1}'.format(orig_val, id(orig_val)))




# main method
# note the changes don't hold in the main method
# to make it permanent, must use 'global' ...
if __name__ == '__main__':
    pp(0, "Called in 'main' before func...")
    pp(0, "orig_val: {0}; id(orig_val): {1}".format(orig_val, id(orig_val)))
    pp(0, "ink_val: {0}; id(ink_val): {1}".format(ink_bye, id(ink_bye)))
    increase_val(orig_val, ink_bye)
    pp(0, "Called in 'main' AFTER func...")
    pp(0, "orig_val: {0}; id(orig_val): {1}".format(orig_val, id(orig_val)))
    pp(0, "ink_val: {0}; id(ink_val): {1}".format(ink_bye, id(ink_bye)))


#=== pg.4 end of .. ===

pp(0,"\n#=== pg.4 end of .. ===")
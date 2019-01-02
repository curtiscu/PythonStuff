

# Exercises from file ...
#   3 Python Variables in Series_18.pdf

# utility function by curtiscu
# nice/ pretty print stuff ...
def pp(tab_count, str):
    print('\t'*tab_count, str)


# ==== LISTS ====

print("\n# ==== LISTS ====\n")
empty_list = []
empty_list.append(10)
empty_list.append("arse")

print("'empty_list' content: {}".format(empty_list))

ages = [19,21,20]



print("ages: {}".format(ages))

student1_details = [20, 'Michael Kane', 79]
student2_details = [35, 'Mairead Jamella', 56]

class_of_students = [student1_details, student2_details, "some module name", [1,2,3]]

print("class_of_students array: {}\n".format(class_of_students))

x = 1
# choose element to print..
print("ages[{0}]: {1}".format(x, ages[x])) # format string to print element at 'x' ..


s = student2_details
print("{0} \t\t{1} \t{2}".format(s[0], s[1], s[2]))

print("\n2nd element of 1st member of 'class_of_students': {}".format(class_of_students[0][1]))

#--------------

books = []

# doesn't work ...
'''
for i in range(0,4):
    print("hello :) - {}".format(i))
    books[i] = input("Enter book : ")
'''

''' 
# commenting out so I can quickly test the stuff
# after this, which prompts you to input stuff 
# for every execution .. 

for i in range(0,4):
    books.append(input("Enter book title: "))

print("book list: {}".format(books))

for i in range(0,4):
    print("{0} is {1}".format(i, books[i]))
'''

student_subset=class_of_students[0:2]
print("student subset: {}".format(student_subset))

# DONE TO PAGE #2 OF THESE EXERCISES .. MORE TO DO!!!

pp(0,"\n==== ROUGHLY START OF PG.3 ==== \n")

# concatenate list contents, note the difference with 'student_subset' above ...
another_group_of_students = student1_details+student2_details
print("another_group : {}".format(another_group_of_students))

third_group_of_students = ['plop']
third_group_of_students+=another_group_of_students
print("third_group_of_students: {}".format(third_group_of_students))

print("reminder, 'student_subset': {}".format(student_subset))
pp(1,'substring search follows...')
print("'Michael' in list 'student_subset[0][1]' -> {0} ? : {1}".format(student_subset[0][1], "Michael" in student_subset[0][1]))
print("'Michael' in list 'student_subset[0]' -> {0} ? : {1}".format(student_subset[0], "Michael" in student_subset[0]))

# repitition operator '*'

grades = [10,24, 36, 2, 5, 6, 5] # base array
print("\ngrades: {}".format(grades))

nu_grades = [grades] * 2  # new var with *2* copies/ references to *same* array
print("nu_grades : {}".format(nu_grades))  # check it out, same content twice, BUT...

nu_grades[0][0] = 666  # tweak the first element, and...

# ... see that it modified output of both elements..
# as they're THE SAME ELEMENT
print("nu_grades, with repeated list : {}".format(nu_grades))

# END PAGE #4


my_range = range(1,5)
print("\nmy_range: {0}".format(my_range))

my_list = list(my_range)
print("my_list: {}".format(my_list))

stu_grades = [
    ['L98765', 50, 51],
    ['L56789', 60, 61]
]

print('LNum: {}'.format(stu_grades[0][0]))
print('Grade 1: {}'.format(stu_grades[0][1]))

c=5
print('count instances of {0} in {1}: {2}'.format(c, grades, grades.count(c)))


print("len(grades) : {}".format(len(grades)))

grades.sort()
print("grades.sort() : {}".format(grades))

print("grades.pop(6): {}".format(grades.pop(6)))
print("grades: {}".format(grades))

grades.reverse()
print("grades.reverse(): {}".format(grades))

# finished to end of page #5 here ...

# ==== COPYING LISTS =====

print("\n# ==== COPYING LISTS =====\n")

# resetting our vars...
student1_details = [ 20, "Michael Brennan", 77.5]
student2_details = [ 33, "Mairead Gallagher", 65]
class_of_students = [ student1_details, student2_details, "module title", [2, 3, 4] ]

# shallow copy...
student3_details = student2_details

# test
print("Before change...")
print("student3_details: {}".format(student3_details))
print("student2_details: {}".format(student2_details))

# tweak one, see it changes both...
student3_details[0] = 666

# test
print("\nPost change to 'student3_details', to see the shallow copy of 'student2_details' changes both...")
print("student3_details: {0}, ID: {1}".format(student3_details, id(student3_details)))
print("student2_details: {0}, ID: {1}".format(student2_details, id(student2_details)))

# END PAGE #6


# ==== COPY/ DEEPCOPY ====
print("\n# ==== COPY/ DEEPCOPY ====\n")


print("Copying student2_details to student4_details using slice operation...")
student4_details = student2_details[:]
print("student4_details copied by slice: {0}, ID: {1}".format(student4_details, id(student4_details)))

print("\nTesting copying 'class_of_students' using slice op...")
class_of_students2 = class_of_students[:]
print("created class_of_students2: {0}, ID: {1}".format(class_of_students2, id(class_of_students2)))
print(".... copied from class_of_students: {0}, ID: {1}".format(class_of_students, id(class_of_students)))

print("\n==> Apparently nested lists are still shallow copied, testing that info here...")
print("class_of_students: {0}; class_of_students[0]: {1}; id(class_of_students[0]): {2}"
      .format(class_of_students, class_of_students[0], id(class_of_students[0])))

print("class_of_students2: {0}; class_of_students2[0]: {1}; id(class_of_students2[0]): {2}"
      .format(class_of_students2, class_of_students2[0], id(class_of_students2[0])))

print("\n==> it's clear from above that the nested lists were shallow copied!!")
pp(1, "id(class_of_students[0]): {0}".format(id(class_of_students[0])))
pp(1, "id(class_of_students2[0]): {0}".format(id(class_of_students2[0])))

# == copy stuffs...

print("\n==> copy stuff...")
# import and use copy module...
import copy

# tired of the old students, making new student data...
s10_grades = [67, 93, 85]
student10_details = [26, "Curtis Cunningham", 76.2, s10_grades]

# check output
pp(0, "New student...")
pp(1, "student10_details: {0}; id: {1}". format(student10_details, id(student10_details)))
pp(1, "student10_details[1]: {0}; id: {1}".format(student10_details[1], id(student10_details[1])))
pp(1, "student10_details[3]: {0}; id: {1}".format(student10_details[3], id(student10_details[3])))

pp(0, "\nSlice copy 'student10_details' to 'student11_details'...")
student11_details = student10_details[:]
pp(1, "student11_details: {0}; id: {1}". format(student11_details, id(student11_details)))
pp(1, "student11_details[1]: {0}; id: {1}".format(student11_details[1], id(student11_details[1])))
pp(1, "student11_details[3]: {0}; id: {1}".format(student11_details[3], id(student11_details[3])))

pp(0, "\n Deep copy 'student10_details' to 'student12_details'...")
student12_details = copy.deepcopy(student10_details)
pp(1, "student12_details: {0}; id: {1}".format(student12_details, id(student12_details)))
pp(1, "student12_details[1]: {0}; id: {1}".format(student12_details[1], id(student12_details[1])))
pp(1, "student12_details[3]: {0}; id: {1}".format(student12_details[3], id(student12_details[3])))

pp(1,"\n... note in the above output, *ALL* the sublists appear to be shallow copied, elements accessed using\n"
     "subindexes appear to have the same IDs - booo...")
# END PAGE #7

# ==== SETS ====
pp(0,"\n# ==== SETS ====")

# make a list
names=["as", "sd", "df", "df", "ed", "fg", "as"]
pp(0, "names: {}".format(names))
pp(0, "names.len(): {}".format(names.__len__()))

# make a set from the list ...
names_set = set(names)
pp(0, names_set)
pp(0, "names_set.len(): {}".format(names_set.__len__()))

# ==== TUPLES ====
pp(0,"\n# ==== TUPLES ====")

'''
A tuple is effectively a list that cannot be changed. It is immutable. 
The tuple is defined with round brackets. Again it can be nested and 
can have a variety of element types. Elements can be accessed for 
viewing or assigning to new variables however, as shown, items cannot 
be changed.
'''

empty_tuple = ()
pp(0,"empty_tuple: {}".format(empty_tuple))
grades=(34,45,56)
pp(0,"grades: {}".format(grades))

# make some new tuples with sample data
s1_tuple = (22, 'C. Cunningham', 860)
s2_tuple = (44, 'M. McLaughlin', 987)
s3_tuple = (66, "S.O. Git", (567, 432, 232), [111,222,333])

pp(0, "s1_tuple: {}".format(s1_tuple))
pp(0, "s2_tuple: {}".format(s2_tuple))
pp(0, "s3_tuple: {}".format(s3_tuple))

# now pull out the individual bits of the tuple
# using index numbers ....
pp(0, "s1_tuple[0]: {0}; s1_tuple[1]: {1}; s1_tuple[2]: {2}"
   .format(s1_tuple[0], s1_tuple[1], s1_tuple[2]))

students_list = [s1_tuple, s2_tuple, "Ppp-python", (9,98,87,7654), [4, 5, 6]]

# note: doesn't handle leading zeros, the following '09' in the annon
# list at the end of the top level/ main list actually borks the interpreter...
#students_list = [s1_tuple, s2_tuple, "Ppp-python", [09,98,87,7654]]

pp(0,"structure of 'students_list': {}".format(students_list))

pp(0, "item in embedded tuple: {}".format(students_list[0][2]))
pp(0, "item in unamed tuple: {}".format(students_list[3][2]))

# last bit, can't change content of stuff embedded in tuples ...
pp(0,"\n nearly done with tuple tests...")
pp(0,"s3_tuple: {}".format(s3_tuple))
pp(1, "s3_tuple[3]: {}".format(s3_tuple[3]))
pp(1, "s3_tuple[3][1]: {}".format(s3_tuple[3][1]))

# NOTE: she said you can't do this, but you can :)
pp(0,"changing -> s3_tuple[3][1] = 888 ...")
s3_tuple[3][1] = 888
pp(1, "changing s3_tuple[3]: {}".format(s3_tuple[3]))

pp(0,"\nNow experimenting with tuple contents...")
pp(0,"empty_tuple: {}".format(empty_tuple))
list_of_contents = list(empty_tuple)
pp(0,"list_of_contents: {}".format(list_of_contents))
list_of_contents.append("something_on_the_end")
pp(0,"list_of_contents: {}".format(list_of_contents))
empty_tuple = tuple(list_of_contents)
pp(0,"list now assigned to 'empty_tuple': {0}".format(empty_tuple))
pp(0,"len(empty_tuple): {}".format(len(empty_tuple)))

# ==== DICTIONARIES ==== (p.9)
pp(0,"\n# ==== DICTIONARIES ==== (p.9)")


'''
Dictionaries
Dictionaries hold key, value pairs. These are also referred 
to as hash tables and associative array’s in other programming
languages. Dictionaries may contain lists or tuples and may be
contained within lists or tuples. Keys can be any immutable 
type – strings, tuples. Create a dictionary as follows:

    contacts={“Ruth Lennon”:749186355}

'''

campuses = {}  # empty dict
contacts = {"Curtis":123456, "JohnL":234567, "JohnR":345678}
contacts_addr = {"Curtis":"Ardmore", "JohnL":"NoOneKnows", "JohnR":"Seagate"}

pp(0,"contacts: {}".format(contacts))
pp(0,"contacts_addr: {}".format(contacts_addr))
pp(0,"contacts['Curtis']: {}".format(contacts['Curtis']))

# now tweaking contacts dict..
contacts['Mick'] = 987654
pp(0,"contacts: {}".format(contacts))

# now add some stuff to campuses dict...
campuses['LYIT'] = 'Letterkenny'
campuses['UU1'] = 'Magee'
campuses['UU2'] = 'Jordanstown'
campuses['UU3'] = 'Belfawst'
pp(0,'campuses: {}'.format(campuses))

# experiment with deleting...
pp(0,'len(campuses): {}'.format(len(campuses)))
del campuses['UU2']
pp(0,'len(campuses): {}'.format(len(campuses)))
pp(0,'campuses: {}'.format(campuses))

pp(0,"'UU3' in campuses: {}".format('UU3' in campuses))
pp(0,"'UU2' in campuses: {}".format('UU2' in campuses))

c_name, c_addr = campuses.popitem()

pp(0,"c_name: {0}; c_addr: {1}".format(c_name, c_addr))

pp(0,"Post pop: {}".format(campuses))

# testing for item existing in dict...
if 'LYIT' in campuses:
    pp(0,"it's there! see: {}".format(campuses['LYIT']))

pp(0,'direct pull: {}'.format(campuses.get('LYIT')))
pp(0,'direct pull: {}'.format(campuses.get('LYITT')))

# some copying tests ..
contacts_shallow = contacts.copy()
contacts_deep = copy.deepcopy(contacts)

eng_contacts = {'Gizmo':444555}

all_contacts = {}

all_contacts.update(eng_contacts)
all_contacts.update(contacts_deep)

pp(0,"all_contacts: {}".format(all_contacts))

# == end p.10

# == start p.11, iterations...

pp(0,"printing keys for 'all_contacts' ... ")
for key in all_contacts:
    pp(1,'nextKey: {}'.format(key))

# pulling apart the contents of the dict ...
staff = all_contacts.keys()
numbers = all_contacts.values()
list_from_dict =  all_contacts.items()

# creating dictionaries from lists ..
design_phones = [343434, 565656]
design_pholks = ['jason', 'paul']
design_list = (list(zip(design_pholks, design_phones)))
pp(0,"design_list, create list of tuples: {}".format(design_list))

design_dict = dict(design_list)
pp(0,"design_dict, dict from list of tuples: {}".format(design_dict))

# === end p.11 ===

# ==== QUESTIONS ====
pp(0,"\n# ==== QUESTIONS ====")

## Q.1 (EASY) tuples, lists, and dicts

students = ('L123123', 'L789789')

# testing examing contents, and some other printy stuffs ...
pp(0,'testing tuple prints: {}, {}, {}'.format(students[1], students[0], 'bleh'))
pp(0,'testing tuple prints: {1}, {0}'.format(students[1], students[0]))
pp(0,'testing tuple prints: {0}, {1}'.format(students[1], students[0]))

modules = ['BDA','ML']

# testing...
pp(0,'testing list bits: {}, {}'.format(modules[1], modules[0]))

# decided to make a dict of dicts, and the containted
# dicts contain the subject grades...
grades = {students[0]:{}, students[1]: {}}
pp(0,'getting grades: {}'.format(grades))

grades[students[0]]
pp(0,'looking up contained dict for {}: {}'.format(students[0], grades[students[0]]))

# add in our grades...
grades[students[0]][modules[0]] = 55
grades[students[0]][modules[1]] = 65

grades[students[1]][modules[0]] = 44
grades[students[1]][modules[1]] = 77

# show content so far ...
pp(0,'getting grades: {}'.format(grades))

# at this point we have ...
#   {'BDA': {'L123123': 55, 'L789789': 65}, 'ML': {'L123123': 44, 'L789789': 77}}

def show_all():
    # show content so far ...
    pp(1, 'getting grades: {}'.format(grades))

# query user to pull data from dicts...

while True:
    user_input = input("Enter student number, '0' to quit, '1' to print all:")

    # test for return/ no input
    if user_input =='':
        continue

    # check for commands...
    try:
        if int(user_input) == 0:
            pp(1,'Bye...')
            break
        elif int(user_input) == 1:
            show_all()

        # skip to start of loop
        continue

    except:
        # do nothing..
        pass # no-op/ dummy statement

    # attempt to lookup data...
    try:
        student_subjects = grades[user_input]
        pp(1,'student {0}, for the following grades: {1}'.format(user_input, student_subjects))
    except:
        pp(1,'nothing found for: {}'.format(user_input))




## Q. 2 (MEDIUM) list, dicts, lotto numbers



## Q.3 (HARD) read VM config info, verify with user.



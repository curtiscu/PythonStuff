
'''

Related doc...

    https://docs.scipy.org/doc/numpy/reference/routines.math.html \n



'''

# utility function by curtiscu
# nice/ pretty print stuff ...
def pp(tab_count, str):
    print('\t'*tab_count, str)


import pandas as pd
import numpy as np


'''

create a wee container for our code that tests
playing around with various Pandas.Series stuff
NOTE: series = 1 dimensional data structure

'''
class basics_demo_series:

    # pandas left to create default indices
    def create_series_1(self):
        acm_events = pd.Series(['Hour of Code', 'Revision Class 01', 6, 13])
        print('\n')
        print(acm_events)

    # we specify indices at creation time...
    def create_series_2(self):
        acm_events = pd.Series(['Hour of Code', 'Revision Class 01', 6, 13],
                               index=['a','b','c','d'])
        print('\n')
        print(acm_events)

    '''
        This'll take a dictionary and make a series
        out of it, using the dictionaries keys as 
        indices for the newly created series
    '''
    def convert_d(self, d_in):
        p_book = pd.Series(d_in)
        print('\n')
        print(p_book)

    # this one demos methods for selecting elements
    # and modifiying data referenced by an index...
    def series_tweaking_demo(self):
        acm_events = pd.Series(['Hour of Code', 'Revision Class 01', 6, 13],
                               index=['a', 'b', 'c', 'd'])

        acm_events['d'] = 'Lifetime Trip'

        print('\n')
        search_key = 'a'
        pp(0,"\nQ. Is '{0}' in acm_events? \nA. {1} -> {2}\n".
           format(search_key, search_key in acm_events, acm_events['a']))
        print(acm_events)

    def series_maths_funcs(self):
        acm_events = pd.Series(['Hour of Code', 'Revision Class 01', 6, 13],
                               index=['a', 'b', 'c', 'd'])
        stu_grades = pd.Series([66, 99, 55, 33], index=['jo', 'mia', 'ruben', 'oscar'])

        print('\nGrades/4 ...')
        print(stu_grades/ 4) # value * 0.25

        print('\nGrades**')
        print(np.square(stu_grades)) # find value**

        stu_grades2 = pd.Series([11,77,66,44],index=['john','mia','ruben','oscar'])

        a_n_tuther_series = acm_events[2:3] # chopping something out of it

        stu_grades3 = stu_grades + stu_grades2

        print('\nAdded series...')
        print(stu_grades3)

        print('\nTest for null...')
        print(stu_grades3.isnull())


class basics_demo_data_frame:

    def first_func(self):
        pp(0,'\nCall to {}'.format(self))
        pass

    def df_init(self):
        bd_c = { 'yr_sem':['2019_1', '2019_2', '2019_1', '2019_2'],
                 'stu':['001234', '001234', '001122', '001122'],
                 'BI_ML':[55, 66, 65, 67],
                 'BDA_DSP':[36, 70, 68, 71],
                 'DA_PRJ':[60, 70, 70, 72]}

        student_marks = pd.DataFrame(bd_c, columns=['yr_sem','stu','BI_ML','BDA_DSP','DA_PRJ'])

        print('\n')
        print(student_marks)

'''
##
# call series sample code below here
##

# instantiate object to access code
bd = basics_demo_series()


bd.create_series_1()
bd.create_series_2()

# phone book example
phone_b = {'Curtis':12345, 'Gizmo':54321, 'Me ma':67890}
bd.convert_d(phone_b)

# series tweaking example
bd.series_tweaking_demo()

# run the func that does ops/ maths on series contents..
bd.series_maths_funcs()

'''

'''
##
# call DataFrame sample code below here
##


'''

# instantiate object to access code
df = basics_demo_data_frame()

df.df_init()

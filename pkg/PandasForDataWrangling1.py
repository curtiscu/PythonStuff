
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
import os


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



class basics_demo_data_frame:

    def first_func(self):
        pp(0,'\nCall to {}'.format(self))
        pass

    def df_class_init(self):
        bd_c = { 'yr_sem':['2019_1', '2019_2', '2019_1', '2019_2'],
                 'stu':['001234', '001234', '001122', '001122'],
                 'BI_ML':[55, 66, 65, 67],
                 'BDA_DSP':[36, 70, 68, 71],
                 'DA_PRJ':[60, 70, 70, 72]}

        student_marks = pd.DataFrame(bd_c, columns=['yr_sem','stu','BI_ML','BDA_DSP','DA_PRJ'])

        print('\n')
        print(student_marks)

    def df_airport_init(self):
        a_ports_csv = pd.read_csv(os.path.normpath('airports.csv'))

        pp(0,'count(airports.csv)... \n{}'.format(a_ports_csv.count()))
        '''
        NOTE:  each column should have 50305 rows of
        data, so counts less than this indicate
        a column has blanks. fyi, it prints the following..
        
            count(airports.csv): 
            id                   50305
            ident                50305
            type                 50305
            name                 50305
            latitude_deg         50305
            longitude_deg        50305
            elevation_ft         45408
            continent            24479
            iso_country          50061
            iso_region           50305
            municipality         44767
            scheduled_service    50305
            gps_code             40708
            iata_code             9109
            local_code           27583
            home_link             2697
            wikipedia_link        9178
            keywords              5784
            dtype: int64

        '''

        print()
        print(a_ports_csv.keys())

        print()
        print(a_ports_csv.head(10))

    def df_airport_filtered_init(self):

        # column names lifted direct from file using df.keys()
        column_names = ['id', 'ident', 'type', 'name', 'latitude_deg', 'longitude_deg',
            'elevation_ft', 'continent', 'iso_country', 'iso_region',
            'municipality', 'scheduled_service', 'gps_code', 'iata_code',
            'local_code', 'home_link', 'wikipedia_link', 'keywords']

        # 'infer' headers from row in file
        a_ports_csv = pd.read_csv(os.path.normpath('airports.csv'),
                                  delimiter=',',
                                  header='infer',
                                  skip_blank_lines=True)
        print()
        print(a_ports_csv.count())

        print()
        print(a_ports_csv.head(4))

        print()
        print(a_ports_csv.keys())

        print('\n Now show filtered snapshot of columns and rows...')
        print(a_ports_csv[['name', 'latitude_deg', 'longitude_deg']].head(6))


    def df_inspect_init(self):

        # note the different loading params again..
        a_ports_csv = pd.read_csv(os.path.normpath('airports.csv'),
                                  header=0,
                                  index_col=0)
        print()
        print(a_ports_csv.info())

        print()
        print(a_ports_csv.head(4))

        print()
        print(a_ports_csv.tail(4))

        print()
        print(a_ports_csv.describe())

    def df_select_init(self):
        a_ports_csv = pd.read_csv(os.path.normpath('airports.csv'),
                                  header=0,
                                  index_col=0)

        sub_table = a_ports_csv[['name','latitude_deg','longitude_deg']]

        # type 1 filtering
        print()
        print(sub_table[(sub_table.latitude_deg > 75)])

        # type 2 filtering
        trim_table = a_ports_csv[3:6] #reduce to rows 3-5 inc.
        print('\ntrim the main table...\n{}'.format(trim_table))
        print('\ntrim the main table, single column, 3 rows...\n{}'.format(a_ports_csv[['name']][3:6]))
        print('\ntrim previous sub_table..\n{}'.format(sub_table[(sub_table.latitude_deg > 75)][3:6]))


    def df_formatting_tests(self):
        a_ports_csv = pd.read_csv(os.path.normpath('airports.csv'),
                                  header=0,
                                  index_col=0)

        sub_table = a_ports_csv[['name','latitude_deg','longitude_deg']]

        sub_table = sub_table[(sub_table.latitude_deg > 80)]

        print('\nfiltered data...\n{}'.format(sub_table))
        print('\ncount of rows: \n{}'.format(sub_table.count()))
        print('\nhtml...\n{}'.format(sub_table.to_html()))
        print('\njson...\n{}'.format(sub_table.to_json()))


# instantiate object to access code
df = basics_demo_data_frame()

'''
##
# call DataFrame sample code below here
##

# load & display airport data
df.df_airport_init()

df.df_airport_filtered_init()

df.df_inspect_init()

df.df_select_init()

'''

df.df_formatting_tests()


'''

Useful doc...

    https://docs.python.org/3/library/csv.html \n


'''

import csv

# utility function by curtiscu
# nice/ pretty print stuff ...
def pp(tab_count, str):
    print('\t'*tab_count, str)


def count_log_entries():

    # specify counties to search for here ...
    county_text1 = 'MARION COUNTY'
    county_text2 = 'PINELLAS COUNTY'

    pp(0,' \nSearch for counties {0}, {1}'.format(county_text1, county_text2))
    with open('FL_insurance_sample.csv', newline='\n') as csvfile:
        insurance_data = csv.reader(csvfile, delimiter = ',')
        county_count1 = 0
        county_count2 = 0

        for row in insurance_data:
            if (insurance_data.line_num == 1):
                pp(0,'\n...found first line: {}'.format(row))
                continue

            if (row[2] == county_text1):
                #pp(1,'{0} found @ line: {1}'.format(county_text1, insurance_data.line_num))
                county_count1 += 1
            elif (row[2] == county_text2):
                #pp(1, '{0} found @ line: {1}'.format(county_text2, insurance_data.line_num))
                county_count2 += 1

        pp(0,'\n{0}: {1}, {2}: {3}'.format(county_text1, county_count1, county_text2, county_count2))



count_log_entries()


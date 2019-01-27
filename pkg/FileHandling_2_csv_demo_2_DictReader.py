

from csv import DictReader

# utility function by curtiscu
# nice/ pretty print stuff ...
def pp(tab_count, str):
    print('\t'*tab_count, str)


def dict_reader_out1():
    with open('FL_insurance_sample.csv', newline='\n') as csvfile2:
        csv_dict_reader = DictReader(csvfile2)

        marion_counter = 0
        pinellas_counter = 0

        for row in csv_dict_reader:
            pp(0,'Row: {}'.format(row))

            '''
            
            Sample pretty formatted out. It prints the following for each row in the file ..
            
                Row: OrderedDict
                (
                    [
                        ('policyID', '347912'), 
                        ('statecode', 'FL'), 
                        ('county', 'CITRUS COUNTY'), 
                        ('eq_site_limit', '0'), 
                        ('hu_site_limit', '50717.66'), 
                        ('fl_site_limit', '0'), 
                        ('fr_site_limit', '0'), 
                        ('tiv_2011', '50717.66'), 
                        ('tiv_2012', '59502.77'), 
                        ('eq_site_deductible', '0'), 
                        ('hu_site_deductible', '0'), 
                        ('fl_site_deductible', '0'), 
                        ('fr_site_deductible', '0'), 
                        ('point_latitude', '28.906515'), 
                        ('point_longitude', '-82.603765'), 
                        ('line', 'Residential'), 
                        ('construction', 'Wood'), 
                        ('point_granularity', '3')
                    ]
                )
                    
            '''

def dict_reader_out2():
    with open('FL_insurance_sample.csv', newline='\n') as csvfile2:
        csv_dict_reader = DictReader(csvfile2)

        totals_counter = 0
        marion_counter = 0
        pinellas_counter = 0

        policy_high_val = 980000

        for row in csv_dict_reader:
            policy_ID_attribute = int(row['policyID'])
            if (policy_ID_attribute > policy_high_val):
                totals_counter += 1
                pp(0,'Got high policy #: {}'.format(policy_ID_attribute))

        pp(0,'Total policies > {1}: {0}'.format(totals_counter, policy_high_val))


def dict_reader_out3():
    with open('FL_insurance_sample.csv', newline='\n') as csvfile2:
        csv_dict_reader = DictReader(csvfile2)

        totals_counter = 0
        marion_counter = 0
        pinellas_counter = 0

        for row in csv_dict_reader:
            if (row['county'] == "MARION COUNTY"): marion_counter +=1
            elif (row['county'] == "PINELLAS COUNTY"): pinellas_counter +=1


        pp(0,'Marion: {0}, Pinellas: {1}'.format(marion_counter, pinellas_counter))

# testing the variations...
# dict_reader_out1()
#dict_reader_out2()
dict_reader_out3()
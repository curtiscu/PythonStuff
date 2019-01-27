
'''

Useful doc/ links...
    https://ossec-docs.readthedocs.io/en/latest/log_samples/  \n

'''

# utility function by curtiscu
# nice/ pretty print stuff ...
def pp(tab_count, str):
    print('\t'*tab_count, str)



def read_ssh_log():

    log_entries = open("ssh_logon_attempt.txt").readlines()

    total_log_counter = 0
    failed_counter = 0
    illegal_user_counter = 0
    err_counter = 0

    pp(0, '\nPrinting comments, generating counter totals...\n')

    for log_entry in log_entries:
        comments = log_entry[36:] # keeps only the english textual description, 2nd part of line
        non_comments = log_entry[:35] # keeps 1st part of line
        total_log_counter += 1

        pp(1,'{0} - {1}'.format(total_log_counter, comments))

        # gather counter totals...
        if (comments[0] == 'F'): # 'Failed..'
            failed_counter += 1
        elif (comments[0] == 'I'): # 'Illegal..'
            illegal_user_counter += 1
        else: # 'error..'/ other
            err_counter += 1


    print('\n')
    pp(0,'Failed - {}'.format(failed_counter))
    pp(0,'Illegal - {}'.format(illegal_user_counter))
    pp(0,'error /other - {}'.format(err_counter))


read_ssh_log()


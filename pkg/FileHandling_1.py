
'''

Useful doc...
    https://realpython.com/working-with-files-in-python/ \n
    https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects \n
    https://www.datacamp.com/community/tutorials/reading-writing-files-python

'''

# utility function by curtiscu
# nice/ pretty print stuff ...
def pp(tab_count, str):
    print('\t'*tab_count, str)


lines=open ("sampleTxt.txt").readlines()
#lines.sort() #this method can be used to sort a file
pp(0,'\ntesting opening file and splitting lines into tokens...')
for line in lines:
    student, L_num, course = line.split(",")
    pp(1, "Student Name: {0}, LNumber: {1}, and Course: {2}".format(student,L_num,course))

# testing other file methods...

# get a file handle..
file_thing = open("sampleTxt.txt", "r+t")

pp(0,"\nprint line by line, notice the trailing '<' gets dumped on a newline in the output as 'next_line' has '\\n' at the end of it")

for next_line in (file_thing):
    pp(1,'line>{0}<'.format(next_line))


pp(0, "\ntesting stripping white/ dead space, note the '<' no longer printed on a new line..")

# rewind file to start to process it a little differently
file_thing.seek(0)

for next_line in (file_thing):
    pp(1,'line>{0}<'.format(next_line.strip()))


# write something to the file..
# TODO: commenting this out as it continually appends while
#   I'm testing the code in the rest of the file...
#file_thing.write("\nBatman, L666666, MSc in BioHacking")

# rewind file again to start to process it a little differently
file_thing.seek(0)

whole_file = file_thing.read()

pp(0,'\ndumping entire file contents, after writing to it ...')
print(whole_file)

file_thing.close()

pp(0,'\njust closed file: {}'.format(file_thing.name))


#=== pg.3 stuff ===

'''
this part is mostly about seeking, but no real
examples of using those functions. found some in
the python doc, testing those here...
'''

pp(0,'\ntesting some code from the python doc..')

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')

pp(1,'Go to the 6th byte in the file: {}'.format(f.seek(5))) # note the output is the position in the file
pp(1,'f.read(1): {}'.format(f.read(1)))
pp(1,'Go to the 3rd byte before the end: {}'.format(f.seek(-3, 2))) # note the output is the position in the file
pp(1,'f.read(1): {}'.format(f.read(1)))

f.close()

#=== pg.4 stuff ===

import os

base_dir = ".."
pp(0,'\n Printing contents of: {}'.format(base_dir))
for folder_name, sub_folders, file_names in os.walk(base_dir):
    pp(1,'folder: {}'.format(folder_name))

    for sub_folder in sub_folders:
        pp(2,'folder: {1}, is a subfolder of: {0}'.format(folder_name,sub_folder))

    for file_name in file_names:
        pp(2,'file: {0}, is in folder: {1}'.format(file_name, folder_name))

    print('\n')


# TODO: finish these questions...

pp(0,'\n==== QUESTIONS ==== TODO')

pp(1,'Q1: take dir as input, check exists, then total file sizes in given dir')

pp(1,'Q2: as #1, but recurse through subfolders')

pp(1,'Q3: from given dir/ location, recurse through entire contents saving to a list any files with .txt or .doc suffixes')
import settings
import datetime
import os


def create_file():
    # Find new sequence number
    current_files = os.listdir(settings.PATH_TO_REQ)
    print current_files
    sequence_number = 0
    for f in current_files:
        # Check for valid filenames
        if len(f) == 32:
            if int(f[25:28]) > sequence_number:
                sequence_number = int(f[25:28])
            print f, sequence_number
    # Create File
    try:
        sequence_number += 1
        file_name = settings.PATH_TO_REQ + settings.REQ_FILE_NAME + str(sequence_number) + '.xml'
        print file_name
        new_file = open(file_name, 'w+')
        return new_file
    except IOError:
        print 'Cannot create file: ', file_name


# create_file()
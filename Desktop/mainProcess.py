
# PART 1 - All the basic work of the program is implemented in this file

################################################################################################################################################################################
################################################################################################################################################################################
################################################################################################################################################################################

from __future__ import print_function
import sys
import csv
import random

class doMainProcess(object):

    # Name of the object
    def __init__(self, name):
        self.name = name

    #A function that executes the doReadFile function below
    def doRun(self, library):
        print("\n################################## THE {0} IS STARTING! ##################################".format(self.name))
        self.doReadFile(library)
        print("\n################################## THE PROCESS HAS FINISHED! ##################################")

    #Basic function
    #Calls the store function and adds the item to the library
    def doReadFile(self, library):
        i = 0
        f = open('./books.txt', 'r')
        try:
            reader = csv.reader(f)
            x = list(reader)
            for row in x:
                print("  ")
                if(row[0] == 'd'):
                    print("The library contains:")
                    if not library.list_contents():
                        print ("None book")
                    for i in library.list_contents():
                        print(i)
                elif(row[0] == 'a'):
                    row.append("NOT ON Loan")
                    id = random.getrandbits(32)
                    print ("Adding book with ID: {}".format(id))
                    row.append(str(id))
                    y = library.store(row)
                elif(row[0] == 'sy'):
                    z = library.list_contents()
                    for c in z:
                        for x in range(len(c)):
                            if ((c[x] > row[1]) & (c[x] < row[2])):
                                print ("The book which has publication date within the specified year range is: {}".format(c))
                elif(row[0] == 'si'):
                    z = library.list_contents()
                    for c in z:
                        for x in range(len(c)):
                            if (c[x] == row[1]):
                                print ("The book wwth the specified ISBN is: {}".format(c))
                elif(row[0] == 'ol'):
                    z = library.list_contents()
                    for c in z:
                        for x in range(len(c)):
                            if (c[x] == row[1]):
                                c[x+3] = 'ON Loan'
                                print ("Change the status of the specified book: {}".format(c))
                elif(row[0] == 'nol'):
                    z = library.list_contents()
                    for c in z:
                        for x in range(len(c)):
                            if (c[x] == row[1]):
                                c[x+3] = 'NOT ON Loan'
                                print ("Change the status of the specified book: {}".format(c))

        finally:
            f.close()

################################################################################################################################################################################
################################################################################################################################################################################
################################################################################################################################################################################

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 17:59:34 2018

@author: Urchaug
"""

# INFORMATION ABOUT ONE EMPLOYEE
class EmployeeRecord:
    def _init_(self, n, i, r):
        self.name = n
        self.id = i
        self.pay_rate = r
        
def open_database(filename, db):
    '''
    read employee information from a given file and store it
    in the given vector.
    returns true if the file could be read; otherwise,
    it returns false.
    '''
    # open file to read
    lines = open(filename)
    for line in lines:
        name, id, rate = eval(line)
        db.append(EmployeeRecord(name, id, rate))
    lines.close()
    return True

def print_database(db):
    '''
    display the contents of the database
    '''
    for rec in db:
        print(str.format("{:>5}: {:<10} {:>6.2f}", \
                         rec.id, rec.name, rec.pay_rate))
        
def less_than_by_name(e1, e2):
    """
    returns true if e1's name is less than e2's
    """
    return e1.name < e2.name


def less_than_by_id(e1, e2):
    """
    returns true if e1's name is less than e2's
    """
    return e1.id < e2.id

def less_than_by_pay(e1, e2):
    """
    returns true if e1's name is less than e2's
    """
    return e1.pay_rate < e2.pay_rate


def sort(db, comp):
    """
    sort the database object db ordered by the given comp function.
    """
    n = len(db)
    for i in range(n - 1):
        smallest = i;
        for j in range(i + 1, n):
            if comp(db[j], db[smallest]):
                smallest = j
        if smallest != i:
            db[i], db[smallest] = db[smallest], db[i]
            
def main():
    # simple "database" of employees
    database = []
    
    #  open file to read
    if open_database("data.dat", database):
        # print the contents of the database
        print("-----Unsorted:")
        print_database(database)
        
        
        # sort by name
        sort(database, less_than_by_name)
        print("-------Name order:")
        print_database(database)
        
                # sort by ID
        sort(database, less_than_by_id)
        print("-------ID order:")
        print_database(database)

        # sort by pay rate
        sort(database, less_than_by_pay)
        print("------Pay order:")
        print_database(database)
    else: # error could not open file
        print("could not open database file")
        
main()

         
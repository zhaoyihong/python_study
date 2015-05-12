#!/usr/bin/env python
# coding=utf-8

import sys,shelve

fields = ('name','age','phone')


def store_person(db):
    pid = raw_input('Enter your id number:')
    person=dict()
    person['name']=raw_input('Enter name:')
    person['age']=raw_input('Enter age:')
    person['phone']=raw_input('Enter phone number:')
    db[pid]=person

def lookup_person(db):
    pid=raw_input('Enter your id number:')
    if pid not in db:
        print "id %s is not exist!" % pid
        return
    global fields
    field=raw_input('What would you like to know?')
    field=field.strip().lower()
    if field not in fields:
        print 'filed %s is not exits!'  % field
        return 
    print field.capitalize() + ":"  + db[pid][field]

def delete_person(db):
    pid=raw_input('Enter your id number:')
    if pid not in db:
        print "id %s is not exist!" % pid
        return
    confirm=raw_input('delete %s ?(y/n)' % db[pid])
    confirm=confirm.strip().lower()
    if confirm == 'y':
        del db[pid]

def print_help():
    print "the avalable commands are:\n"
    print "store:Store information about a person"
    print "lookup:Look up a person about a person"
    print "del:Delete a information  about a person"
    print "quit:Save change and exit"
    print "?:print this message"

def enter_cmd():
    cmd=raw_input("Enter command(? for help):")
    cmd=cmd.strip().lower()
    return cmd


if __name__ == "__main__":
    database = shelve.open('person.dat')
    try:
        while True:
            cmd = enter_cmd()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == 'quit':
                sys.exit(0)
            elif cmd == 'del':
                delete_person(database)
            elif cmd == '?':
                print_help()
            else:
                print "unvalid commad"
                print_help()
    finally:        
        database.close()



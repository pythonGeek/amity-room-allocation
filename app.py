'''
Usage:
    add_person <person_id> <first_name> <last_name> <F|S> [--wants_accomodation=N]
    create_room <room_name> <room_type>
    reallocate_person <full_name> <new_room_name>
    load_people <filename>
    print_allocations [--o=filename]
    print_unallocated [--o=filename]
    print_room <room_name>
    save_state [--db=sqlite_database]
    load_state [--db=sqlite_database]
    quit
Options:
    -h, --help  Show this screen and exit
    -i --interactive  Interactive Mode
    --wants_accomodation=<N> [defult: N]
'''

from app.amity import Amity
import sys
import cmd
import os
from termcolor import cprint, colored
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

border = colored("*" * 20, 'cyan').center(80)
def introduction():
    print (border)
    print ("WELCOME TO AMITY SPACE ALLOCATION!".center(70))
    print(__doc__)
    print (border)

class AmityApplication(cmd.Cmd):
    cprint(figlet_format('AMITY', font='banner3-D'), 'cyan', attrs=['bold'])

    prompt = "Amity -->"

    @docopt_cmd
    def do_create_room(self, arg):
        '''Usage: create_room <room_name> <room_type>'''
        r_name = arg["<room_name>"]
        r_type = arg["<room_type>"]
        if r_name.upper in Amity.all_rooms:
            cprint('Room already exists')
            return
        else:
            Amity.create_room(r_name.upper(), ''.join(r_type.upper()))

    @docopt_cmd
    def do_add_person(self, arg):
        '''Usage: add_person <person_id> <firstname> <lastname> <position> [--wants_accomodation=N] '''
        p_id = arg["<person_id>"]
        f_name = arg["<firstname>"]
        l_name = arg["<lastname>"]
        pos = arg["<position>"]
        wants_accomodation = arg["--wants_accomodation"]

        if wants_accomodation:
            Amity.add_person(p_id, f_name, l_name, pos, wants_accomodation)
        else:
            Amity.add_person(p_id, f_name, l_name, pos)

    @docopt_cmd
    def do_load_people(self, arg):
        ''' Usage: load_people <filename>'''
        file_n = arg["<filename>"]
        if os.path.exists(file_n):
            Amity.load_people(file_n)
        else:
            print("File not found")

    @docopt_cmd
    def do_reallocate_person(self, arg):
        ''' Usage: reallocate_person <firstname> <lastname> <new_room_name>'''
        first_name = arg["<firstname>"]
        last_name = arg["<lastname>"]
        full_name = first_name + " " + last_name
        new_room = arg["<new_room_name>"]

        if new_room.upper() in Amity.office_rooms:
            Amity.reallocate_person_from_office(full_name.upper(), new_room.upper())
        elif new_room.upper() in Amity.ls_rooms:
            Amity.reallocate_person_from_ls(full_name.upper(), new_room.upper())
        else:
            print('%s is not a room in Amity' % new_room)

    @docopt_cmd
    def do_print_room(self, arg):
        ''' Usage: print_room <room_name>'''
        r_name = arg["<room_name>"]
        if r_name.upper() in Amity.all_rooms:
            Amity.print_room(r_name)
        else:
            print('There is no room called %s in Amity' % r_name)

    @docopt_cmd
    def do_print_allocations(self, arg):
        '''Usage: print_allocations [--o=filename] '''
        filename = arg["--o"]

        if filename:
            Amity.print_allocations(filename)
        else:
            Amity.print_allocations()

    @docopt_cmd
    def do_print_unallocated(self, arg):
        '''Usage: print_unallocated [--o=filename] '''
        filename = arg["--o"]

        if filename:
            Amity.print_unallocated(filename)
        else:
            Amity.print_unallocated()

    @docopt_cmd
    def do_save_state(self, arg):
        '''Usage: save_state [--db=sqlite_database]'''
        database_name = arg["--db"]
        if database_name:
            Amity.save_state(database_name)
        else:
            Amity.save_state('default_db')

    @docopt_cmd
    def do_load_state(self, arg):
        '''Usage: load_state <sqlite_database>'''
        pass

    @docopt_cmd
    def do_quit(self, arg):
        '''Usage: quit '''
        print("GOODBYE!!!")
        exit()


if __name__ == '__main__':
    introduction()
    AmityApplication().cmdloop()

# amity-room-allocation
[![Build Status](https://travis-ci.org/pythonGeek/amity-room-allocation.svg?branch=develop)](https://travis-ci.org/pythonGeek/amity-room-allocation)
[![Coverage Status](https://coveralls.io/repos/github/pythonGeek/amity-room-allocation/badge.svg)](https://coveralls.io/github/pythonGeek/amity-room-allocation)
## Introduction
The Amity room allocation is a system that allocates rooms to the Staff and fellows working at Andela. Developed in #python.

1. `create_room <room_name>...` - Creates a room in Amity. This command can create as many rooms as possible by specifying multiple room names
2. `add_person <firstname> <lastname> <F|S> [--wants_accomodation=N]` - Add a person to the system and allocates the person to a random room
3. `reallocate_person <person_identifier> <new_room_name>` - Reallocate the person with person with `person_identifier` to `new_room_name`
4. `load_people` - Adds people to rooms from a text file
5. `print_allocations [-o=filename]` - Prints a list of allocations  onto the screen. Specifying the optional -o option here outputs the information to the text file provided
6. `print_unallocated [-o=filename]` - Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to the text file provided
7. `print_room <room_name>` - Prints the names of the people in `room_name` on the screen
8. `save_state [--db=sqlite_database]` - Persists all the data stored in the app to a SQLite database. Specifying the --db parameter explicitly stores the data in the sqlite_database specified.
9. `load_state <sqlite_database>` - Loads data from a database into the application.

## Installation & Setup
1. Download & Install Python
 	* Head over to the [Python Downloads](https://www.python.org/downloads/) Site and download a version compatible with your operating system
 	* To confirm that you have successfully installed Python:
		* Open the Command Propmpt on Windows or Terminal on Mac/Linux
		* Type python
		* If the Python installation was successfull you the Python version will be printed on your screen and the python REPL will start
2. Clone the repository to your personal computer to any folder
  * Url  - https://github.com/pythonGeek/amity-room-allocation.git
 	* Enter the terminal on Mac/Linux or Git Bash on Windows
 	* Type `git clone ` and paste the URL

3. Virtual Environment Installation
 	* Install the virtual environment by typing: `pip install virtualenv` on your terminal
4. Install the required modules
 	* Inside the directory where you cloned the repository run `pip install -r requirements.txt`
5. Inside the application folder run the app.py file:
 * On the terminal type `python app.py -i` to start the application

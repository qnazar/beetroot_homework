# When you start a Python interpreter, one of the things it creates automatically is a list that contains
# all directories it will use to search for modules when importing.
# This list is available in a variable named sys.path.
# Note that the empty '' entry means the current directory.
import sys
print(sys.path)
# You are allowed to modify sys.path during run-time. Just be sure to modify it before you call import.
# It will search the directories in order stopping at the first place it finds the specified modules.

# PYTHONPATH is related to sys.path very closely.
# PYTHONPATH is an environment variable that you set before running the Python interpreter.
# PYTHONPATH, if it exists, should contain directories that should be searched for modules when using import.
# If PYTHONPATH is set, Python will include the directories in sys.path for searching.
# Use a semicolon to separate multiple directories.

# set PYTHONPATH=C:\pypath1\;C:\pypath2\
# python -c "import sys; print(sys.path)"

# So, in order to import modules or packages, they need to reside in one of the paths listed in sys.path.
# You can modify the sys.path list manually if needed from within Python.
# It is just a regular list, so it can be modified in all the normal ways.
# For example, you can append to the end of the list using sys.path.append()
# or to insert in an arbitrary position using sys.path.insert()
sys.path.append('')
sys.path.insert(0, '')
print(sys.path)

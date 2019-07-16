import sys

# Input File -> List
# Opens input file/stream, places lines into list and returns list
def constructor():
    with open(sys.argv[1], 'r') as my_file:
        assemblylines = my_file.readlines()
    assemblylines = [x.strip() for x in assemblylines] 
    return assemblylines

# Nothing -> Boolean
# Are there more commands in the input?
def hasMoreCommands():
    return True

# Nothing -> Nothing
# Reads the next command from the input and makes it
# the current command. Should be called only if the
# if hasMoreCommands() is true. Intitially there is
# no current command.
def advance():
    return null

# Nothing -> Command 
# Returns the type of the current command.
def commandType():
    return currentcommand

# Nothing -> String
# Returns the symbol of decimal Xxx of current command @
# or (Xxx). Should be called only when commandType() is 
# A_COMMAND or L_COMMAND
def symbol():
    return string

# Nothing -> String
# Returns dest mnemonic in the current C-command
# (8 possibilities). Should be called only when 
# commandType() is C_COMMAND
def dest():
    return string

# Nothing -> String
# Returns the comp mnemonic in the current C-command
# (28 possibilities). Should be called only when
# the commandType() is C_COMMAND
def comp():
    return string

# Nothing -> String
# Returns the jump mnemonic in the current C-command
# (8 possibilities). Should be called only when the
# commandType() is C_COMMAND
def jump():
    return string

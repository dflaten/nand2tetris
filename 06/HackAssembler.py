from Parser import constructor, commandType

def main():
    #Get list of lines from file loaded in commandline argument
    assemblylines = constructor()
    assemblylines_nocomments=[]
    converted_assembly=[]
    #Replace comments with white space, remove spaces.
    for line in assemblylines:
        line = line.split("//", 1)[0]
        line = line.replace(" ", "")
        assemblylines_nocomments.append(line)
    #Remove blank lines.
    assemblylines_nocomments = list(filter(None, assemblylines_nocomments))
    for line in assemblylines_nocomments:
        cmdtype =  commandType(line)
        if cmdtype == "A_COMMAND":
            line = int(line[1:])
            binary_number = "{0:015b}".format(line)
            binary_line = '1' + str(binary_number) 
            converted_assembly.append(binary_line)
#        elif cmdtype == "COMMAND":

#    for printme in assemblylines_nocomments:
#        print(printme)
if __name__ == "__main__":
    main()

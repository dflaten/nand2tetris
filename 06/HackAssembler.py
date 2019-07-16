from Parser import constructor

def main():
    #Get list of lines from file loaded in commandline argument
    assemblylines = constructor()
    assemblylines_nocomments=[]
    #Replace comments with white space, remove spaces.
    for line in assemblylines:
        line = line.split("//", 1)[0]
        line = line.replace(" ", "")
        assemblylines_nocomments.append(line)
    #Remove blank lines.
    assemblylines_nocomments = list(filter(None, assemblylines_nocomments))
    for printme in assemblylines_nocomments:
        print(printme)
if __name__ == "__main__":
    main()

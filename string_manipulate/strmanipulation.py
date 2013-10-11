import re

#
#
#
#  usage : $python <strmanipulation.py> <input_string>
#
#
#



def string_manipulator():
    print "Function to remove white-spaces and remove duplicate chars, if adjecent to each other"
    input = raw_input("Enter input string: ")
    stripped_string = remove_whitespaces(input=input)
    print "***"

    print "result string without whitespaces :  {0}".format(stripped_string)
    no_dup_string = remove_duplicates(input=stripped_string)
    print "result string without duplicate chars next to each other :  {0}".format(no_dup_string)

    print "***"


def remove_whitespaces(input=None):
    if input is not None:
        return "".join(input.split())


def remove_duplicates(input=None):
    if input is not None and len(input)>0:
    #using regex to catch duplicate chars next to each other and truncate them
     return re.sub("(.)\\1+", "\\1", input)

if __name__ == '__main__':
    string_manipulator()

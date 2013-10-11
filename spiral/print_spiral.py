import sys
from os.path import basename

__author__ = 'nikh0881'


#
#
#
#  usage : $python <print_spiral.py> <input_file_path>
#
#
#


def print_spiral():
    try:
        #Read input from sys args
        # usage : $python <python_file_name> <input_data_file>
        file_path = sys.argv[1]
        file = open(file_path)
        #define a matrix
        matrix = [line.split() for line in file]
        #validate if input matrix is of (n x m ) format if not then raise exception
        child_list_size = len(matrix[0])
        if all(len(x) == child_list_size for x in matrix):
            print "printing matrix in spiral order (clockwise):\n"
            print clockwise(matrix)
        else:
            raise InvalidMatrixInputException(
                message="Invalid matrix input , matrix should be in (n x m) format."
            )


    except InvalidMatrixInputException as e:
        print e.message
        exit(-1)

    except (ValueError) as e:
        print e.message
        exit(-1)

    except (IndexError) as e:
        print "usage : $python {0} {1} ".format(basename(sys.argv[0]), '<input_file_path>')
        exit(-1)

    except(IOError)as e:
        print "{0} : ( file_path : {1} )".format(getattr(e, 'strerror'), sys.argv[1])
        exit(-1)

    except Exception as e:
        raise


def clockwise(r):
    #recursively print matrix in spiral pattern
    #logic :
    #       check if input is not empty, if not then print first row of the list/matrix
    #       transpose  remaining rows  to columns and reverse it.
    #       input matrix eg : 1 2 3                     first run : print [1 ,2 ,3]
    #                         2 4 5                     transpose : zip [next-row]  matrix would be now  2 6
    #                         6 7 8                                                                      4 7
    #                                                                                                    5 8
    #
    #                                                   reverse list : resultant matrix would be now  5 8
    #                                                                                                 4 7
    #                                                                                                 2 6
    #
    #                                                  print first row now , and continue process
    #
    #

    return list(r[0]) + clockwise(list(reversed(zip(*r[1:])))) if r else []


class  InvalidMatrixInputException(Exception):
    def __init__(self, **kwargs):
        self.message = kwargs.get('message')

    pass


if __name__ == '__main__':
    print_spiral()





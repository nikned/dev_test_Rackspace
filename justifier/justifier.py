__author__ = 'nikh0881'
import sys
from os.path import basename



#
#
#  usage : $python <justifier.py> <input_file_path> <width>
#
#



def justify_text():
    try:
        execute(file=open(sys.argv[1]), width=int(sys.argv[2]))

    except (ValueError) as e:
        print e.message
        exit(-1)

    except(TypeError) as e:
        print e.message
        print "usage : $python {0} {1} {2}".format(basename(sys.argv[0]), '<input_file_path>', '<column_width>')
        exit(-1)

    except (IndexError) as e:
        print "index out of bound exception, script failed "
        print "usage : $python {0} {1} {2}".format(basename(sys.argv[0]), '<input_file_path>', '<column_width>')
        exit(-1)

    except(IOError)as e:
        print "{0} : ( file_path : {1} )".format(getattr(e, 'strerror'), sys.argv[1])
        print "usage : $python {0} {1} {2}".format(basename(sys.argv[0]), '<input_file_path>', '<column_width>')
        exit(-1)

    except Exception as e:
        raise


def execute(file=None, width=None):
    for line in file:
        line.replace('\n', " ")
        last_position = len(line) - 1
        output_text = []
        start = 0

        if not last_position == 0:
            while True:
                end = start + width + 1 # +1=allow for next character is space
                rec = line[start:end].strip()
                sub_string_len = len(rec)
                counter = -1
                if end < last_position:
                    ## look for space from right to left
                    while counter + width != 0 and rec[counter] != " ":
                        counter -= 1
                    record = rec[:counter].strip()
                    if len(record) > 0:
                        output_text.append(record)
                    start += len(rec[:counter]) + 1  #skip space
                else:
                    output_text.append(line[start:].strip())
                    break
        print "\n".join(output_text)


if __name__ == '__main__':
    justify_text()
    #justify_text_test()

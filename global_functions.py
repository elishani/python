import re
import sys

def get_para_value(filename, string_to_find, para=None):

        '''     Get paramter string in file "para = value" and return is value
                with a lot of  variations:
                stringA para = value
                stringA stringB para = value stringC
                para=value
                para = value
                para  = value
                para =    value
        '''
        if  para == None  : para = string_to_find
        string_to_find = string_to_find.lstrip()

        array_file = []
        try:
                with open(filename) as f:
                        for line_file in f:
                                array_file.append(line_file)
        except Exception:
                print("\n***ERROR:  Could not open file %s\n" %(filename))
                sys.exit(1)

        i = 0
        while i < len(array_file):
                line = str(array_file[i]).lstrip()
                if line.startswith('#'):
                        line = None
                        next
                if line != None:
                        if string_to_find in line:
                                 break
                        else:
                                line = None
                i += 1

        if not line:
                raise  "***ERROR: Parameter '%s' is not defined. Please check log file for detailed description" % (string_to_find)

        line = re.sub( '\s+', ' ', line ).strip()
        line = line.replace(" =", "=").replace("= ", "=")
        line = line + " "
        pattern = para + "=.+ "
        left_list = re.findall(pattern, line)
        para_value = str(left_list[0].split()[0])
        value_str = para_value.split("=",1)[1]
        if not value_str:
                raise  "***ERROR: Parameter '%s' has no value. Please check log file for detailed description" % (value_str)

        return value_str

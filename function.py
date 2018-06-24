import re

def get_para_value(filename, string_to_find, para=None):

        '''     Get paramter string in file "para = value" and return is value
                with allot of  variations:
                stringA para = value
                stringA stringB para = value stringC
                para=value
                para = value
                para  = value
                para =    value
        '''

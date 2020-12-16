import re

def get_para_value(filename, string_to_find, para=None):

        """     Get parameter string in file "para = value" and return is value
                with allot of  variations:
                stringA para = value
                stringA stringB para = value stringC
                para=value
                para = value
                para  = value
                para =    value
        """
        if  para is None :
                para = string_to_find.lstrip()

        array_file = []
        try:
                with open(filename) as f:
                        for line_file in f:
                                array_file.append(line_file)
        except Exception:
                print("Could not open file %s\n" %(filename))

        i = 0
        while i < len(array_file):
                line = str(array_file[i]).lstrip()
                if line.startswith('#'):
                        line = None
                        next
                if line is None:
                        line = " " + line
                        exact_string_to_find = " " + string_to_find
                        if exact_string_to_find in line:
                                 break
                        else:
                                line = None
                i += 1

        if not line:
                raise  Exception (string_to_find + " Is not in file")

        line = re.sub( '\s+', ' ', line ).strip()
        line = line.replace(" =", "=").replace("= ", "=")
        line = " " + line + " "
        pattern = " " + para + "=.+ "
        left_list = re.findall(pattern, line)
        if not left_list:
                raise  Exception (para + " Parameter is not found or dose not have value.")

        para_value = str(left_list[0].split()[0])
        value_str = para_value.split("=",1)[1]
        if not value_str:
                raise  Exception (value_str + " Has no value.")

        return value_str
#File
v = "ppppp"
v2 = "lllll"
with open("file.txt") as f:
  for line in f:
    line = line.strip()
    eval(line)
  print(f"'{v}'")
  print(f"'{v2}'")
        
 new_str="123"
fileout="temp"
fo=open("temp", 'w')
fi=open("file.txt")
for line in fi:
  if line.startwith("# roles") or line.startwith("roles"):
    line = new_str
    fo.write(line+"\n")
  else:
    fo.write(line)
fo.close()
fi.close()

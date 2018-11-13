import sys
import os
import fileinput
import re
from collections import defaultdict

primitives = ['short', 'int', 'unsigned',
              'long', 'double', 'float',
              'char', 'wchar_t', 'std::string']

class_list = defaultdict(dict)
current_class = ''

with open(sys.argv[1]) as f:
  for line in f:
    if '#reflect_class' in line:
      line = next(f)
      class_vars = []
      class_name = ''
      while class_name == '':
        class_info = re.split('\W+', line)
        class_name = class_info[1]
      current_class = class_name
    elif '#reflect_var' in line:
      line = next(f)
      split_point = 0
      for word in line.split():
        if word in primitives:
          split_point += len(word)+1
      type = line.strip()[:split_point]
      var_name = line.strip()[split_point:].split()[0].split(';')[0]
      class_list[current_class][var_name] = type

include_line = True

with fileinput.input(sys.argv[1], inplace=True, backup='.bak') as f:
  for line in f:
    if '#include <iostream>' in line:
    elif '#reflect_class' in line:
      if include_line:
        print('#include <iostream>')
        include_line = False
      line = next(f)
      ##print(line, end='')
      class_name = ''
      while class_name == '':
        print(line, end='')
        class_info = re.split('\W+', line)
        class_name = class_info[1]
      line = next(f)
      while '#class_printer' not in line:
        if '#reflect_var' not in line:
          print(line, end='')
        line = next(f)
      line = next(f)
      print('\npublic:\nfriend std::ostream& operator<<(std::ostream& os, const ' + class_name + ' &class_t);\n')
      while '#reflect_end' not in line:
        print(line, end='')
        line = next(f)

      print('\nstd::ostream& operator<<(std::ostream& os, const ' + class_name + ' &class_t) {')
      print('  os ', end='')
      for name in class_list[class_name]:
        print('  << class_t.' + name + '<< \'\\n\'', end='')
      print(';\n  return os;\n}')
    else:
      print(line, end='')
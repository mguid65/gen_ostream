import sys
import os
import fileinput
import re
from collections import defaultdict

primitives = ['short', 'int', 'unsigned', 'signed',
              'long', 'double', 'float', 'char',
              'wchar_t', 'std::string',
              'uint16_t', 'uint32_t', 'uint64_t',
              'uint8_t',
              'uint_fast8_t', 'uint_fast16_t', 'uint_fast32_t',
              'uint_fast64_t',
              'uint_least8_t', 'uint_least16_t', 'uint_least32_t',
              'uint_least64_t',
              'int8_t', 'int16_t', 'int32_t', 'int64_t',
              'int_fast8_t', 'int_fast16_t', 'int_fast32_t',
              'int_fast64_t',
              'int_least8_t', 'int_least16_t', 'int_least32_t',
              'int_least64_t',
              'uintmax_t', 'uintptr_t',
              'intmax_t', 'intptr_t',
              'size_t'
              ]

class_list = defaultdict(dict)
current_class = ''

with open(sys.argv[1]) as f:
  for line in f:
    if '#parse_class' in line:
      line = next(f)
      class_vars = []
      class_name = ''
      while class_name == '':
        class_info = line.split()
        class_name = class_info[1].strip()
      current_class = class_name
    elif '#parse_var' in line:
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
      pass
    elif '#parse_class' in line:
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
        if '#parse_var' not in line:
          print(line, end='')
        line = next(f)
      line = next(f)
      print('\npublic:\nfriend std::ostream& operator<<(std::ostream& os, const ' + class_name + ' &class_t);\n')
      while '#parse_end' not in line:
        print(line, end='')
        line = next(f)

      print('\nstd::ostream& operator<<(std::ostream& os, const ' + class_name + ' &class_t) {')
      for name in class_list[class_name]:
        print(' os << class_t.' + name + '<< \'\\n\';')
      print('\n  return os;\n}')
    else:
      print(line, end='')

#include <string>

#reflect_class
class TestClass {
public:
  TestClass() {}
  TestClass(int i, std::string j, std::string k, unsigned long long l) {
    test_int = i;
    test_string = j;
    secret = k;
    tmp = l;
  }
#reflect_var
  int test_int;
#reflect_var
  std::string test_string;
private:
#reflect_var
  std::string secret;
#reflect_var
  unsigned long long tmp;
#class_printer
};
#reflect_end


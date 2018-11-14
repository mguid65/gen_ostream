#include <string>

#parse_class
class TestClass {
public:
  TestClass() {}
  TestClass(long long class_id, std::string test_string_0, std::string test_string_1, std::string test_string_2,
		std::string test_string_3, std::string test_string_4, std::string test_string_5,
		std::string test_string_6, std::string test_string_7, std::string test_string_8,
		std::string test_string_9) :
                class_id(class_id),
		test_string_0(test_string_0),test_string_1(test_string_1),test_string_2(test_string_2),
		test_string_3(test_string_3),test_string_4(test_string_4),test_string_5(test_string_5),
		test_string_6(test_string_6),test_string_7(test_string_7),test_string_8(test_string_8),
		test_string_9(test_string_9){}
#parse_var
  long long class_id;
#parse_var
  std::string test_string_0;
#parse_var
  std::string test_string_1;
#parse_var
  std::string test_string_2;
#parse_var
  std::string test_string_3;
#parse_var
  std::string test_string_4;
#parse_var
  std::string test_string_5;
#parse_var
  std::string test_string_6;
#parse_var
  std::string test_string_7;
#parse_var
  std::string test_string_8;
#parse_var
  std::string test_string_9;
#class_printer
};
#parse_end

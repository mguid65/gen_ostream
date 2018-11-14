#include "test_class.h"
#include <iostream>
#include <string>
#include <vector>

int main() {
  std::ios_base::sync_with_stdio(false);
  std::vector<TestClass> messages;
  for(long long i = 0; i < 100; i++){
    messages.push_back(TestClass(i, "test string 0",
				"test string 1",
				"test string 2",
				"test string 3",
				"test string 4",
				"test string 5",
				"test string 6",
				"test string 7",
				"test string 8",
				"test string 9" ));
  }

  for(TestClass &t: messages) std::cout << t << '\n';

  TestClass2 t2("test string 0", "test private string 0");
  std::cout << t2;
}

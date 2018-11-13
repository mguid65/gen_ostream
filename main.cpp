#include "test_refl.h"
#include <iostream>

int main() {
  TestClass t(123, "test1", "test2", 12345678910);
  std::cout << t;
}

#include "test_message.h"
#include <iostream>

int main() {
  TestMessage t("0000000000000001", 1542213246, "127.0.0.1", "127.0.0.1", "Test Content");
  std::cout << t;
}

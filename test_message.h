#include <string>

#parse_class
class TestMessage {
public:
  TestMessage() {}
  TestMessage(std::string messageID, long long ISODate,
              std::string source, std::string dest,
              std::string content) :
              messageID(messageID), ISODate(ISODate),
              source(source), dest(dest), content(content) {}
#parse_var
  std::string messageID;
#parse_var
  long long ISODate;
#parse_var
  std::string source;
#parse_var
  std::string dest;
#parse_var
  std::string content;

#class_printer
};
#parse_end

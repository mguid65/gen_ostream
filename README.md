# Gen Ostream <<

This is an experiment to auto generate ostream& operator<< friend function 
to print out class members


\#parse_class                 add before class definition  
\#parse_var                   add before variables you want to know about  
\#class_printer               this will be replaced with a friend function declaration  
\#parse_end                   end of parse block, if \#class_printer specified,  
                              this will be replaced with an ostream& operator<< overload  

# Reflectify

This is an experiment to auto generate ostream& operator<< friend function 
to print out class members


\#reflect_class                 add before class definition
\#reflect_var                   add before variables you want to know about
\#class_printer                 this will be replaced with a friend function declaration
\#reflect_end                   end of reflection block, if \#class_printer specified,
                                this will be replaced with an ostream& operator<< overload

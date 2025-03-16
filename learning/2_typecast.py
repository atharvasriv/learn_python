# type() --> gives the datatype of a var
# str, int, float, bool

var_1 = "variable"
type(var_1) # doesn't give any output
print(type(var_1)) # prints the type to the console
# output --> <class '{datatype}'>


# typecasting --> changing one datatype to another
# str(), int(), float(), bool()

# for example, float --> int
val1 = 4.7
val2 = int(val1)
print(val2) # output will be integer part of the float, i.e., 4

# string --> bool
name = "<name>"
bool1 = bool(name)
print(bool1) # output - true, as string != empty
_name = ""
bool2 = bool(_name)
print(bool2) # output - false, as string == empty
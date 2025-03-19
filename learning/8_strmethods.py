# for a complete list of string methods, run
# print(help(str))

# len(x) - length of string
# x.find('n') - location of first occurence of n in x
# x.rfind('n') - location of last occurence of n in x
# x.capitalize() - capitalize the first letter of the string
# x.upper() - convert all letters into uppercase
# x.lower() - convert all letters into lowercase
# x.isdigit() - check whether string is made up completely from digits
#               boolean value
# x.isalpha() - check whether string is made up completely from alphabe-
#               ts, boolean value
# x.count("n") - counts the number of occurence of n in x
# x.replace("n", "u") - replaces n with u

x = "string"

print(len(x))
print(x.find('r'))
print(x.rfind('r'))
print(x.capitalize())
print(x.upper())
print(x.lower())
print(x.isdigit())
print(x.isalpha())
print(x.replace('i', 'u'))

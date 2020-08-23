a="nithin Sallagonda Reddy"
# More specifically, make the first character
# have upper case and the rest lower case.
capitalizeName = a.capitalize()
upperMyName = a.upper()

# str.replace(old, new, count) -> str
replaced= a.replace("a","b",2)

# Return a version of the string suitable 
# for caseless comparisons.
casefold=a.casefold()

# center(width, fillchar) -> str
# Return a centered string of length width.
# Padding is done using the specified fill 
# character (default is a space).
center= a.center(40,"N")

# str.encode(encoding, errors)
# Encode the string using the codec registered 
# for encoding.
# encoding The encoding in which to encode the string. 
# errors The error handling scheme to use for encoding 
# errors. The default is 'strict' meaning that encoding
#  errors raise a UnicodeEncodeError. Other possible 
# values are 'ignore', 'replace' and 'xmlcharrefreplace'
#  as well as any other name registered with 
# codecs.register_error that can handle 
# UnicodeEncodeErrors.
encode= a.encode()

# str.endswith(suffix, start=0, end=-1)
# S.endswith(suffix[, start[, end]]) -> bool
# ends= a.endswith("reddy")
ends= a.endswith("Reddy")

# Return a copy where all tab characters are expanded 
# using spaces.
# If tabsize is not given, a tab size of 8 
# characters is assumed.
tabspace= a.expandtabs()

# S.find(sub[, start[, end]]) -> int
find = a.find("i",0 , 13)

# format(*args, **kwargs) -> str

# S.format_map(mapping) -> str

# Return a formatted version of S, using substitutions 
# from mapping. The substitutions are identified by 
# braces ('{' and '}').

# S.index(sub[, start[, end]]) -> int
indx= a.index("n",0,10)

# Return True if the string is an 
# alpha-numeric string, False otherwise.
alphanumeric = a.isalnum()

# Return True if the string is an 
# alphabetic string, False otherwise.
a.isalpha()

# Return True if all characters in the 
# string are ASCII, False otherwise.
ascii = a.isascii()

space= a.isspace()
upper= a.isupper()

# Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
joi = a.join('b,c')

# str.ljust(width, fillchar) -> str
just = a.ljust(40,"k")
ju =  a.rjust(50,"t")

# Return a copy of the string with leading 
# whitespace removed.
lsrip = a.lstrip()

# str.maketrans(x, y, z) -> dict
# Return a translation table usable for str.translate().

# If there is only one argument, it must be a dictionary
#  mapping Unicode ordinals (integers) or characters to 
# Unicode ordinals, strings or None. Character keys will 
# be then converted to ordinals. If there are two arguments,
#  they must be strings of equal length, and in the 
# resulting dictionary, each character in x will be 
# mapped to the character at the same position in y. If
#  there is a third argument, it must be a string, whose 
# characters will be mapped to None in the result.
trans = a.maketrans("nat" , "nit")


partition = a.rpartition("Red")

rfin = a.rfind("n", 0 ,10)

split = a.rsplit("de")


# Return a list of the lines in the string, 
# breaking at line boundaries.
# Line breaks are not included in the resulting list
#  unless keepends is given and true.
splitlin = a.splitlines(True)

ss = a.startswith("s", 0, 10)

# Convert uppercase characters to 
# lowercase and lowercase characters to uppercase.
a.swapcase()

# Return a version of the 
# string where each word is titlecased.
tit = a.title()

# Pad a numeric string with zeros on the left, to 
# fill a field of the given width
fill = a.zfill(40)

# str.__add__(value) -> str
add = a.__add__

# str.__init__(bytes_or_buffer, encoding=None, errors=None)
a.__init__


print(add)
print(capitalizeName)
print(center)
print(upperMyName)
print(replaced)
print(casefold)
print(encode)
print(ends)
print(tabspace)
print(find)
print("My name is :{} ".format(a))
print(indx)
print(alphanumeric)
print(ascii)
print(space)
print(upper)

print(joi)
print(just)
print(ju)
print(lsrip)
print(trans)
print(partition)
print(rfin)
print(split)
print(splitlin)
print(ss)
print(tit)
print(fill)
print(trans)
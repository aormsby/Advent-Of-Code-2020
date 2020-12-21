import re
import regex

x1 = 'AAAZZZ'
# print(re.match(r'A(?R)?Z', x1))
print(regex.match(r'A(?R)?Z', x1))
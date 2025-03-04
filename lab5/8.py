import re

txt = "ChaseAtlantic MacDemarco TestingRegex"
print(re.findall(r'[A-Z][a-z]*', txt))  
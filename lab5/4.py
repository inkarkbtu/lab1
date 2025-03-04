import re

txt = "Alice met Bob at the Market on Friday"
print(re.findall(r'[A-Z][a-z]+', txt)) 
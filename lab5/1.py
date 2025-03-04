import re

txt = "ab a abbb aabb abb"
print(re.findall(r'ab*', txt))  
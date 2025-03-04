import re

txt = "apple banana acb aaaab axyzb ab"
print(re.findall(r'\ba+b\b', txt))  
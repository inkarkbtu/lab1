import re

txt = "abb abbb abbbb aab abbba"
print(re.findall(r'ab{2,3}', txt))  
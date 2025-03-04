import re

txt = "my_variable test_value another_one not_thisOne"
print(re.findall(r'\b[a-z]+_[a-z]+\b', txt))  
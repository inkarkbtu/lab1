import re

txt = "hello_world study_group twinkling_watermelon"
camel_case_list = [re.sub(r'_([a-z])', lambda m: m.group(1).upper(), word).capitalize() for word in txt.split()]
print(" ".join(camel_case_list))  
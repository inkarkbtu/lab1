import re

txt = "Hi, my name is Woo Min. How are you; today?"
print(re.sub(r"[\s,.;]", ":", txt))  
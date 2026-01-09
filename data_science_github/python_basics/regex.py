# Regex(Regular Expression)
# Pattern Matching

import re
text = "My name is Shubham."
word = "Shubham"

print(re.search(word, text))
print(bool(re.search(word, text)))

# Example 2
text_2 = "Shubham"
word_2 = "Shubham"

print(re.match(word_2, text_2))

# Example 3
text_3 = "Orders 3, 4 ,5 and 98 are shipped together."
text_4 = " My phone number is 8208411933."

print(re.findall(r"\d", text_3)) # d as in digits, check the last number.
print(re.findall(r"\d+", text_4)) # + indicates continuous values.

# Example 4
text_5 = "My email id is masalsam99@gmail.com."
pattern = r"\b[\w.$+-]+@[\w.-]+\.[a-zA-Z.-]{2,}\b"

print(re.findall(pattern, text_5))
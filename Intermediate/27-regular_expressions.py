#=======================
#   Regular Expressions
#=======================
 # Regular expressions are patterns used to match text.
 # Python uses the `re` module for regex operations.

import re

text = "My email is prince@example.com and my phone is 123-456-7890."

# Search for a pattern
email_pattern = r"[\w.+-]+@[\w-]+\.[\w.-]+"
email_match = re.search(email_pattern, text)
if email_match:
    print("Email found:", email_match.group())

# Find all matches
phone_pattern = r"\d{3}-\d{3}-\d{4}"
phones = re.findall(phone_pattern, text)
print("Phone numbers:", phones)

# Replace text using sub()
masked_text = re.sub(phone_pattern, "XXX-XXX-XXXX", text)
print(masked_text)

# Split text using regex
words = re.split(r"\s+", text)
print(words)

# Validate a simple pattern
if re.match(r"^My\b", text):
    print("Text starts with 'My'")

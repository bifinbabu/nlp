import re
import get_pattern_match

chat1 = "codebasics: You ask a lot of questions, 1234567890, abc@xyz.com"
chat2 = "codebasics: here it is: (123)-567-7777, abc_ss@xyz.com"
chat3 = "codebasics: yes phone: 8075739957, email: abc@xyz.com"

chat4 = "codebasics: Hello, I am having an issue with my order # 12345678"
chat5 = "codebasics: Hello, I have a problem with my order number 12345678"
chat4 = "codebasics: My order 12345678 is having an issue, I was charged 300$ when online it said 280$"

# pattern = r"\d{10}|\(\d{3}\)-\d{3}-\d{4}"
# pattern = r"[a-z0-9A-Z_]*@[a-z0-9A-Z]*\.[a-zA-Z]*"
pattern = r"order[^\d]*(\d*)"

matches = re.findall(pattern, chat4)

print(matches)

print(get_pattern_match.get_pattern_match(pattern, chat5))

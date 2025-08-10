name = input("Enter your name: ")

print(f"Good Afternoon {name}")



letter = """ Dear <|Name|>,
 You are selected!
 <|Date|>"""

print(letter.replace("<|Name|>", "Mahesh").replace("<|Date|>", "12/08/2025"))



str = "Hello good  night"

print(str.replace("  ", " "))
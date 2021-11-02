# # Lesson #7 - Strings functions 2

# #Warm-up
# # Modulus % - is remainder of a division 
# # 7 % 3 = 1
# print(8 % 3) # 2
# print(9 % 7)  # 2
# print(8 % 4)  # 0

# print(2 % 3)  # 2
# print(7 % 8)  # 7
# print(100 % 101)  # 100 

# print(1 % 2)  # 1
# print(2 % 2)  # 0 
# print(3 % 2)  # 1
# print(4 % 2)  # 0
# print(5 % 2)  # 1

# # abs() - absolute value 
# print(abs(-3))  # 3
# print(abs(-6.7)) # 6.7

# # ** - exponential 
# print(2**3)  # 8
# print(3**2)  # 9
# import math 
# print(math.pow(2, 3))  # 8.0 
# print(math.pow(3, 2))  # 9.0 

# # * for string "multiplication"
# print("Spam" * 3)
# print("hello " * 4)

# Today's Lesson - String functions 2 
# startswith() - checks if a string starts with a certain substring 
s = "hello"
print(s.startswith("h"))  # True
print(s.startswith("he")) # True 
print(s.startswith("k"))  # False 
print(s.startswith("H"))  # False
print("hello".startswith("hell"))  # True

# endswith() - checks if a string ends with a certain substring

print(s.endswith("o"))  # True 
print(s.endswith("lo")) # True 
print(s.endswith("ol"))  # False 
print(s.endswith("hello"))  # True 

# find() 
print(s.find("h"))  # 0
print(s.find("e"))  # 1
print(s.find("l"))  # 2
print(s.find("o"))  # 4
print(s.find("k"))  # -1 
print(s.find("hel")) # 0
print(s.find("ello"))  # 1
s = '"hello"'
print(s.find("h"))

# replace(old, new) - finds and replace characters 
s = "hello"
print(s.replace("h", "j")) # jello
print(s.replace("h", "b"))
print(s.replace("h", "f"))

s = "python"
# convert python to pyjamas 

print(s.replace("thon", "jamas"))














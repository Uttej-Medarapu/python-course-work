str1 = "Hello"
str2 = "World"
# concatination
concatenated = str1 + " " + str2
print("Concatenation: " + concatenated)
#repetition
repeated = str1 * 3
print("Repetition: " + repeated)
#indexing
first_char = str1[0]
last_char = str2[-1]
print(f"Indexing: First character of str1: {first_char}, Last character of str2: {last_char}")
#slicing
sliced_str1 = str1[1:4]
sliced_str2 = str2[:3]
print(f"Slicing: str1[1:4]: {sliced_str1}, str2[:3]: {sliced_str2}")
#using membership operator
is_hello_in = "Hello" in str1
is_world_in = "World" not in str1
print(f"Membership:{is_hello_in}")
a='python'
print(a.center(50, "*") )

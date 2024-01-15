# This is a script for converting Japanese keyboard to US keyboard.

convert_dict = {"\"": "@", "&": "^", "'": "&", "(": "*", ")": "(", "=": "_", 
        "~": "+", "^": "=", "|": "}", "\\": "/", "`": "{", "@": "]", "{": "}", "[": "]",
        "+": ":", "*": "\"", ":": "'", "}": "|", "]": "\\"}
string = input("Type your string: ")
replaced = []
for s in string:
  try:
    s = convert_dict[s]
  except:
    s = s 
  replaced.append(s)
result = ''.join(map(str, replaced))
print(result)

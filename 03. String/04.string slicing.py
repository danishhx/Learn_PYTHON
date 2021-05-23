mystr = "I am a string"
print(len(mystr))  # 13
print(mystr[0])  # 'I'
print(mystr[1])  # ' '  blank space
print(mystr[0:len(mystr)])  # full string
print(mystr[:])  # here python automatically assigns 0 and
                 # value of length of string
print(mystr[-2:-1])  # 'n'
print(mystr[-14:-1])  # full string excluding 'g'
print(mystr[:100])  # full string (no errors)

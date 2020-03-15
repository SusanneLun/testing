
prompt = "Write your word here:"
word = (input(prompt))

list1 = ["a", "o", "e", "i", "u", "y"]
list2 = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "w", "z" ]
list3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


if word[0] in list1 : 
    print("vowel")
elif word[0] in list2 :
    print("consonant")
elif word[0] in list3 :
   print("number")
else:
    print("unknown")
        
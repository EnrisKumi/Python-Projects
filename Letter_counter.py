String = "London is the one of the most beautiful citties in the world"

frequency = dict()

for ch in String:
    if ch in frequency:

        frequency[ch]+=1
    else:
        frequency[ch] = 1

for letter,count in frequency.items():
    print(letter," : ",count)


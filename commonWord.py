counts = dict()
print("Enter a line :  ")
line = input('')
words = line.split()
print(words)
for word in words:
    counts[word] = counts.get(word,0)+1
print('Counting...........')
print('Count : ',counts)

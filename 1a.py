text= input("Enter a paragraph:")
words=text.split()
print("Length of words=",len(words))
longest=max(words,key=len)
print("Longest word:",longest)
count=0
for ch in text:
    if ch=="?" or ch=="." or ch=="!":
        count+=1
print("number of sentence=",count)
print("Words frequency")
for w in words:
    print(f"{w} : {words.count(w)}")
        


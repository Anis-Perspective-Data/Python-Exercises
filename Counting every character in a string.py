string = "vinithavinnu"
dict = {}
for ele in string:
    if(ele in dict):
        dict[ele]+=1
    else:
        dict[ele]=1
print(dict)
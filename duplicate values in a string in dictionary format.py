data = '34631'
duplicate={}
for i in data:
    if i in duplicate:
        duplicate[i]+=1
    else:
         duplicate[i]=1
print(duplicate)
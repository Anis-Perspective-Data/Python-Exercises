def sum(my_dict):
    sum=0
    for i in my_dict.values():
        sum=sum+i
    return sum
dict={'a':2,'b':3,'c':4}
print(sum(dict))
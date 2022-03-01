def sample(list):
    return [set(i for i in list if list.count(i)>1)]

print(sample([1,2,1,3,2,4,5,3,7,8]))

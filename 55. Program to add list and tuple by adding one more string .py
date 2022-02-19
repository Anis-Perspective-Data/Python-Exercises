def a(list1,list2):
	return list1+list2
my_list1=[1,2,3,4]
my_list2=[5,6,7,8]
updated_list=map(a,my_list1,my_list2)
print(updated_list)
print(tuple(updated_list))
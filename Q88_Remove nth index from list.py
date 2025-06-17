def remove_list_from_index(lst,n):
    del lst[n]
    return print('new list is',lst)
list = [1,2,3,4,5,5,6,7,8]
n = int(input(f"Enter the index you want to remove from your list - {list}: "))
remove_list_from_index(list,n)

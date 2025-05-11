"""
Name: Adi Pedel
Project: mmn14 contains:
1.find_max - receives a list of numbers that was sorted in ascending order and was being shifted right k times.
2.find_pairs - receives a list sorted in ascending order (lst) and a positive number k and returns the number of pairs that their difference is k.
"""

"""
find_max is a function that receives a list (lst) and returns maximum value in the list. The list was initially sorted in
ascending order but has been shifted to the right by k positions (k is ot negative and is smaller than the list length). 
To find the maximum value the function will check the relations between three items - the first on the list, the last
on the list, and the one in the middle. 
if lst[first]<lst[middle]<lst[last] than lst[last] is the maximum value. and we will return it.
if lst[first]>lst[last]>lst[middle],the maximum value is between lst[first] and lst[middle] and to continue searching 
for the maximum value we will call the function with the chopped list (lst[first:middle]).
else (lst[first]<lst[middle] and lst[middle]>lst[last]), the maximum value is between lst[middle] and lst[last] and to
continue searching for the maximum value we will call the function with the chopped list (lst[middle:last]).
The function will call herself until it will find the maximum value (recursion). 
Because each function call reduces the list size by half, the running time is logarithmic.
"""
def find_max(lst):
    if len(lst)==1:
        return lst[0]
    if len(lst) == 2:
        if lst[0]<lst[1]:
            return lst[1]
        else:
            return lst[0]
    first_item = lst[0]
    middle_item = lst[len(lst) // 2]
    last_item = lst[len(lst)-1]
    if first_item<middle_item<last_item:
        return last_item
    elif first_item>last_item>middle_item:
        return find_max(lst[0:len(lst) // 2])
    else:
        return find_max(lst[len(lst)//2:len(lst)-1])

"""
find_pairs is a function that receives a list sorted in ascending order (lst) and a positive number k. 
the function returns the number of pairs that their difference is k.
"""
def find_pairs(lst,k):
    count = 0
    i = 0
    j = 1
    while i<len(lst)-2:
        if j==len(lst)-1 and lst[j] - lst[i] < k:
            break
        if lst[j]-lst[i] == k:
            count += 1
            if j < len(lst)-1:
                i += 1
                j += 1
        elif lst[j]-lst[i] > k:
            if j-i > 1:
                i += 1
            elif j < len(lst)-1:
                i += 1
                j += 1
        elif lst[j] - lst[i] < k and j < len(lst)-1:
            j+=1
    return count

"""
update_list is a function that receives a list of numbers and a value. It will return the list without the
given value using recursion. If the value appears in the list more than once, only the first item with that value will be
removed from the list.
"""
def update_list(lst,value):
    if lst[0] == value:
        if len(lst) == 1:
            return []
        else:
            return lst[1::]
    elif len(lst) == 1:
        return [lst[0]]
    else:
        return [lst[0]]+update_list(lst[1::], value)
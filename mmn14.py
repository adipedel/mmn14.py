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
    if len(lst) == 0:
        return None
    if len(lst) == 1:
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
    if len(lst) == 0:
        return []
    if lst[0] == value:     #the value we want to remove is in the start of the list
        if len(lst) == 1:
            return []   #if it's the last item in the list, we will return an empty list
        else:
            return lst[1::] #it's not the end of the list, removing the item by returning the list starting the next item
    elif len(lst) == 1:     #if it's the last item of the list, and it's not the value, returning the list
        return [lst[0]]
    else:
        return [lst[0]]+update_list(lst[1::], value)
#calling the function with the list starting with the next item to check if the value is in there, and returning the resulted list

"""
equal_lists is a function that receives two list of numbers. The function will return True if the lists
are equal in their size and values(not in order). The function will use the function update_list, to take
out a value from the two list recursively until one of the lists is empty. If the two list remains equal
in size each call, they meet the conditions and the function will return True.
"""
def equal_lists(lst1, lst2):
    if lst1 == lst2 == []:  #if the two lists are empty, they are equal and the function returns True
        return True
    elif len(lst1) != len(lst2):    #the lists are not equal in size, the function returns False
        return False
    else:
        value = lst1[0]         #the value we will try to remove from the list
        lst1 = update_list(lst1, value)     #calling the function to remove the value and updating the new lists
        lst2 = update_list(lst2, value)
        result = equal_lists(lst1, lst2)    #calling the function again with the updated lists
        return result


"""
is_palindrome is a function that receives a list of strings and return true if each list is a palindrome
and together they formed a palindrome. the function does it with recursion,it compares the string
in the beginning and in the end of the list, and if the chars in the begging and end of each string are the
same it trims them and with recursion continue to compare them until the strings are empty. the  function
continues too checks every string until it detect a string that isn't a palindrome or doesnt create a
palindrome in thr whole list or if the list is empty.

"""
def is_palindrome(lst):
    if len(lst) == 0:
        return True
    if len(lst) == 1 :
        if len(lst[0]) == 1:
            return True
        if len(lst[0]) == 2:
            if lst[0][0] == lst[0][-1]:
                return True
            else:
                return False
        else:
            if lst[0][0] == lst[0][-1]:
                lst[0] = lst[0][1:-1]
                if is_palindrome(lst):
                    return True
                else:
                    return False
            else:
                return False
    else:
        if len(lst[0]) != len(lst[-1]):
            return False
        if len(lst[0]) == 0 or  len(lst[0]) == 1:
            lst = lst[1:-1]
            if is_palindrome(lst):
                return True
            else:
                return False
        if lst[0][0] == lst[0][-1] == lst[-1][0] == lst[-1][-1]:
            if len(lst[0]) == 2:
                lst = lst[1:-1]
                if is_palindrome(lst):
                    return True
                else:
                    return False
            else:
                lst[0], lst[-1] = lst[0][1:-1], lst[-1][1:-1]
                if is_palindrome(lst):
                    return True
                else:
                    return False
        else:
            return False

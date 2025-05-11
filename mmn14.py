"""
Name: Adi Pedel
Project: mmn14 contains:
1.find_max - receives a list of numbers that was sorted in ascending order and was being shifted right k times.
2.find_pairs - receives a list sorted in ascending order (lst) and a positive number k and returns the number of pairs that their difference is k.
3.update_list - receives a list of numbers and a value, and returns the list without the value.
4.qual_lists - receives two list of numbers, and checks if the lists are equal in their size and values(not in order)
5.is_palindrome - receives a list of strings and return true if each list is a palindrome and together they formed a palindrome.
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
    if first_item<middle_item<last_item:        #maximum value has to be the last item
        return last_item
    elif first_item>last_item>middle_item:      #maximun value has to be in the first half, sending it to the function
        return find_max(lst[0:len(lst) // 2])
    else:
        return find_max(lst[len(lst)//2:len(lst)-1])        #maximun value has to be in the second half, sending it to the function

"""
find_pairs is a function that receives a list sorted in ascending order (lst) and a positive number k. 
the function returns the number of pairs that their difference is k.
the function does it with by comparing 2 items (a,b) in the list. if their difference is less than k, than we need
to take a bigger number than b for a chance of finding numbers with k difference. but if their difference is
bigger than k,  than we need to take a bigger number than a for a chance of finding numbers with k difference.
(unless a and b are consecutive numbers, and we will have to change both of them)
"""
def find_pairs(lst,k):
    count = 0
    i = 0
    j = 1
    while i<len(lst)-2:
        if j==len(lst)-1 and lst[j] - lst[i] < k:   #no more numbers in the list to compare
            break
        if lst[j]-lst[i] == k:      #we have found 2 numbers with k difference
            count += 1              #the number of pairs with k difference
            if j < len(lst)-1:      #ncreasing both numbers
                i += 1
                j += 1
        elif lst[j]-lst[i] > k:
            if j-i > 1:         #not consecutive numbers
                i += 1
            elif j < len(lst)-1:    #consecutive numbers
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
    if len(lst) == 0:           #list is empty, it's a palindrome
        return True
    if len(lst) == 1 :          #list contains 1 string
        if len(lst[0]) == 1:        #string is 1 char, it's a palindrome
            return True
        if len(lst[0]) == 2:
            if lst[0][0] == lst[0][-1]:         #string is 2 equal chars, it's a palindrome
                return True
            else:                           #string is 2 unequal chars, it's not a palindrome
                return False
        else:                        #string is longer than 2 chars
            if lst[0][0] == lst[0][-1]:        #chars in the beginning and end of the string are equal
                lst[0] = lst[0][1:-1]          #trimming the string to check if the middle is a palindrome
                if is_palindrome(lst):          #sending the list with the updated string to the function
                    return True
                else:                   #the middle of the string is not a palindrome
                    return False
            else:            #chars in the beginning and end of the string are not equal, not a palindrome
                return False
    else:                        #list contains at list 2 strings
        if len(lst[0]) != len(lst[-1]):   #strings in the beginning and end of the list are not equal, not a palindrome
            return False
        if len(lst[0]) == 0 or len(lst[0]) == 1:        #string length is 0 or 1
            if len(lst[0]) == 1 and  lst[0][0] != lst[1][0]:
                return False     #string length is 1 and the chars are not equal, not palindorme
            lst = lst[1:-1]        #trimming the list, to check if the strings in the middle are palindromes
            if is_palindrome(lst):      #sending the list with the updated string to the function
                return True
            else:
                return False
        if lst[0][0] == lst[0][-1] == lst[-1][0] == lst[-1][-1]:        #the chars in the beginning and end are equal
            if len(lst[0]) == 2:         #string length is 2
                lst = lst[1:-1]          #trimming the list, to check if the strings in the middle are palindromes
                if is_palindrome(lst):
                    return True
                else:
                    return False
            else:               #string length is bigger than 2
                lst[0], lst[-1] = lst[0][1:-1], lst[-1][1:-1] #trimming the strings, to check if the middle is palindrome
                if is_palindrome(lst):
                    return True
                else:
                    return False
        else:
            return False

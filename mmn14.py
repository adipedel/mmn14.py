"""
Name: Adi Pedel
Project: mmn14 contains:
1.find_max - receives a list of numbers that was sorted in ascending order and was being shifted right k times.
2.find_pairs - receives a list sorted in ascending order (lst) and a positive number k and returns the number of pairs that their difference is k.
3.update_list - receives a list of numbers and a value, and returns the list without the value.
4.qual_lists - receives two list of numbers, and checks if the lists are equal in their size and values(not in order)
5.is_palindrome - receives a list of strings and return true if each list is a palindrome and together they formed a palindrome.
"""

def find_max(lst):
    """
        Finds the maximum value in a list that has been sorted in ascending order
        and then rotated (shifted) to the right by k positions.

        The function uses a recursive binary search approach to identify the maximum value.
        It compares the first, middle, and last elements of the list in each recursive call
        and determines in which half the maximum resides.

        Conditions:
        - If lst[first] < lst[middle] < lst[last], then the list is strictly increasing and
          the last item is the maximum.
        - If lst[first] > lst[last] > lst[middle], the maximum lies in the first half.
        - Else (lst[first] < lst[middle] and lst[middle] > lst[last]), the maximum lies in the second half.

        The function keeps halving the list until the maximum is found.
        Since each call reduces the size by half, the time complexity is logarithmic (O(log n)).

        Args:
            lst (list): A list of numbers that has been rotated to the right. Must not be empty.

        Returns:
            The maximum value in the rotated list, or None if the list is empty.
        """
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


def find_pairs(lst,k):
    """
        Counts the number of unique pairs in a sorted list where the difference
        between the elements in each pair is exactly k.

        The function uses a two-pointer approach to efficiently scan through the list.
        It compares two elements (a, b) where b is ahead of a:

        - If the difference (b - a) is less than k, it advances b to increase the difference.
        - If the difference is greater than k, it advances a to decrease the difference.
        - If the difference is exactly k, it increments the count and moves both pointers forward.

        The input list must be sorted in ascending order, and k must be a positive integer.

        Args:
            lst (list): A list of integers sorted in ascending order.
            k (int): The target positive difference.

        Returns:
            int: The number of unique pairs with a difference of exactly k.
        """
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


def update_list(lst,value):
    """
        Recursively removes the first occurrence of a given value from a list.

        The function traverses the list using recursion and returns a new list
        that excludes the first element equal to the specified value. If the value
        does not exist in the list, the original list is returned unchanged.

        If the list is empty, an empty list is returned.

        Args:
            lst (list): A list of numbers.
            value: The value to remove from the list.

        Returns:
            list: A new list with the first occurrence of the value removed.
        """
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


def equal_lists(lst1, lst2):
    """
       Recursively checks if two lists contain the same elements, regardless of order.

       The function compares two lists of numbers and returns True if:
       - They are the same length.
       - They contain the same values (regardless of order).

       It uses the `update_list` function to remove matching values from both lists
       recursively. If both lists are reduced to empty at the same pace, the lists
       are considered equal in content.

       Args:
           lst1 (list): The first list of numbers.
           lst2 (list): The second list of numbers.

       Returns:
           bool: True if both lists contain the same values and are the same length, False otherwise.
       """
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


def is_palindrome(lst):
    """
        Checks whether a list of strings forms a palindrome structure both individually and collectively.

        A list is considered a valid palindrome if:
        1. Each string in the list is a palindrome (reads the same forwards and backwards).
        2. The entire sequence of strings also forms a palindrome (i.e., first string equals last, second equals second-last, etc.).

        The function uses recursion to:
        - Compare characters at the beginning and end of each string.
        - Trim matching characters from both ends.
        - Compare strings from both ends of the list to see if they mirror each other.

        It continues until all strings are reduced to empty or one character, or until a mismatch is found.

        Args:
            lst (list): A list of strings.

        Returns:
            bool: True if each string is a palindrome and the overall list is also a palindrome; False otherwise.
        """
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

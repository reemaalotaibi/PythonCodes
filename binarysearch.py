###Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
###For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#define a list of numbers
#prompt the user to choose k
#iterate over the list by adding the numbers
#check if the numbers sum up to k


def find_sum(arr, target):
    arr_len=len(arr)
    for num1 in range (arr_len - 1):
        for num2 in range (num1+1, arr_len):
            if (arr[num1] + arr[num2]) == target:
               storage_one = arr[num1]
               storage_two = arr[num2]
               print('match found: ' + str(storage_one) + ' + ' + str(storage_two) + ' = ' + str(target))
               return True
    else:
        print('no pairs found')
                 
     
num_list = [10, 15, 3, 7]
number = 17  
find_sum(num_list, number)





      
    

    

         
    


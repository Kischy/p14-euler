# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:51:37 2019

@author: kisch
"""

def is_even(number):
    return (number % 2) == 0

def get_next_collatz_number(number):
    if(is_even(number)):
        return number//2 
    else:
        return 3*number + 1          
            
        
    
def len_of_collatz_sequence(number):
    length = 1 
    
    while(number != 1):
        number = get_next_collatz_number(number)
        length += 1
        
    return length


def get_starting_number_with_longest_sequence(max_starting_num):
    curr_length = 0
    start_num = 0
    
    for i in range(1,max_starting_num):
        tmp = len_of_collatz_sequence(i)
        
        if(tmp > curr_length):
            curr_length = tmp
            start_num = i       
 
    return start_num
    
        
        
    
    
    




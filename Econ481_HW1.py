#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Econ 481 HW1
#Yuzhi Fu


# In[ ]:


def github() -> str:
    return 


# In[1]:


#Exercise 2
def evens_and_odds(n: int) -> dict:
    evens_sum=0
    odds_sum=0
    """Make for loops to get the sum of even numbers and odd numbers separately"""
    for num in range(0,n):
        if num%2==0:
            evens_sum += num
        else:
            odds_sum+=num
            """if/else"""
    return{"evens": evens_sum, "odds": odds_sum}
print(evens_and_odds(4)) 


# In[2]:


#Exercise 3
from typing import Union
from datetime import datetime
def time_diff(date_1: str, date_2: str, out: 'float')-> Union[str,float]:
    date_1 = datetime.strptime(date_1, '%Y-%m-%d')
    date_2 = datetime.strptime(date_2, '%Y-%m-%d')
    """define datetime1 and datetime 2 and their format"""
    if out=="string":
        t_diff=(abs(date_2-date_1).days)
        """absoluste value function"""
        return f"There are {t_diff} days between the two dates."
        print(f"There are {t_diff} days between the two dates.")
    else:
        t_diff=(abs(date_2-date_1).days)
        return t_diff

print(time_diff('2024-04-03', '2024-04-05', 'float'))
print(time_diff('2024-04-03', '2024-04-05', 'string'))



# In[129]:


#Exercise 4
in_list=['a', 'b', 'c']
"""First define the in_list"""

def reverse(in_list: list) -> list:
    reversed_list=in_list[::-1]
    return reversed_list

print(reverse(in_list))


# In[3]:


#Excercise 5
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
        """n is a non-negative integeral"""

def prob_k_heads(n: int, k: int) -> float:
    if n < k:
        raise ValueError("n must be greater or equal than k")
        
    """Calculate binomial coefficient using factorial"""
    binomial_coefficient = factorial(n) // (factorial(k) * factorial(n - k))
    """probability of getting k heads"""
    probability_heads = (1/2) ** k
    """Calculate probability of getting (n-k) tails"""
    probability_tails = (1 - (1/2)) ** (n - k)
    total_probability = binomial_coefficient * probability_heads * probability_tails

    return total_probability

print(prob_k_heads(1, 1)) 
    


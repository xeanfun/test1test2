#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Exercise : Using only one print() method, try to display two or more lines.

print('asdas \ndasdas')


# In[10]:


#Exercise : Try to find a way to raise one number to the power of another

a = int(input('Enter the first number:'))
b = int(input ('Enter the second number:'))

c = pow(a,b)
print(c) 


# In[5]:


help(pow)


# In[13]:


#NumPy Example

import numpy as np
nparray = np.zeros((5,5))
print(nparray)


# In[18]:


#Exercise : Try to find the mean of all the numbers in the L4 list.
L4 = [[2, 9, -5], [-1, 0, 4], [3, 1, 2]]

import numpy as np
npmean = np.mean(L4)
print(npmean)


# In[22]:


#Exercise : Build a condition that will check if a number is divisible by 3 or not.

a = int(input('Enter a number to see if its divisible by 3 or not:'))

if a%3==0:
    print(a , 'is divisible by 3!')
else:
    print(a , 'is not divisible by 3!')


# In[36]:


#Exercise : Build both for and while loops that can calculate the factorial of a positive integer variable

#for loops

n = int(input('Enter a number to find out its factorial:'))
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)


# In[35]:


#while loops

n = int(input('Enter a number to find out its factorial:'))
fact = 1
a = 1
while a<=n: 
    fact *= a
    a += 1
print(fact)


# In[52]:


#Exercise : Build a function to calculate the distance between two points on an x,y plane: one with 
#coordinates x1 and y1, and the other with coordinates x2 and y2.
def distance(x1, x2, y1, y2):
    dist = pow(pow(x1-x2,2) + pow(y1-y2,2),0.5)
    return dist
z = distance(1,2,3,4)
print (z)


# In[54]:


#Example of class

class Bot():
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
    def move(self, speedx, speedy):
        self.posx += speedx
        self.posy += speedy


# In[55]:


bot = Bot(3,4)


# In[56]:


bot.move(2,-1)
print(bot.posx,bot.posy)


# In[57]:


# Exercise : 
# Your final challenge will be to build a very simple car class. As arguments, a car object
# should take the maximum velocity at which the car can move (unit in m/s), as well as 
# the acceleration at which the car is accelerating (unit in m/s2#). I also challenge you to 
# build a method that will calculate the time it will take for the car to accelerate from the 
# current speed to the maximum speed, knowing the acceleration (use the current speed 
# as the argument of this method).

class Car():
    def __init__(self, maxspeed, accel):
        self.maxspeed = maxspeed
        self.accel = accel
    def time(self, currentspeed):
        t = (self.maxspeed - currentspeed) / self.accel
        return t
    
car = Car(75,3.5)

time = car.time(30)
print(time)


# In[ ]:





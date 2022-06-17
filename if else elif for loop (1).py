#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if else elif 


# In[ ]:


if statement 


# In[ ]:


syntax: if # only for one condition
    if some_condition 
        #Execute some code


# In[ ]:


syntax: if__else #only for one condition only but for true or flase 
    if some_condition 
        #execute some code
    else: 
        #do something else


# In[ ]:


syntax: if_elif_else #for multiple condition to be passed
     if some_condition 
        #execute some code
    elif some_other_condition
        #do something different 
    else: 
        #do something else


# In[ ]:


boolean condition 


# In[4]:


a = True
if True:
    print('Its True!')


# In[7]:


if 3>2: #comparsion operator
    print('Its true')


# In[9]:


hungry = False
if hungry:
    print('FEED ME!')
else:
    print('Im not Hungry')
    


# In[13]:


loc = 'Dhruvil'
if loc == 'Auto Shop':
    print('cars')
elif loc == 'Bank':
    print('Money')
elif loc == 'Store':
    print('Welcome to store')
else:
    print('I dont know much')


# In[ ]:


For LOOP
 they are iterable (i.e. repeate)


# In[ ]:


Syntax:
    loop = [1,2,3]
    for item_name in loop
        print(item_name)


# In[15]:


mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)


# In[25]:


mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
        #check for even
    if num % 2 == 0:
        print(num)
    #else:
      #  print(f'odd number')


# In[26]:


mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
        #check for even
    if num % 2 == 0:
        print(num)
    else:
           print(f'odd number:{num}')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[67]:


from datetime import date

today = date.today()
today_year = today.year
today_year_int = int(today_year)

class AgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    pass


current_age = int(input('Enter current age: '))
name = input("Enter your name: ")

if current_age>99:
    raise AgeError("Already_100_Error")

print("Year when", name, "will become 100 years old:",today_year_int - current_age + 100)


# In[ ]:





# In[ ]:





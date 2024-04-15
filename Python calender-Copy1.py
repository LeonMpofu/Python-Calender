#!/usr/bin/env python
# coding: utf-8

# In[1]:


import calendar

def unique_calendar(year):
    cal = calendar.TextCalendar(calendar.SUNDAY)  # Create a TextCalendar instance
    for month in range(1, 13):  # Loop through each month
        month_calendar = cal.formatmonth(year, month)
        print(f"=== {calendar.month_name[month]} ===")
        print(month_calendar)

# Test the function
unique_calendar(2024)


# In[ ]:





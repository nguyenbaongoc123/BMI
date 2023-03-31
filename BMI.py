#!/usr/bin/env python
# coding: utf-8

# In[5]:


h= float(input('m'))
w= float(input('kg'))
BMI = w/(h**2)

if BMI > 40: 
            print('béo phì cấp độ III')
elif 35 <= BMI < 40: 
            print('béo phì cấp độ II')
elif 30 <= BMI < 35:
            print('béo phì cấp độ I')
elif 25 <= BMI < 30:
            print('thừa cân')
elif 18.5 <= BMI < 25: 
            print('bình thường')
elif 17 <= BMI < 18.5: 
            print('gầy cấp độ I')
elif 16 <= BMI < 17: 
            print('gầy cấp độ II')
else:  
            print('gầy cấp độ III')


# In[ ]:





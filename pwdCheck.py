
# coding: utf-8

# In[3]:


import re


# In[91]:


password = 'AZERCELL3'


# In[32]:


check1 = re.compile(r'''(
                        [a-zA-Z0-9]{9,}
                        )''', re.VERBOSE)


# In[9]:


check2 = re.compile(r'''(
                        [a-z]+
                        )''', re.VERBOSE)


# In[11]:


check3 = re.compile(r'''(
                        [A-Z]+
                        )''', re.VERBOSE)


# In[13]:


check4 = re.compile(r'''(
                        [0-9]+
                        )''', re.VERBOSE)


# In[89]:


def pwdCheck(text):
    if check1.search(text) != None:
        pass
    else:
        return 'Password must be at least 9 symbols!'
    if check2.search(text) != None:
        pass
    else:
        return 'Password must contain at least 1 lowercase letter!'
    if check3.search(text) != None:
        pass
    else:
        return 'Password must contain at least 1 UPPERCASE letter!'
    if check4.search(text) != None:
        pass
    else:
        return 'Password must contain at least 1 digit!'
    return 'Password is OK'


# In[92]:


pwdCheck(password)


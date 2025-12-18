#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.tokenize import word_tokenize


nltk.download('punkt')

sentence = "Natural Language Processing is interesting."
tokens = word_tokenize(sentence)

print(tokens)


# In[ ]:





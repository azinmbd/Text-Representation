#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# blue ones are inbuild nltk tasks
# function is like subrutine


# In[1]:


#chunk is sequance of words


# In[14]:


import nltk


# In[15]:


nltk.download('averaged_perceptron_tagger')


# In[9]:


setntence = [("the", "DT"), ("litte", "JJ"), ("yellow", "JJ"), ("dog", "NN"),("barked", "VBD"),("at", "IN"),("the", "DT"), ("cat", "NN")   ]


# In[10]:


grammar = "NP: {<DT>?<JJ>*<NN>}"


# In[11]:


cp = nltk.RegexpParser(grammar)


# In[12]:


result = cp.parse(setntence)


# In[13]:


print(result)


# In[14]:


result.draw()


# In[16]:


#chinking is for excluding the s part
#o 2 NP can overlap so by excluding the chunks(NP)


# In[20]:


# <DT>? optional DT
# <JJ.*> - . means one character like JJR,JJR
# <JJ.*> - . means 0 or more character JJRV, JJ
# <JJ.*>* 0 or more of these type od adj
# <NN.*>+ 1 or more noun
# considering all of the familie of jj and nn


# In[25]:


g2 = "NP: {<DT>?<JJ.*>*<NN.*>+}"


# In[26]:


doc2 = ["another", "sharp", "dive", "trade", "figures", "new", "policy", "measures", "earlier", "stages","Panamanian", "dictator", "Manuel", "Noriega"]


# In[30]:


tagged_doc = nltk.pos_tag(doc2)


# In[31]:


cp2 = nltk.RegexpParser(g2)


# In[32]:


res2 = cp2.parse(tagged_doc)


# In[33]:


print(res2)


# In[34]:


res2.draw()


# In[35]:


# pp$ special character o chapture the $ 
# propernouns are the name of a person
# 2 garammer in different lines ans user r""""""


# In[36]:


gram3 = r"""
 NP: {<DT|PP\$>?<JJ>*<NN>} # shunl determiner/possesive, adjectives and nouns 
 {<NP>+} # chunk sequences of proper nouns
"""


# In[37]:


cp = nltk.RegexpParser(gram3)


# In[39]:


sentence = [("Rapinzel", "NNP"),("let", "VBD"),("down", "RP"),("her", "PP$"),("long", "JJ"),("golden", "JJ"),("hair", "NN")]


# In[41]:


result3 = cp.parse(sentence)


# In[43]:


print(result3)


# In[44]:


result3.draw()


# In[53]:


nouns = [("money", "NN"),("market", "NN"),("funds", "NN")]


# In[61]:


grammer4 = "NP:{<NN>+}"


# In[62]:


cp = nltk.RegexpParser(grammer4)


# In[63]:


print(cp.parse(nouns))


# In[64]:


res1 = cp.parse(nouns)


# In[65]:


res1.draw()


# In[66]:


#chinking
# <.*>+ means all of them withut this chink <VBD|IN>


# In[81]:


grammar3  = r"""
 NP:
 {<.*>+} #chunk everthing
 }<VBD|IN>+{ #chink sequamces of vbd and in
"""


# In[82]:


sent4  = [("the", "DT"),("little", "JJ"),("yellow", "JJ"),("dog", "nn"),("barked", "VBD"),("at", "IN"),("the", "DT"),("cat", "NN")]


# In[83]:


cp = nltk.RegexpParser(grammar3)


# In[84]:


print(cp.parse(sent4))


# In[85]:


res5 = cp.parse(sent4)


# In[86]:


res5.draw()


# In[87]:


#convert IOB tag to tree


# In[90]:


text = '''
he PRP B-NP
accepted VBD B-VP
the DT B-NP
position NN I-NP
'''


# In[ ]:


nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw()


# In[1]:


# CoNLL-2000


# In[16]:


from nltk.corpus import conll2000
nltk.download('conll2000')


# In[17]:


print(conll2000.chunked_sents('train.txt')[99])


# In[18]:


#---------- important parts------------


# In[19]:


# no grammer "" no NP
# evaluate the nothing grammer
# 43% belong to tangs out of NP all of them belongs to O outside of NP


# In[20]:


cp = nltk.RegexpParser("")


# In[21]:


test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])


# In[22]:


print(cp.evaluate(test_sents))


# In[23]:


grammar = "NP:{<[CDJNP].*>+}"


# In[24]:


cp = nltk.RegexpParser(grammar)


# In[25]:


print(cp.evaluate(test_sents))


# In[ ]:





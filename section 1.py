#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cobra


# In[5]:


from cobra import Model,Reaction,Metabolite


# In[6]:


model=Model('first_model')


# In[7]:


v1=Reaction('v1')
v1.name='v1'
v1.lower_bound=0
v1.upper_bound=1000


# In[8]:


v2=Reaction('v2')
v2.name='v2'
v2.lower_bound=0
v2.upper_bound=1000


# In[9]:


M=Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000


# In[10]:


v0=Reaction('v0')
v0.name='v0'
v0.lower_bound=1
v0.upper_bound=1


# In[12]:


v3=Reaction('v3')
v3.name='v3'
v3.lower_bound=.9
v3.upper_bound=.9


# In[13]:


v4=Reaction('v4')
v4.name='v4'
v4.lower_bound=0
v4.upper_bound=1000


# In[14]:


A=Metabolite('A',compartment='c')
B=Metabolite('B',compartment='c')
C=Metabolite('C',compartment='c')
ATP=Metabolite('ATP',compartment='c')


# In[15]:


################ V1 : A======>B #################
v1.add_metabolites({A:-1,B:1})


# In[16]:


################ V2 : B======>C #################
v2.add_metabolites({B:-1,C:1})


# In[17]:


################ V0 : ======>A #################
v0.add_metabolites({A:1})


# In[18]:


################ M : C======> #################
M.add_metabolites({C:-1})


# In[19]:


################ v3 : A======>ATP #################
v3.add_metabolites({A:-1,ATP:1})


# In[20]:


################ v4 : ATP======> #################
v4.add_metabolites({ATP:-1})


# In[21]:


model.add_reactions([v0,v1,v2,v3,v4,M])
model.objective='M'
model.optimize()


# In[22]:


model.summary()


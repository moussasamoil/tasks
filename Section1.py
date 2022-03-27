#!/usr/bin/env python
# coding: utf-8

# In[53]:


import cobra 


# In[54]:


from cobra import Model, Reaction,Metabolite


# In[55]:


model=Model('example')


# In[56]:


###### v1 : A=====> B ########
v1=Reaction('v1')
v1.name='V1'
v1.lower_bound=0
v1.upper_bound=1000


# In[57]:


###### v2 : B=====> c ########

v2=Reaction('v2')
v2.name='V2'
v2.lower_bound=0
v2.upper_bound=1000


# In[58]:


###### v0 : =====> A ######

v0=Reaction('v0')
v0.name='V0'
v0.lower_bound=20
v0.upper_bound=20


# In[59]:


###### M : C=====>  ########

M=Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000


# In[60]:


###### v3 : A=====> ATP #########

v3=Reaction('v3')
v3.name='v3'
v3.lower_bound=18
v3.upper_bound=18


# In[61]:


###### V4 : ATP=====>  #########

v4=Reaction('v4')
v4.name='v4'
v4.lower_bound=0
v4.upper_bound=1000


# In[62]:


A= Metabolite(
    'A',compartment='c')
B=Metabolite(
    'B',compartment='c')
C= Metabolite(
    'C',compartment='c')

ATP= Metabolite(
    'ATP',compartment='c')


# In[63]:


###### Add metabolites in reaction V1 #########


v1.add_metabolites({A:-1,B:1})


# In[64]:


###### Add metabolites in reaction V2 ##########

v2.add_metabolites({B:-1,C:1})


# In[65]:


###### Add metabolites in reaction V0 #########

v0.add_metabolites({A:1})


# In[66]:


###### Add metabolites in reaction M ###########

M.add_metabolites({C:-1})


# In[67]:


###### Add metabolites in reaction v3 ########

v3.add_metabolites({A:-1,ATP:1})


# In[68]:


###### Add metabolites in reaction V4 ######

v4.add_metabolites({ATP:-1})


# In[69]:


###### Add reactions in model  ######

model.add_reactions([v0,v1,v2,v3,v4,M])


# In[70]:


##### Put M as a objective function  ######

model.objective = M

model.optimize()


# In[71]:


model.summary()



# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab inline')


# In[27]:

import pandas as pd
import numpy as np
import seaborn as sns
rcParams["figure.figsize"] = 18, 8
np.set_printoptions(precision=4)


# In[49]:

df = pd.read_csv("data/opendata_projects.csv", 
                 true_values="t", false_values="f",
                 parse_dates = ["date_posted", "date_completed", "date_expiration"])


# In[38]:

df.columns


# In[39]:

df._schoolid.value_counts().hist(bins=30, log=np.log10)
plt.title("school projects");


# In[40]:

one_proj_schools = (df._schoolid.value_counts() == 1).sum()
uniq_schools = len(df._schoolid.value_counts())

print "One project schools / Total amount of schools\n"
print "{} / {} -- {:.2f}".format(one_proj_schools, uniq_schools, np.float(one_proj_schools)/uniq_schools)


# In[67]:

year_posted = df.date_posted.apply(lambda date: date.year)
df["year_posted"] = year_posted
years_active = df.groupby("_schoolid").year_posted.nunique()
projs_per_school = df.groupby("_schoolid")._projectid.nunique()


# In[77]:

# years_active.hist(bins=13)
year_posted.hist(bins=13)


# In[81]:

projs_per_year = projs_per_school/years_active.astype(np.float)


# In[87]:

projs_per_year.hist(bins=40, log=np.log10)
plt.title("Projects/year")


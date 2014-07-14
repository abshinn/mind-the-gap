
# coding: utf-8

# In[94]:

get_ipython().magic(u'pylab inline')


# In[95]:

import pandas as pd
import numpy as np
import seaborn as sns
rcParams["figure.figsize"] = 18, 8
np.set_printoptions(precision=4)


# ### Read in project data

# In[96]:

df = pd.read_csv("data/opendata_projects.csv", 
                 true_values="t", false_values="f",
                 parse_dates = ["date_posted", "date_completed", "date_expiration"])


# In[97]:

for column in df.columns:
    print column


# ### Histogram: Projects per school [2002 - 2013]

# In[113]:

df._schoolid.value_counts().hist(bins=40, log=np.log10)
plt.title("Projects / school Histo");


# ### How many one-project schools are there?

# In[114]:

one_proj_schools = (df._schoolid.value_counts() == 1).sum()
uniq_schools = len(df._schoolid.value_counts())

print "[One project schools / Total amount of schools]\n"
print "{} / {} -- {:.2f}".format(one_proj_schools, uniq_schools, np.float(one_proj_schools)/uniq_schools)

# print "\n"

# print "[Number of one-project schools that were unsuccessful]\n"
# one_proj_df = df.loc[(df._schoolid.value_counts() == 1).index]
# one_proj_expired = len(one_proj_df.funding_status == "expired")
# print "{} / {} -- {:.2f}".format(one_proj_expired, len(one_proj_df), np.float(one_proj_expired)/len(one_proj_df))


# In[101]:

df.funding_status.value_counts()


# In[67]:

year_posted = df.date_posted.apply(lambda date: date.year)
df["year_posted"] = year_posted
years_active = df.groupby("_schoolid").year_posted.nunique()
projs_per_school = df.groupby("_schoolid")._projectid.nunique()

projs_per_year = projs_per_school/years_active.astype(np.float)


# ### Projects/year per school Histogram

# In[112]:

projs_per_year.hist(bins=40, log=np.log10)
plt.title("Projects per year per school Histo");


# In[111]:

# years_active.hist(bins=13)
year_posted.hist(bins=13)
plt.title("Projects by year");


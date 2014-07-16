
# In[1]:

get_ipython().magic(u'pylab inline')


# Out[1]:

#     Populating the interactive namespace from numpy and matplotlib
# 

# In[36]:

import pandas as pd
import numpy as np
import seaborn as sns
rcParams["figure.figsize"] = 18, 8
sns.set(rcParams)
np.set_printoptions(precision=4)


# ### Read in project data

# In[3]:

df = pd.read_csv("data/opendata_projects.csv", 
                 true_values="t", false_values="f",
                 parse_dates = ["date_posted", "date_completed", "date_expiration"])


# In[4]:

for column in df.columns:
    print column


# Out[4]:

#     _projectid
#     _teacher_acctid
#     _schoolid
#     school_ncesid
#     school_latitude
#     school_longitude
#     school_city
#     school_state
#     school_zip
#     school_metro
#     school_district
#     school_county
#     school_charter
#     school_magnet
#     school_year_round
#     school_nlns
#     school_kipp
#     school_charter_ready_promise
#     teacher_prefix
#     teacher_teach_for_america
#     teacher_ny_teaching_fellow
#     primary_focus_subject
#     primary_focus_area
#     secondary_focus_subject
#     secondary_focus_area
#     resource_type
#     poverty_level
#     grade_level
#     vendor_shipping_charges
#     sales_tax
#     payment_processing_charges
#     fulfillment_labor_materials
#     total_price_excluding_optional_support
#     total_price_including_optional_support
#     students_reached
#     total_donations
#     num_donors
#     eligible_double_your_impact_match
#     eligible_almost_home_match
#     funding_status
#     date_posted
#     date_completed
#     date_thank_you_packet_mailed
#     date_expiration
# 

# ### Histogram: Projects per school [2002 - 2013]

# In[91]:

# df._schoolid.value_counts().hist(bins=40, log=np.log10)
# plt.title("Projects / school Histo");


# ### How many one-project schools are there?

# In[45]:

one_proj_schools = (df._schoolid.value_counts() == 1).sum()
uniq_schools = len(df._schoolid.value_counts())

print "[One project schools / Total amount of schools]\n"
print "{} / {} -- {:.2f}".format(one_proj_schools, uniq_schools, np.float(one_proj_schools)/uniq_schools)

# print "\n"

# print "[Number of one-project schools that were unsuccessful]\n"
# one_proj_df = df.loc[df._schoolid.value_counts() == 1,:]
# one_proj_expired = len(one_proj_df.funding_status == "expired")
# print "{} / {} -- {:.2f}".format(one_proj_expired, len(one_proj_df), np.float(one_proj_expired)/len(one_proj_df))

# one_proj_df.funding_status.value_counts().plot(kind="bar")
# plt.title("Breakdown of success for one-project schools");


# Out[45]:

#     [One project schools / Total amount of schools]
#     
#     13685 / 56354 -- 0.24
# 

# ### One-project schools: Breakdown by Project Success

# In[54]:

print "[Funding Status Percentages -- out of {} one-project schools]".format(len(one_proj_df))
print (one_proj_df.funding_status.value_counts().astype(np.float)/len(one_proj_df)).apply(lambda x: "{:.2f}".format(x))
print

sns.factorplot("funding_status", data=one_proj_df, kind="bar", palette="Blues_d", size=8);
plt.title("One-Prject Schools -- Funding Status");


# Out[54]:

#     [Funding Status Percentages -- out of 13685 one-project schools]
#     completed      0.72
#     expired        0.25
#     reallocated    0.02
#     dtype: object
#     
# 

# image file:

# In[81]:

# What is going on here?
# There are only three years where one-proj schools were unsuccesful?
one_proj_df.date_posted.apply(lambda date: date.year).value_counts()


# Out[81]:

#     2007    13114
#     2008      547
#     2009       24
#     dtype: int64

# In[101]:

df.funding_status.value_counts()


# Out[101]:

#     completed      437671
#     expired        183296
#     live            19631
#     reallocated      6097
#     dtype: int64

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


# Out[112]:

# image file:

# In[90]:

## years_active.hist(bins=13)
# year_posted.hist(bins=13)
# plt.title("Projects by year");


# ### Students Reached Over Time

# In[89]:

# dfsorted = df[df.funding_status == "completed"].sort("date_posted")
# dfsorted.index = dfsorted.date_posted
# dfsorted.students_reached.cumsum().plot()
# plt.title("Students Reached Cummulative Sum");


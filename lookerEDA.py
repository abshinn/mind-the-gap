
# In[5]:

get_ipython().magic(u'pylab inline')


# Out[5]:

#     Populating the interactive namespace from numpy and matplotlib
# 

# In[6]:

import pandas as pd
import numpy as np
import seaborn as sns
rcParams["figure.figsize"] = 18, 8
sns.set(rcParams)
sns.set(palette="Set2")
sns.set_context("poster")
np.set_printoptions(precision=4)


# ## Read in project data

# In[58]:

columns = [u'essay_title', u'_projectid', u'date_completed', u'date_expired', u'funding_status', 
           u'grade_level', u'num_donors', u'date_posted', u'poverty_level', u'students_reached', 
           u'project_subject', u'subject_category', u'total_donations', u'tot_price_without_support', 
           u'total_price_with_support', u'_schoolid', u'city', u'state', u'district', u'latitude', 
           u'longitude', u'teach_for_america', u'_teacherid', u'zip', u'_NCESid', u'resource_type', u'county']

df = pd.read_csv("data/looker_completed_projects_7_14_14.csv", skiprows = 1, names=columns,
                 parse_dates = ["date_posted", "date_completed", "date_expired"],
                 true_values="Yes", false_values="No")


# In[73]:

df.funding_status.value_counts()


# Out[73]:

#     completed      435665
#     expired        181882
#     reallocated      6043
#     dtype: int64

# In[21]:

for column in sorted(columns):
    print column


# Out[21]:

#     _NCESid
#     _projectid
#     _schoolid
#     _teacherid
#     city
#     county
#     date_completed
#     date_expired
#     date_posted
#     district
#     essay_title
#     funding_status
#     grade_level
#     latitude
#     longitude
#     num_donors
#     poverty_level
#     project_subject
#     resource_type
#     state
#     students_reached
#     subject_category
#     teach_for_america
#     tot_price_without_support
#     total_donations
#     total_price_with_support
#     zip
# 

# In[23]:

print "Date Posted Range:\n{} - {}\n".format(df.date_posted.min(), df.date_posted.max())

# print "Date Completed Range:\n{} - {}\n".format(df.date_completed.min(), df.date_completed.max())


# Out[23]:

#     Date Posted Range:
#     2002-09-13 00:00:00 - 2014-03-07 00:00:00
#     
# 

# ## Histogram: Projects per school [2002 - 2014]

# In[91]:

# df._schoolid.value_counts().hist(bins=40, log=np.log10)
# plt.title("Projects / school Histo");


# ## How many one-project schools are there?

# In[71]:

one_proj_schools = (df._schoolid.value_counts() == 1).sum()
uniq_schools = len(df._schoolid.value_counts())

print "[One project schools / Total amount of schools]\n"
print "{} / {} -- {:.2f}".format(one_proj_schools, uniq_schools, np.float(one_proj_schools)/uniq_schools)


# Out[71]:

#     [One project schools / Total amount of schools]
#     
#     13659 / 55285 -- 0.25
# 

# ## One-project schools: Breakdown by Project Success

# In[87]:

# df.groupby("_schoolid")._projectid.nunique() == 1
# (df._schoolid.value_counts() == 1).dr
df[df._schoolid.drop_duplicates()]


# Out[87]:


    ---------------------------------------------------------------------------
    KeyError                                  Traceback (most recent call last)

    <ipython-input-87-d54f2148e2f0> in <module>()
          1 # df.groupby("_schoolid")._projectid.nunique() == 1
          2 # (df._schoolid.value_counts() == 1).dr
    ----> 3 df[df._schoolid.drop_duplicates()]
    

    /usr/local/lib/python2.7/site-packages/pandas/core/frame.pyc in __getitem__(self, key)
       1650         if isinstance(key, (Series, np.ndarray, list)):
       1651             # either boolean or fancy integer index
    -> 1652             return self._getitem_array(key)
       1653         elif isinstance(key, DataFrame):
       1654             return self._getitem_frame(key)


    /usr/local/lib/python2.7/site-packages/pandas/core/frame.pyc in _getitem_array(self, key)
       1694             return self.take(indexer, axis=0, convert=False)
       1695         else:
    -> 1696             indexer = self.ix._convert_to_indexer(key, axis=1)
       1697             return self.take(indexer, axis=1, convert=True)
       1698 


    /usr/local/lib/python2.7/site-packages/pandas/core/indexing.pyc in _convert_to_indexer(self, obj, axis, is_setter)
        965                     if isinstance(obj, tuple) and is_setter:
        966                         return {'key': obj}
    --> 967                     raise KeyError('%s not in index' % objarr[mask])
        968 
        969                 return indexer


    KeyError: '[\'"76168e4e68c8adb7bbf0d672ac05f6e4"\' \'"01f83c022f08e89e06a737d2df369132"\'\n \'"dd6a9f68f843096de713ef834a95e805"\' ...,\n \'"cb1ac51c57e5ecb8f9a5ab5204e94b8c"\' \'"4effb11a762d152b107678ab4744063b"\'\n \'"f0d8c5dc8f630c1251a75cde190ecdd2"\'] not in index'


# In[77]:

print "[Funding Status Percentages -- out of {} one-project schools]\n".format(len(one_proj_df))
print (one_proj_df.funding_status.value_counts().astype(np.float)/len(one_proj_df)).apply(lambda x: "{:.2f}".format(x))
print

sns.factorplot("funding_status", data=one_proj_df, kind="bar", palette="Greens_d", size=8);
plt.title("One-project Schools -- Funding Status");


# Out[77]:


    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)

    <ipython-input-77-4edcd5576d12> in <module>()
          3 print
          4 
    ----> 5 sns.factorplot("funding_status", data=one_proj_df, kind="bar", palette="Greens_d", size=8);
          6 plt.title("One-project Schools -- Funding Status");


    /usr/local/lib/python2.7/site-packages/seaborn/linearmodels.pyc in factorplot(x, y, hue, data, row, col, col_wrap, estimator, ci, n_boot, units, x_order, hue_order, col_order, row_order, kind, markers, linestyles, dodge, join, hline, size, aspect, palette, legend, legend_out, dropna, sharex, sharey, margin_titles)
        862     # Plot by mapping a plot function across the facets
        863     if kind == "bar":
    --> 864         facets.map_dataframe(barplot, x, y, hue, **kwargs)
        865     elif kind == "box":
        866         def _boxplot(x, y, hue, data=None, **kwargs):


    /usr/local/lib/python2.7/site-packages/seaborn/axisgrid.pyc in map_dataframe(self, func, *args, **kwargs)
        373 
        374             # Draw the plot
    --> 375             self._facet_plot(func, ax, args, kwargs)
        376 
        377         # Finalize the annotations and layout


    /usr/local/lib/python2.7/site-packages/seaborn/axisgrid.pyc in _facet_plot(self, func, ax, plot_args, plot_kwargs)
        391 
        392         # Draw the plot
    --> 393         func(*plot_args, **plot_kwargs)
        394 
        395         # Sort out the supporting information


    /usr/local/lib/python2.7/site-packages/seaborn/linearmodels.pyc in barplot(x, y, hue, data, estimator, hline, ci, n_boot, units, x_order, hue_order, dropna, color, palette, label, ax)
        935     if ax is None:
        936         ax = plt.gca()
    --> 937     plotter.plot(ax)
        938     return ax
        939 


    /usr/local/lib/python2.7/site-packages/seaborn/linearmodels.pyc in plot(self, ax)
        268         """Plot based on the stored value for kind of plot."""
        269         plotter = getattr(self, self.kind + "plot")
    --> 270         plotter(ax)
        271 
        272         # Set the plot attributes (these are shared across plot kinds


    /usr/local/lib/python2.7/site-packages/seaborn/linearmodels.pyc in barplot(self, ax)
        297 
        298             color = self.palette if self.x_palette else self.palette[i]
    --> 299             ecolor = self.err_palette[i]
        300             label = self.hue_order[i]
        301 


    IndexError: list index out of range


#     [Funding Status Percentages -- out of 55285 one-project schools]
#     
#     Series([], dtype: float64)
#     
# 

# image file:

# In[105]:

# What is going on here?
# There are only three years where one-proj schools were unsuccesful?
print "Only three years with unsuccessful projects?"
one_proj_df.date_posted.apply(lambda date: date.year).value_counts()


# Out[105]:

#     Only three years with unsuccessful projects?
# 

#     2007    13114
#     2008      547
#     2009       24
#     dtype: int64

# ## Funding Status for All Projects

# In[109]:

print df.funding_status.value_counts()
print "\nPercentages:"
print (df.funding_status.value_counts().astype(np.float)/len(df)).apply(lambda flt: "{:.2f}".format(flt))


# Out[109]:

#     completed      437671
#     expired        183296
#     live            19631
#     reallocated      6097
#     dtype: int64
#     
#     Percentages:
#     completed      0.68
#     expired        0.28
#     live           0.03
#     reallocated    0.01
#     dtype: object
# 

# ## Projects/year per school Histogram

# In[110]:

year_posted = df.date_posted.apply(lambda date: date.year)
df["year_posted"] = year_posted
years_active = df.groupby("_schoolid").year_posted.nunique()
projs_per_school = df.groupby("_schoolid")._projectid.nunique()

projs_per_year = projs_per_school/years_active.astype(np.float)


# In[160]:

projs_per_year.hist(bins=40, log=np.log10)
plt.title("Projects per year per school Histo");


# Out[160]:

# image file:

# In[90]:

## years_active.hist(bins=13)
# year_posted.hist(bins=13)
# plt.title("Projects by year");


# ## Students Reached Over Time

# In[104]:

# dfsorted = df[df.funding_status == "completed"].sort("date_posted")
# dfsorted.index = dfsorted.date_posted
# dfsorted.students_reached.cumsum().resample("M", how="mean").plot()
# plt.title("Students Reached Cummulative Sum");


# ## Average number of projects per year per school

# In[122]:

projs_by_year = df.sort("date_posted").groupby(["_schoolid", "year_posted"])._projectid.nunique()


# In[167]:

groupby_year = df.groupby("year_posted")
projs_by_year = groupby_year._projectid.nunique()/groupby_year._schoolid.nunique()

projs_by_year[projs_by_year.index < 2014].plot(marker="o",markerfacecolor="purple")
plt.title("Average Projects per School by Year")
plt.ylabel("numnber of projects")
plt.xlabel("year posted");


# Out[167]:

# image file:

# ### The average amount of projects by year seems more variable than I would have expected.

# ## Resource Types

# In[170]:

# df.resource_type.value_counts().plot(kind="bar");
df.resource_type.value_counts()


# Out[170]:

#     Supplies      223250
#     Technology    210012
#     Books         139157
#     Other          67969
#     Trips           5276
#     Visitors         988
#     dtype: int64

# In[171]:

df.funding_status.value_counts()


# Out[171]:

#     completed      437671
#     expired        183296
#     live            19631
#     reallocated      6097
#     dtype: int64

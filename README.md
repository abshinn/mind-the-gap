mind-the-gap 
===

#### Zipfian Capstone Project: _Mind the Supply Gap_ on [DonorsChoose.org](http://donorschoose.org)

### Gap in the Supply of Projects

[DonorsChoose.org](http://donorschoose.org) is an organization that enables educators to crowd-source funds for classroom projects, helping to provide essential and enriching classroom projects for students all over the country.

The purpose of this project is to help increase the supply of projects to DonorsChoose.org by seeking out school districts which are most economically and similar to the most active DonorsChoose districts.

### Data

Data sources used include DonorsChoose.org project data from their thirteen year history, education revenue data the National Center for Education Statistics (NCES), and district-level demographic and economic census data. 

- [DonorsChoose.org Open Data - Hacking Education](http://data.donorschoose.org/open-data/overview/)
- [National Center for Education Statistics](http://nces.ed.gov/ccd/ccddata.asp)
- [2010 US Census school districts](http://nces.ed.gov/surveys/sdds/ed/)

The NCES data can be downloaded by executing the shell script `download_nces.sh`:

```bash
$ ./download_nces.sh
```

### Process

- Data pipeline
 * `get_donorschoose.py` 
 * `get_nces.py` 
 * `get_census.py`
 * `get_latlon.py`
- EDA on California schools alone
 * `california.py`
- Train classifiers to predict DonorsChoose.org activity
 * `feature_importance.py`
- Explore feature-importances with the aggregated data
- Develop a fast cosine-similarity calculation using matrix multiplication
 * `similarity.py`
- Recommend districts based on their cosine-similarity to active schools
 * `district.py`
- Develop d3.js interactive visualization to explore result
 * [hosted on abshinn.github.io](http://abshinn.github.io/mind-the-gap)
 * [the code lives here](https://github.com/abshinn/abshinn.github.io/tree/master/projects/mind-the-gap)

My first approach was to train classifiers to predict active DonorsChoose.org schools. Due to the complicated nature of the data, it was difficult to predict activity with meaningful accuracy. As an alternative, I used the classifiers to whittle down the large feature set for a cosine-similarity calculation. The objective for the cosine-similarity calculation is to leverage the district-level aggregated data to find districts that are *economically similar* to the most *active* DonorsChoose.org schools. 

I define *economic similarity* with district revenue on the local, state, and federal levels, as well as the average income and housing prices of their local communities. I label a district to be *active* if it has an average of 3 or more projects per year since its first project with DonorsChoose.org.

### End Product 

####[_Interactive Visualization_](http://abshinn.github.io/mind-the-gap)

![alt text](https://github.com/abshinn/mind-the-gap/blob/master/mind-the-gap.png "Mind the Supply Gap - Interactive Visualization")

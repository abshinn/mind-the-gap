Project Proposal: DonorsChoose.org 
===

</br>

### _Mind the Supply Gap_

Adam Shinn, July 10th, 2014

</br>

### Description
[Donors Choose](http://donorschoose.org) is an organization that enables educators to crowdsource funds for classroom projects, helping to provide essential and enriching classroom projects for students all over the country. The over-aching goal of the project is to provide insight to DonorsChoose.org so that they will be most effective in seeking out new schools to aid and to help guide teachers to create successfully-funded projects.

DonorsChoose.org has been helping teachers for thirteen years. Their data spans their thirteen-year history and contains information on donor transactions as well as the project details proposed by the educators.

The plan for this project is to perform series of analyses to better understand why there are gaps in supply of projects to DonorsChoose and to present them in quantitatively meaningful ways. Based on the data compiled for the analyses, I hope to produce a data product that produces useful characteristics for any given school along with a D3 visualization that either highlights an interesting finding or showcases the data.

##### The question I will attempt to answer:
How do school districts with a relatively low supply of projects differ from active DonorsChoose districts? Do they differ by:
- geographic location?
- school size?
- demographics?
- amount of state and federal funding?
- presence federal aid programs?
- percent of Teach For America educators?
- percent of essential versus enrichment projects?
- type of projects?

In other words, I am attempting to determine any limiting factors that contribute to the growth of DonorsChoose for any given school.

</br>

### Modular Approach
##### 1) Prepare Data
- Combine DonorsChoose, National Center for Education Statistics, and Census data on schools and their communities.

##### 2) Supply Gap Label
   - For every school, determine measure of DonorsChoose activity proportional to the total amount of projects over time.
   - Label schools as having a supply gap if their activity metric is below the mean, or some appropriate threshold.

##### 3) Data Exploration
   - Explore whether there are any distinguishing factors that lead to a gap in the supply of projects.
   - Perform feature importance with respect to project success for supply gap schools, compare to active schools.

##### 4) Data Exploration Using Cosine-Similarity
   - Using community demographics and school revenue, compute the cosine-similarity of schools and/or districts.
   - Compare project success in similar supply-gap schools.

##### 5) Probability of Success
   - Time permitting, I would like to create a data product that computes the probability of success given the project success rate of similar school districts, project cost, project type, teacher information, and project description.

##### 6) Visualize
   - Create a D3 map and/or graph to showcase a resulting analysis, exploration, or data product.

</br>

### The Data

The data sources include the DonorsChoose internal database, the National Center for Education Statistics (NCES), and census data. No scraping required. I have been given access to the DonorsChoose internal SQL database which contains both current data and data from their thirteen-year history. The data from NCES contains state and federal revenue information on each school and district. United States Census data will add city-level demographic information to the data set.

</br>

### Presentation

I intend to present this project modularly, creating a series of personal blog posts that follow the theme of analyzing and visualizing gaps in supply. Analyses will also be available on GitHub in the form of scripts and well-formatted ipython notebooks. Additionally, DonorsChoose.org has a [blog](http://data.donorschoose.org/) in which I can showcase any particularly fascinating findings or visualizations created by the project.

</br>

### Anticipated Hurdles
##### Data Constraint
This project is not constrained by lack of data, or difficulty of obtaining data, but could fall victim to inconclusive findings. However, uninteresting or inconclusive analyses may still be of use to DonorsChoose and will still be a presentable and worthwhile project.

##### Time Constraint
I plan to start with simple analyses and add complexity as time goes on. Worst case scenario, I will be able to present some kind of in-depth analysis and highlight on-going work at the end of two weeks.

</br>

### Bias and Assumptions
It is possible that arbitrarily choosing a threshold with which to determine a school has having a supply-gap may introduce unwanted bias. I will need to run the analyses with a range of thresholds to determine whether bias is introduced.

</br>

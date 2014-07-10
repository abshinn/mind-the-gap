DonorsChoose.org Final Proposal
===============================

### _Demographical and Geographical Supply-gap Predictor_

Adam Shinn, July 9th, 2014

</br>

#### Description

[Donors Choose](http://donorschoose.org) is an organization that enables educators to crowdsource funds for classroom projects, helping to provide essential and enriching classroom projects for students all over the country. The overaching goal of the project is to help provide insight and guidance to DonorsChoose.org so that they will be most effective when guiding teachers to create successfully-funded projects. DonorsChoose.org has been helping teachers for thirteen years. Their data spans their thirteen-year history and contains information about donors as well as the project details proposed by the educators.

Modular project, high-level details
1) Supply Gap Label
   - For every school, determine measure of DonorsChoose activity proportional to the total amount of projects over time.
     (perhaps by district as well?)
     (factor in number of teachers?)
     (filter out schools just starting out with DonorsChoose?)
   - Label schools as having a supply gap if their activity metric is below the mean, or some threshold.

2) Explore whether there are any distinguishing factors that lead to a gap in the supply of projects
   - Georgraphic location
   - State/Federal funding
   - percent of students getting free or reduced lunch

3) School Similarity
   - Using community demographics and school revenue, compute the cosine similarity of the schools.


Questions to Answer:
- Which projects are most important to different areas?
  In other words, in what types of projects does a community find most valuable?

The idea for project idea #3 is similar to project idea #2 in that it leverages community demographics and school district revenue statistics to compute school similarity. However, the difference is that this project sets out to predict which schools stand to benefit most from DonorsChoose projects.

< add more description here >

</br>

#### Presentation

Ideally, I would like to use an interactive js.d3 heat map to show gap locations (district level) for a given year. DonorsChoose.org has a [blog](http://data.donorschoose.org/) in which I can showcase the data product created by the project.

</br>

#### Approach

general plan:
- flag a school as having a supply gap by having only a small amount of activity with DonorsChoose
- how do I define activity, amount of proposed projects per year?
- label as being a gap school if it is less than the mean, or first quartile of projects/year for all schools?
- what biases will I be introducing if I just arbitrarily decide which schools have a gap in supply or not?
- characterize schools that have supply gaps to those that do not with the following features:
    * school reveneue
    * federal aid, e.g., free lunches
    * student body size
    * geographic location
- how do these supply gap characteristics change over time?

detailed plan:
- Combine DonorsChoose, NCES, and Census data on schools and their communities.
- Compute school cosine-similarity.
< perhaps use NMF? >
< fill in details >
- Come up with an appropriate visualization to present the findings in a most useful way for educators, or for the DonorsChoose.org team.

</br>

#### Data

The data sources include the DonorsChoose internal database, the National Center for Education Statistics (NCES), and census data. I have been given access to the DonorsChoose internal database which contains both current data as well as data from their thirteen-year history. The data from NCES contains state and federal financial information on each school and district. United States Census data will add city-level demographic information to help further characterize the schools for a cosine similarity calculation.

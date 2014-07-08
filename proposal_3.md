DonorsChoose.org Project #3
===========================

### _Demographical and Geographical Supply-gap Predictor_

Adam Shinn, July 7th, 2014 -- _preliminary proposal_

</br>

#### Description

[Donors Choose](http://donorschoose.org) is an organization that enables educators to crowdsource funds for classroom projects, helping to provide essential and enriching classroom projects for students all over the country. The overaching goal of the project is to help provide insight and guidance to DonorsChoose.org so that they will be most effective when guiding teachers to create successfully-funded projects. DonorsChoose.org has been helping teachers for thirteen years. Their data spans their thirteen-year history and contains information about donors as well as the project details proposed by the educators.

The idea for project idea #3 is similar to project idea #2 in that it leverages community demographics and school district revenue statistics to compute school similarity. However, the difference is that this project sets out to predict which schools stand to benefit the most from DonorsChoose projects. The target schools here are schools that have not yet used DonorsChoose, or perhaps are not using DonorsChoose to its full potential. 

< add more description here >

</br>

#### Presentation

Ideally, I would like to use an interactive js.d3 United States heat or contour map to demonstrate my findings. DonorsChoose.org has a [blog](http://data.donorschoose.org/) in which I can showcase the data product created by the project.

</br>

#### Approach

- Combine DonorsChoose, NCES, and Census data on schools and their communities.
- Compute school cosine-similarity.

< perhaps use NMF? >
< fill in approach more details >

- Come up with an appropriate visualization to present the findings in a most useful way for educators, or for the DonorsChoose.org team.

</br>

#### Data

The data sources include the DonorsChoose internal database, the National Center for Education Statistics (NCES), and census data. I have been given access to the DonorsChoose internal database which contains both current data as well as data from their thirteen-year history. The data from NCES contains state and federal financial information on each school and district. United States Census data will add city-level demographic information to help further characterize the schools for a cosine similarity calculation.

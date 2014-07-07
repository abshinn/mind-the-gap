DonorsChoose.org Project #2
===========================

### _School Recommender_

Adam Shinn, July 6th, 2014 -- _preliminary proposal_

</br>

### Description (high-level)

[Donors Choose](http://donorschoose.org) is an organization that enables educators to crowdsource funds for classroom projects, helping to provide essential and enriching classroom projects for students all over the country. The overaching goal of the project is to help provide insight and guidance to DonorsChoose.org so that they will be most effective when guiding teachers to create successfully-funded projects. DonorsChoose.org has been helping teachers for thirteen years. Their data contains information about donors as well as the project details proposed by the educators.

The idea for project idea #2 is to build a recommendation system for DonorsChoose.org that will be able to recommend projects to schools that would be most successful based on school 'features' such as size, city/county demographics, poverty-level, and types of governmental aid. Proposal recommendations for educators using DonorsChoose has been addressed at before, but not on the level of creating personalized recommendations for a given school. If effective, this tool could be used by DonorsChoose.org to approach schools with fruitful project ideas and tips for successful DonorsChoose projects. The following is a pseudo recommendation:

Similar schools to yours:
- have had been successful with A, B, and C types of projects.
- have had T times more success with enrichment projects compared to essential projects.
- were most successful with projects with a mean proposed cost of X.
- have received an average of Y dollars of funding from DonorsChoose.

</br>

### Presentation (how are you presenting your work?)

The analyses can be presented piece-wise in personal blog posts and in ipython notebooks available on github. Additionally, I would like to emphasize an interesting finding in an interactive javascript D3 plot. Furthermore, DonorsChoose.org has a [blog](http://data.donorschoose.org/) in which I can showcase my findings.

</br>

### Approach (what is your next step?)

- Combine DonorsChoose, NCES, and Census data.
- Compute school similarity.
- Group schools and districts based on similarity and aggregate project statistics.
- Categorize projects using topic modeling, and determine which projects belong to each school similarity category.

</br>

### Data Sources

The data sources include the DonorsChoose internal database, the National Center for Education Statistics (NCES), and census data. I have been given access to the DonorsChoose internal database which contains both current data as well as data from their thirteen-year history. The data from NCES contains state and federal financial information on each school and district. United States Census data will add city-level demographic information to help further characterize the schools for a cosine similarity calculation.

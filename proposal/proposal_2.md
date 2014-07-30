DonorsChoose.org Project #2
===========================

### _School-Project Recommender_

Adam Shinn, July 6th, 2014 -- _preliminary proposal_

</br>

#### Description (high-level)

[Donors Choose](http://donorschoose.org) is an organization that enables educators to crowdsource funds for classroom projects, helping to provide essential and enriching classroom projects for students all over the country. The overaching goal of the project is to help provide insight and guidance to DonorsChoose.org so that they will be most effective when guiding teachers to create successfully-funded projects. DonorsChoose.org has been helping teachers for thirteen years. Their data spans their thirteen-year history and contains information about donors as well as the project details proposed by the educators.

The idea for project idea #2 is to build a recommendation system for DonorsChoose.org that will be able to recommend projects to schools that would be most successful based on school 'features' such as size, city/county demographics, poverty-level, and types of governmental aid. Proposal recommendations for educators using DonorsChoose has been addressed at before, but not on the level of creating personalized recommendations for a given school. If effective, this tool could be used by DonorsChoose.org to approach schools with fruitful project ideas and tips for successful DonorsChoose projects. The following is a pseudo recommendation:

Similar schools to yours:
- have had been successful with A, B, and C types of projects.
- have had T times more success with enrichment projects compared to essential projects.
- were most successful with projects with a mean proposed cost of X.
- have received an average of Y dollars of funding from DonorsChoose.

This tool could be also be used as outreach to target both current DonorsChoose schools and schools that have yet to use DonorsChoose.  

</br>

#### Presentation (how are you presenting your work?)

The analyses can be presented piece-wise in personal blog posts and in ipython notebooks available on github. Additionally, I would like to emphasize an interesting finding in an interactive javascript D3 plot. Or, if possible, I would like to create an infographic describing the differences between types of schools with the goal of informing DonorsChoose and educators to aid with project creation. Furthermore, DonorsChoose.org has a [blog](http://data.donorschoose.org/) in which I can showcase my findings.

</br>

#### Approach (what is your next step?)

- Combine DonorsChoose, NCES, and Census data on schools and their communities.
- Compute school cosine-similarity.
- Group schools and districts based on similarity bins and aggregate project success statistics.
- Categorize projects by applying topic modeling techniques to their descriptions, and determine which projects are most successful for each school similarity category.
- Come up with a metric to flag schools that are not getting as much use out of DonorsChoose as other schools. One way to do this would be to select schools for every similarity bin that have a below-average amount of current projects.
- Analyze findings to see if there are any interesting trends or major differences between schools in different similarity categories.
- Come up with an appropriate visualization to present the findings in a most useful way for educators, or for the DonorsChoose.org team.

</br>

#### Data Sources

The data sources include the DonorsChoose internal database, the National Center for Education Statistics (NCES), and census data. I have been given access to the DonorsChoose internal database which contains both current data as well as data from their thirteen-year history. The data from NCES contains state and federal financial information on each school and district. United States Census data will add city-level demographic information to help further characterize the schools for a cosine similarity calculation.

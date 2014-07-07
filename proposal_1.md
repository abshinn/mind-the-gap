DonorsChoose.org Project #1
===========================
### _Time-series Supply Analysis_ 

Adam Shinn, July 6th, 2014 -- _preliminary proposal_

</br>

### Description (high-level)

[Donors Choose](http://donorschoose.org) is an organization that enables educators to crowdsource funds for classroom projects, helping to provide essential and enriching classroom projects for students all over the country. The overaching goal of the project is to help provide insight and guidance to DonorsChoose.org so that they will be most effective when guiding teachers to create successfully-funded projects. DonorsChoose.org has been helping teachers for thirteen years. Their data contains information about donors as well as the project details proposed by the educators.

The idea for project idea #1 is to use time-series analysis to indicate when there is a gap in the supply of projects, or when the amount of project proposals for a given school or district is below a rolling mean. Once these periods of low-activity are flagged as gaps in supply, I could then explore the following questions:

- When are teachers least likely to propose a project on DonorsChoose.org?
- When are teachers most likely to propose projects, and do these times co-inside with school breaks or national holidays?
- Do unsuccessful projects within a school create gaps in the supply of projects?
- Is there a certain time of year when donors give the most?
- Is there a difference in the supply of essential projects versus enrichment projects?
- Is there a correlation between the supply of projects for a school district, and governmental revenue?
- Given all the available data, is it possible to predict project supply gaps?

</br>

### Presentation (how are you presenting your work?)

The analyses can be presented piece-wise in personal blog posts and in ipython notebooks available on github. Additionally, I would like to emphasize an interesting finding in an interactive javascript D3 plot. Furthermore, DonorsChoose.org has a [blog](http://data.donorschoose.org/) in which I can showcase my findings.

</br>

### Approach (what is your next step?)

The first step would be to use time-series rolling-average methods to create a new data set containing the amount of proposals per month for each school and each district. The next step will be to merge the time-series data with data containing governmental revenue sources for each school and district. If supply gaps could be classified by having a below-average (or threshold) amount of projects, then I can use classification algorithms to determine which features contribute most to the gaps in supply.

</br>

### Data Sources

The data sources include the DonorsChoose internal database, the National Center for Education Statistics (NCES), and census data. I have been given access to the DonorsChoose internal database which contains both current data as well as data from their thirteen-year history. The data from NCES contains state and federal financial information on each school and district.

Donors Choose Project Proposal
==============================

Adam Shinn __July 5th, 2014__

#### Supply gap modeling approaches
- One way to define project-supply-gap: period without any projects for a given school.
- Possible gap metric: Projects per month (or year) for a given school or district.
- Time series analysis: `gap = True` if the number of projects is below its yearly moving-window-average.

#### Thoughts
- Which projects are most sucessful in areas with the highest poverty, and how does it compare to areas with little to no poverty?
- Perform topic modeling on DonorsChoose project proposals to find phrases which are most successful.
- Obtain school district revanues and state budget data, categorically describe schools by income need.
- Compare distribution of essesntial versus enrichment projects from location to location.
- How many schools still have yet to use DonorsChoose? Can we predict whether or not an area could use DonorsChoose in the future?
- How has DonorsChoose evolved over time? -- In terms of project costs, donation size, success rate, school type, etc...
- Is more data available on Teach For America teachers?
- Do wealthier areas give more than impoverished areas?
- Topic modeling on donor reason-for-giving description.
- How has DonorsChoose been advertising? How can they advertise smarter?

### High-level description

[Donors Choose](http://donorschoose.org) is an organization that enables educators to crowdsource funds for classroom projects, helping to provide essential and enriching classroom projects for students all over the country. The overaching goal of the project is to help provide insight and guidance to Donors Choose so that they may most effectively focus their resources on guiding teachers to create successfully-funded projects.

</br>

### How are you presenting your work?

In depth analysis will be presented in a well-formatted ipython notebook, and will be available on github. Additionally, I would like to visualize a subset of the findings in an interactive javascript D3 visualization.

</br>

### What is your next step?

</br>

### What are your data sources?

The data sources include the DonorsChoose internal database, the National Center for Education Statistics (NCES), and census data. I have been given access to the DonorsChoose internal database which contains both current data as well as data from their thirteen-year history. The data from NCES contains state and federal financial information on each school and district.

</br>
</br>
</br>

## __From Zipfian Proposal Repo__:

#### Preliminary-proposal

Preliminary proposals serve to oraganize all of your initial ideas and will allow us to provide feedback on each of them before you narrow it down to one... and it is always great to have backups!

Please follow the following template for your project proposals:

1. Name, Date.
2. High level description of the project: what question or problem are you addressing?
3. How are you presenting your work? (web app, visualization, presentation/slides, etc.)
4. Whats your next step?
5. What are your data sources? 

#### Final Proposal
For the final proposal, you will pick one of your initial ideas and elaborate on it.  In addition to everything listed in the preliminary proposal, please add the following:

1. Describe your techniques: break the data pipeline into portions and describe each one.
2. Can you anticipate problems, what are they, do you need to overcome them now? How do you overcome them?
3. How far do you anticipate to take the project in the allotted time frame? 
4. Any other repos, libraries and other tools that you're considering using? Are you citing them? Are you acknowledging them for their contribution?
5. Do you have the dataset already? If not, what is involved in obtaining it?

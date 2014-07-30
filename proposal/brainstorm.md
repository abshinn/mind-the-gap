DonorsChoose.org Project Brainstorm
===================================


###### school recommendation based on similarity _brainstorm_
- similarity can be used to recommend new schools that are most similar to schools/areas with the highest activity
- start with district level, leveraging census demographic data, then find similar schools within candidate districts
- if time permits, recommend projects as well
- analysis goals:
  * overall: recommend schools that would be most successful on DonorsChoose
  * filter by schools who are already active
  * filter by schools that need the most help
  * LDA on project essays for a given set of similar schools -or- list common project types?

###### _possible methods_
- [ ] Find a NCES poverty level metric - if helpful
- [ ] K-means clustering of schools within candidate districts
- [ ] NCES data -- change datatype to integer when appropriate
- [ ] Look into NCES district CCDNF field and how that affects merging with NCES school data

###### _state-level exploratory analysis: potential D3-gold_ **On Hold**
- [ ] State-level exploratory data analysis:
  * rank DonorsChoose success by state
  * run classification and feature importance using wide range of financial data available
  * most financially similar states
  * are most successful DonorsChoose states financially similar?
#### Supply Gap: Thoughts
- One way to define project-supply-gap: period without any projects for a given school.
- Possible gap metric: Projects per month (or year) for a given school or district.
- Time series analysis: `gap = True` if the number of projects is below its yearly moving-window-average.

#### Recommender Project: Thoughts
- Topic modeling on donor reason-for-giving description.
- Be able to describe the local community for a given school.

#### Random Thoughts
- Which projects are most sucessful in areas with the highest poverty, and how does it compare to areas with little to no poverty?
- Perform topic modeling on DonorsChoose project proposals to find phrases which are most successful.
- Obtain school district revanues and state budget data, categorically describe schools by income need.
- Compare distribution of essesntial versus enrichment projects from location to location.
- How many schools still have yet to use DonorsChoose? Can we predict whether or not an area could use DonorsChoose in the future?
- How has DonorsChoose evolved over time? -- In terms of project costs, donation size, success rate, school type, etc...
- Is more data available on Teach For America teachers?
- Do wealthier areas give more than impoverished areas?
- How has DonorsChoose been advertising or conducting email outreach?
- Project recommender for donors who want to help, but do not know where to help.
- Local project recommender for donors: recommend projects to previous donors based on their donation history and proximity to schools in need. 
- Time series: critical threshold before DonorsChoose becomes popular in a certain area
- Project types per geographic region
- Find communities by donation
- Create measure of community spread for each school

- See Carlo: can you be a data scientist

</br>
</br>

________

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
4. Any other repos, libraries and other tools that you''re considering using? Are you citing them? Are you acknowledging them for their contribution?
5. Do you have the dataset already? If not, what is involved in obtaining it?

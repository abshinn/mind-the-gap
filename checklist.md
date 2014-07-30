mind-the-gap
===

### Zipfian Capstone Project: _Mind the Supply Gap_ on [DonorsChoose.org](http://donorschoose.org)

#### Interactive Visualization: [abshinn.github.io/mind-the-gap](http://abshinn.github.io/mind-the-gap)

## Project Checklist

### _Week 1_

#### Monday
- [x] Obtain Data
- [x] Find state-level NCES financial statistics
- [x] Find school-level NCES statistics and financial data

#### Tuesday
- [x] Merge DonorsChoose data with National Center for Education Statistics
- [x] Try and recover schools that have been dropped for not having an \_NCESid
  * not an issue for 2011 at least: keep this in mind for using other years

#### Wednesday
- [x] 2011 School data
  * [x] get additional feature: school district revenue and expenditures
  * [x] compile matrix to train on
  * [x] look at correlations and scatterplot matrix
  * [x] choose arbitrary labels with which to use a decision tree classifier to find most important features
  * [x] implement decision tree classifier to determine most important features

#### Thursday
- [x] 2011 School data
  * [x] run feature importance on a variety of different 'activity' thresholds
- [x] Acquire district-level demographics (California)
- [x] Make a modular pipeline for merging data sources

#### Friday
- [x] Practice presentation, slides:
  * 1 slide: title
  * 1 slide: what is DonorsChoose?
  * 3 slides: project goal 
    * overarching goal
    * histogram of projects/school
    * specific goals
  * 1 slide: what does the data look like?
    * DonorsChoose project data
    * NCES school demographics and federal aid programs
    * NCES school district state, local and federal revenue
    * NCES school expenditures
    * Census demographic/economic information by school district
  * 1 slide: methods
    * cosine-similarity
    * clustering?
  * 1 slide: results
    * find potential super-schools
    * consequence: schools like you!

#### Saturday
- [x] Clean up data merging code
- [x] Prepare project data, NCES data, and Census data for cosine-similarity calculation
- [x] Starting with California, compute school cosine-similarity

#### Sunday
- [x] Write code that takes a school id or name and lists the most similar schools
- [x] Make-sense checks:
  * Pick an arbitrary school, list most similar schools 
  * Are active schools similar to one-another?
- [x] Rename repo to make it easier to find forked repo on Zipfian github
- [x] Create class to store similarity matrix with methods that operate on the matrix

### _Week 2_

#### Monday
- [x] Determine the closest features to two similar schools by taking the difference of two normalized examples
- [x] Create a similarity matrix of DonorsChoose schools alone
- [x] Try creating a similarity matrix with NCES data alone - all schools in the US

#### Tuesday
- [x] Generalize feature importance code
- [x] Normalize and replace NaNs with the mean before cosine-similarity calculation
- [x] Narrow down feature set for NCES data to make matrix multiplication less memory-intensive
- [x] Compute cosine similarity of NCES school districts using revenue features

#### Wednesday
- [x] Make sure NCES district data matches DonorsChoose data
- [x] Explore district similarity
- [x] Attempt to classify activity (no. of projects) with Naive Bayes, Logistic Regression, and Decision Trees
- [x] Feature importance tree
- [x] Explore deliverable idea: web app that characterizes DonorsChoose potential for a given school
  * Type in school name, search NCES school database, find N most similar districts that use use DonorsChoose 
  * Display district revenue and census demographic information
  * If a DonorsChoose school, display DC information
  * Display expected activity, expected benefit given schools in similar districts
  * ml idea: regress on District project activity (projects/years on DonorsChoose)
  * _Nixed_

#### Thursday
- [x] Deliverable idea: D3.js visual of US map, produce tables with potential DonorsChoose schools on hover
  * Compute cosine similarity of all districts using revenue and census data
  * Find potential districts by their similarity to the most successful DonorsChoose schools
  * Create a "potentially active" metric based on rms of similarity
  * Output potential schools to csv or json format
  * Create D3.js interactive
- [x] Update resume
- [x] Initialize webpage (abshinn.github.io/mind-the-gap)
- [x] Pull down census data for all states
- [x] Compile a district data set with all districts [with NCES revenue and Census features]
- [x] Compute cosine similarity, try pickling

#### Friday
- [x] Compile list of districts most similar to active donors choose districts
  * Choose 10 most similar districts for all DonorsChoose districts that have more than 100 projects
  * Take out DonorsChoose super-schools from list
  * Group by state, do value count
  * Take N potential districts for each state
- [x] Create interactive US map
- [x] Store N potential schools for each state in GeoJson
- [x] Plot most active districts on interactive map

#### Saturday
- [x] TopoJson-creation pipeline
- [x] Fill table with districts when state is clicked
- [x] Link district dot with table 
- [x] Compute "activity potential" metric
- [x] Choose columns to show in D3

#### Sunday
- [x] Clean D3 code using a Mike Bostock example
- [x] Fix table-district binding
- [x] Use div to manage header and table
- [x] Style-formatting and re-arranging
- [x] Deploy on abshinn.github.io/mind-the-gap

### _Week 3_

#### Monday
- [x] Work on slides
- [x] District activity pie plot
- [x] Practice talk
- [x] Add tooltip to describe district-potential

#### Tuesday
- [x] Deploy viz as a blog page
- [x] Include potential-metrics in visualization
- [x] District similarity feature importances
- [x] Mind-the-gap dataViz write-up
- [x] Clean code

#### Wednesday
- [ ] Prepare final version of slides
- [ ] Provide information about data sources in module doc-string
- [ ] Write script which pulls down all the necessary data
- [ ] Project recommendations
- [ ] 3rd level -- show successful schools which are most similar

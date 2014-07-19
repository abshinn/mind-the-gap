Zipfian Capstone Project
===

#### _current project direction_
The idea is to be able to determine schools, districts, and US regions that can most benefit from DonorsChoose by creating a rating that describes schools as being most similar to the most active DonorsChoose schools.

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
          - overarching goal
          - histogram of projects/school
          - specific goals
      * 1 slide: what does the data look like?
          - DonorsChoose project data
          - NCES school demographics and federal aid programs
          - NCES school district state, local and federal revenue
          - NCES school expenditures
          - Census demographic/economic information by school district
      * 1 slide: methods
          - cosine-similarity
          - clustering?
      * 1 slide: results
          - find potential super-schools
          - consequence: schools like you!

#### Saturday
- [ ] Use entire NCES school data set with DonorsChoose project data to compute school similarity
      * similarity can be used to recommend new schools that are most similar to schools/areas with the highest activity
      * if not on the school level, perhaps on the district level, leveraging census demographic data
      * if time permits, recommend projects as well
- [ ] State-level data
      * [ ] rank DonorsChoose success by state
      * [ ] run classification and feature importance using wide range of financial data available
      * [ ] additional feature: median household income


### _Week 2_

- [ ] Make pretty plots
- [ ] Profit

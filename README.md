Zipfian Capstone Project
===

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
      * [x] additional feature: school/district income?
      * [ ] additional feature: median household income from census?
      * [x] compile matrix to train on
      * [x] look at correlations and scatterplot matrix
      * [x] choose arbitrary labels with which to use a decision tree classifier to find most important features
      * [x] implement decision tree classifier to determine most important features

#### Thursday-morning: feature importance
- [x] 2011 School data
      * [x] run feature importance on a variety of different 'activity' thresholds
- [x] Acquire district-level demographics

#### Thursday-afternoon: similarity and recommendations
The idea is to be able to determine schools, districts, and US regions that can most benefit from DonorsChoose by creating a rating that describes schools as being most similar to the most active DonorsChoose schools.
- [ ] Use entire NCES school data set with DonorsChoose project data to compute school similarity
      * similarity can be used to recommend new schools that are most similar to schools/areas with the highest activity
      * if not on the school level, perhaps on the district level, leveraging census demographic data
- [ ] Put together slides on progress

#### Friday
- [ ] State-level data
      * [ ] rank DonorsChoose success by state
      * [ ] run classification and feature importance using wide range of financial data available
      * [ ] additional feature: median household income
- [ ] Preliminary presentation


### _Week 2_

- [ ] Make pretty plots
- [ ] Profit

Zipfian Capstone Project
===

## Project Checklist

### Week 1

#### Monday
- [x] Obtain Data
- [x] Find state-level NCES financial statistics
- [x] Find school-level NCES statistics and financial data

#### Tuesday
- [x] Merge DonorsChoose data with National Center for Education Statistics
- [x] Try and recover schools that have been dropped for not having an _NCESid
      * not an issue for 2011 at least: keep this in mind for using other years

##### _assumptions introduced_
- Grouping projects into year bins based on posted_data: Would it instead be better to go by school year?
  (Be careful with the distinction between fiscal and school years.)

#### Wednesday and Thursday
- [ ] 2011 School data:
      * [x] additional feature: school/district income?
      * [x] additional feature: median household income?
      * [x] compile matrix to train on
      * [x] look at correlations and scatterplot matrix
      * [ ] choose arbitrary labels with which to use a decision tree classifier to find most important features
      * [ ] regress on projects/school/teachers; determine most important features
      * [ ] separate active schools versus inactive and re-run feature importance analysis 
- [ ] State data:
      * rank DonorsChoose success by state
      * regress on success, find most important features
- [ ] Use entire NCES school data set with DonorsChoose project data to compute school similarity
      * similarity can be used to recommend new schools that are most similar to schools/areas with the highest activity
      * if not on the school level, perhaps on the district level, leveraging census demographic data
- [ ] Put together slides on initial EDA and analysis

##### _other blurbs_
- [ ] Use a statistical argument for determining whether a school has a supply-gap or not
- [ ] EDA of school activity on DonorsChoose
      * proportional to projects/teachers/year/school
      * compare school groups that are one and two standard deviations below the yearly mean/metric
      * matplotlib US Map of supply gap locations

#### Friday
- [ ] Preliminary presentation


### Week 2

- [ ] Make pretty plots
- [ ] Profit

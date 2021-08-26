# Asian American Journalism Association Voices Investigative Project 2021 - Student Newsroom Leadership Diversity

Data publication and documentation for the 2021 AAJA investigative project: ***Few Black and Latinx students are editors of top college newspapers, original survey finds.***

*By: Janice Kai Chen, Ilena Peng, Jasen Lo, Trisha Ahmed, Simon J. Levien and Devan Karp*

## Project goal

To understand the state of student newsroom leadership diversity and which racial groups are over- or under-represented as student newsroom leaders, AAJA Voices 
compared demographic data we collected from student newsroom editors-in-chief against the demographic data of the colleges that the surveyed EICs attend. 


**Of 73 editors-in-chief at award-winning college newsrooms in the Spring 2021 semester, less than 6 percent were Black, and approximately 10 percent were Latinx — significantly less than their share of the college population.**


## Project notes

These newspapers were chosen because they were recognized for their excellence in 2020 by the Associated Collegiate Press’s Newspaper Pacemaker Awards and the Society of Professional Journalists’ Regional Mark of Excellence Awards for Best All-Around Student Newspapers as winners and finalists. 73 EICs representing 66 of the surveyed newsrooms responded to AAJA Voices’ survey. AAJA Voices aggregated racial demographic data of their schools’ undergraduate student population from the National Center for Education Statistics' (NCES) most recent survey of American colleges. 

### Data sources

- College demographic data are from the [National Center for Education Statistics' Integrated Postsecondary Education Data System](https://nces.ed.gov/ipeds/use-the-data) is available in `data/source`.
- EIC demographic data was collected via a Google Forms survey and subsequently compiled in Google Sheets. All personal identifiable information (PII) collected was redacted. Race and ethnicity of each of the publications' EICs are available in `data/public`. Compensation and weekly hours worked data are published in `data/manual`, although publication and school names are redacted in these data because of PII and data privacy concerns. 

*Please contact (<jasenlo123@gmail.com>)/[@jasenlo123](https://github.com/jasenlo123) for any inquiries about the methodology or data used in this project.*

## Technical
ETL scripts help generate `csv` files in `data/processed` that are used to generate graphics using [Datawrapper](https://www.datawrapper.de). 

## Data notes
- Where 2020 student demographic data was not available, 2019 data was used. This was the case for Eastfield College.
- Non-alien residents and students of unknown racial background were excluded from student demographic data aggregation. 
- Although the editors-in-chief of the Calgary Journal are included in the survey data, Mount Royal University's demographic data are not accounted for in the student demographic data because it is based in Calgary, Canada. NCES only surveys colleges in the United States. 
- Only the data for the schools of the 66 newsrooms editors-in-chief that responded to our survey were included in the aggregated data.
- `data/source` uses the NCES racial category 'Hispanic', while `data/processed` and `data/public` uses 'Latinx'.

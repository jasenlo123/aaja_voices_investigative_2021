import pandas as pd

df_spring_21 = pd.read_csv("data/manual/survey_race.csv")
df_NCES_demo = pd.read_csv("data/source/nces_race.csv")

#find list of schools in responses
ls_names = df_spring_21['school_name']

#remove schools that did not respond from NCES data
condition = df_NCES_demo['institution name'].isin(ls_names)
print(f'{len(df_NCES_demo[~condition])} out of {len(df_NCES_demo) + 1} newsrooms failed to respond.')
print(df_NCES_demo[~condition]['institution name'])
df_NCES_demo = df_NCES_demo[condition]

#count
num_asian = df_NCES_demo['EFFY2020.Asian total'].sum()
num_native = df_NCES_demo['EFFY2020.American Indian or Alaska Native total'].sum()
num_black = df_NCES_demo['EFFY2020.Black or African American total'].sum()
num_mixed = df_NCES_demo['EFFY2020.Two or more races total'].sum()
num_islander = df_NCES_demo['EFFY2020.Native Hawaiian or Other Pacific Islander total'].sum()
num_white = df_NCES_demo['EFFY2020.White total'].sum()
num_hispanic = df_NCES_demo['EFFY2020.Hispanic or Latino total'].sum()


ls_NCES_count = [num_asian,
                 num_native,
                 num_black,
                 num_mixed,
                 num_islander,
                 num_white,
                 num_hispanic
                ]

ls_NCES_races = ['Asian',
                      'American Indian or Alaska Native',
                      'Black',
                      'Two or more races',
                      'Native Hawaiian or other Pacific Islander',
                      'White',
                      'Hispanic']

df_NCES_demo = pd.DataFrame(list(zip(ls_NCES_races,ls_NCES_count)), columns=['Race','Count'])

#ADDING 0 TO RACES WITHOUT DATA IN SURVEY DATAFRAME 
ls_values = list(df_spring_21['single_race'].value_counts())
ls_races = df_spring_21['single_race'].value_counts().index.tolist()
#iterating through unique single races in NCES
for race in ls_NCES_races:
    #if each single race is not in df
    if race not in ls_races:
        ls_races.append(race)
        ls_values.append(0)

#create dataframe of single race data        
df_single_race = pd.DataFrame(list(zip(ls_races, ls_values)),
               columns =['Race', 'Count'])

#indicate data source and sort
df_single_race['Data'] = 'Survey'
df_single_race = df_single_race.sort_values(by=['Race'],ascending=True)
df_NCES_demo['Data'] = 'NCES'
df_NCES_demo = df_NCES_demo.sort_values(by=['Race'],ascending=True)

#replace hispanic with latinx
df_single_race = df_single_race.append(df_NCES_demo).replace({'Hispanic': 'Latinx'}, regex=True)

#export
df_single_race.to_csv('data/processed/single_race.csv',index=False)

#create dataframe for multiple racial identities (nerd box)
ls_values_multi = list(df_spring_21['multi_race'].value_counts())
ls_races_multi = df_spring_21['multi_race'].value_counts().index.tolist()
df_multi_race = pd.DataFrame(list(zip(ls_races_multi, ls_values_multi)),
               columns =['Race', 'Count'])

#replace hispanic with latinx
df_multi_race = df_multi_race.replace({'Hispanic': 'Latinx'}, regex=True)

#export
df_multi_race.to_csv('data/processed/multi_race.csv',index=False)

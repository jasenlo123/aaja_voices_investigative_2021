import pandas as pd

spring_21 = pd.read_csv("data/manual/survey_wages_hours.csv")

spring_21 = spring_21[~spring_21.work_hours.astype(str).str.contains("nan")]
spring_21.work_hours = pd.to_numeric(spring_21.work_hours)
bins = range(0,90,5)

spring_21['bins'] = pd.cut(spring_21.work_hours, bins)
ls_bin_index = spring_21['bins'].value_counts(sort = False).index

ls_in_bin = list(spring_21['bins'].value_counts(sort = False))
ls_bin_mid = [(a.left + a.right)/2 for a in ls_bin_index ]

print(ls_in_bin)
print(ls_bin_mid)

for i in range(len(ls_bin_mid)):
    for number in range(1,ls_in_bin[i]+1):
      print(f"{number};{ls_bin_mid[i]}")

print(f'Respondents:{len(spring_21)}')
spring_21.work_hours.to_csv('data/processed/hours.csv',index=False)

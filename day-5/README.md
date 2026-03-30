# training--2026

## Result 
1. Survival Counts:
Survived
0    549
1    342
Name: count, dtype: int64

Percentages:
Survived
0    61.62
1    38.38
Name: proportion, dtype: float64 

2. Survival Rate by Class (%):
Pclass
1    62.96
2    47.28
3    24.24
Name: Survived, dtype: float64 

3. Average Age:
Survived
0    30.63
1    28.34
Name: Age, dtype: float64 

4. Survival Rate by Embarkation Port (%):
Embarked
C    55.36
Q    38.96
S    33.70
Name: Survived, dtype: float64 

5. Missing Age Values: 177
Missing ages filled using median per class.

6. Oldest Survivor:
Name: Barkworth, Mr. Algernon Henry Wilson
Age: 80.0
Class: 1

7. Survival Rate by Gender (%):
Sex
female    74.20
male      18.89
Name: Survived, dtype: float64 

8. Survival Rate by Age Group (%):
AgeGroup
Adult     36.44
Child     53.98
Senior    26.92
Name: Survived, dtype: float64 

9. 3rd Class Survival Rate by Gender (%):
Sex
female    50.00
male      13.54
Name: Survived, dtype: float64 

10. Cabin Data Cleaning:
Remaining Rows: 204
Percentage Kept: 22.90%


## Most Surprising Finding
The biggest surprise was how strong the gender effect was — women had a significantly higher survival rate than men. This clearly reflects the "women and children first" evacuation priority.

## What I Would Investigate Next
- Survival rate by fare price (wealth correlation)
- Build a simple ML model to predict survival
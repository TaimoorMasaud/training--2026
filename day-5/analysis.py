import pandas as pd

# Load dataset
df = pd.read_csv("titanic.csv")


# Total passengers
total_passengers = len(df)

# 01. How many passengers survived vs. didn't? Show as counts and percentages.
survival_counts = df["Survived"].value_counts()
survival_percent = df["Survived"].value_counts(normalize=True) * 100

print("1. Survival Counts:")
print(survival_counts)
print("\nPercentages:")
print(survival_percent.round(2), "\n")


# 02. What was the survival rate by passenger class (1st, 2nd, 3rd)?
class_survival = df.groupby("Pclass")["Survived"].mean() * 100

print("2. Survival Rate by Class (%):")
print(class_survival.round(2), "\n")


# 03. Average age of survivors vs. non-survivors.
avg_age = df.groupby("Survived")["Age"].mean()

print("3. Average Age:")
print(avg_age.round(2), "\n")


# 04. Which embarkation port had the highest survival rate?
embark_survival = df.groupby("Embarked")["Survived"].mean() * 100

print("4. Survival Rate by Embarkation Port (%):")
print(embark_survival.round(2), "\n")


# 05. How many passengers have missing age values? Fill missing ages with the median age for that passenger class.
missing_age = df["Age"].isna().sum()

print(f"5. Missing Age Values: {missing_age}")

# Fill missing ages with median per class
df["Age"] = df.groupby("Pclass")["Age"].transform(
    lambda x: x.fillna(x.median())
)

print("Missing ages filled using median per class.\n")


# 06. Who was the oldest surviving passenger? Print their name, age, class.
oldest_survivor = df[df["Survived"] == 1].sort_values(by="Age", ascending=False).iloc[0] # iloc gets first row

print("6. Oldest Survivor:")
print(f"Name: {oldest_survivor['Name']}")
print(f"Age: {oldest_survivor['Age']}")
print(f"Class: {oldest_survivor['Pclass']}\n")


# 07. What % of women survived vs. what % of men?
gender_survival = df.groupby("Sex")["Survived"].mean() * 100

print("7. Survival Rate by Gender (%):")
print(gender_survival.round(2), "\n")


# 08. Create a new column 'AgeGroup': Child (<18), Adult (18-60), Senior (60+). Show survival rate per group.
def age_group(age):
    if age < 18:
        return "Child"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

df["AgeGroup"] = df["Age"].apply(age_group)

agegroup_survival = df.groupby("AgeGroup")["Survived"].mean() * 100

print("8. Survival Rate by Age Group (%):")
print(agegroup_survival.round(2), "\n")


# 09. Among 3rd class passengers, what was the survival rate for men vs. women?
third_class = df[df["Pclass"] == 3]
third_gender_survival = third_class.groupby("Sex")["Survived"].mean() * 100

print("9. 3rd Class Survival Rate by Gender (%):")
print(third_gender_survival.round(2), "\n")


# 10. Drop all rows with missing Cabin data. How many rows remain? What % of original data did you keep?
original_count = len(df)
df_cabin = df.dropna(subset=["Cabin"])
remaining_count = len(df_cabin)

percentage_kept = (remaining_count / original_count) * 100

print("10. Cabin Data Cleaning:")
print(f"Remaining Rows: {remaining_count}")
print(f"Percentage Kept: {percentage_kept:.2f}%\n")


import pandas as pd

# ---------------------------------------------------------
# READ EXCEL FILE
# ---------------------------------------------------------
# Dataset structure:
# name | profession

df = pd.read_excel("data.xlsx")

# Print full dataset
print("Full Dataset:")
print(df)



# =========================================================
# 1. READ SINGLE COLUMN
# =========================================================

# Get all names
names = df["name"]

print("\nAll Names:")
print(names)



# Get all professions
professions = df["profession"]

print("\nAll Professions:")
print(professions)



# =========================================================
# 2. READ SINGLE ROW (by index)
# =========================================================

# First row (Ebrahim)
first_row = df.iloc[0]

print("\nFirst Row Data:")
print(first_row)



# =========================================================
# 3. READ SPECIFIC CELL VALUE
# =========================================================

# Row 0, Column 1 → profession of Ebrahim
cell_value = df.iloc[0, 1]

print("\nSpecific Cell Value (Profession of first user):")
print(cell_value)



# =========================================================
# 4. FILTER DATA (VERY IMPORTANT IN SQA)
# =========================================================

# Get only SQA professionals
sqa_only = df[df["profession"] == "SQA"]

print("\nSQA Professionals:")
print(sqa_only)



# =========================================================
# 5. READ SINGLE VALUE USING CONDITION (BEST PRACTICE)
# =========================================================

# Get profession of a specific person
ebrahim_profession = df.loc[df["name"] == "Ebrahim", "profession"].values[0]

print("\nEbrahim Profession:", ebrahim_profession)



# =========================================================
# 6. FIND NON-SQA USERS (REAL QA VALIDATION CASE)
# =========================================================

non_sqa = df[df["profession"] != "SQA"]

print("\nNon-SQA Users:")
print(non_sqa)



# =========================================================
# 7. LOOP THROUGH DATASET (AUTOMATION STYLE)
# =========================================================

print("\nIterating Dataset:")

for index, row in df.iterrows():
    print(f"User: {row['name']} | Profession: {row['profession']}")
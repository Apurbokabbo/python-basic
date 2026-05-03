import pandas as pd

# ---------------------------------------------------------
# CREATE TEST DATA
# ---------------------------------------------------------
# In QA automation, this can represent:
# - test users
# - test execution results
# - API test data
# - regression dataset

data = {
    'Name': ['Ebrahim', 'Test', 'Sazzad'],
    'Age': [50, 55, 55]
}

# Convert dictionary to DataFrame (tabular structure)
df = pd.DataFrame(data)

# Print dataset (for verification)
print("Generated Test Data:")
print(df)



# =========================================================
# EXPORT DATA TO EXCEL
# =========================================================

df.to_excel('output.xlsx', index=False)

# index=False → prevents extra index column in Excel



# =========================================================
# LEAD SQA EXPLANATION
# =========================================================

# ✔ This code is used in automation frameworks for:
#    - saving test execution results
#    - generating QA reports
#    - exporting API validation results
#    - storing regression test data

# ✔ DataFrame → structured test dataset
# ✔ to_excel() → output layer for reporting



# =========================================================
# REAL SQA AUTOMATION USE CASES
# =========================================================

# Example 1: Save test execution results
results = {
    "TestCase": ["TC_Login", "TC_Logout", "TC_Signup"],
    "Status": ["Pass", "Fail", "Pass"]
}

df_results = pd.DataFrame(results)
df_results.to_excel("test_results.xlsx", index=False)


# Example 2: Save API validation report
api_report = {
    "Endpoint": ["/login", "/user", "/order"],
    "ResponseCode": [200, 200, 500]
}

df_api = pd.DataFrame(api_report)
df_api.to_excel("api_report.xlsx", index=False)


# Example 3: Save performance test results
performance = {
    "API": ["login", "search", "payment"],
    "ResponseTime(ms)": [120, 300, 800]
}

df_perf = pd.DataFrame(performance)
df_perf.to_excel("performance_report.xlsx", index=False)



# =========================================================
# KEY TAKEAWAYS (LEAD SQA LEVEL)
# =========================================================

# ✔ DataFrame = test data structure
# ✔ to_excel() = reporting/output layer
# ✔ index=False = clean Excel output

# ✔ Used in real automation for:
#    - test reports
#    - CI/CD pipelines
#    - API validation reports
#    - regression result tracking

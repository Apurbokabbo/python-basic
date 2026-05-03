# =========================================================
# LOOPING THROUGH TUPLE (SQA AUTOMATION CONTEXT)
# =========================================================

# Tuple is:
# ✔ Ordered
# ✔ Immutable (cannot be modified)
# ✔ Supports iteration like list

programming = ("Python", "Java", "C#", "C++", "Javascript")


# ---------------------------------------------------------
# METHOD 1: DIRECT ITERATION (BEST PRACTICE)
# ---------------------------------------------------------
# Most readable and commonly used in automation scripts

for item in programming:
    print(item)



# ---------------------------------------------------------
# METHOD 2: INDEX-BASED LOOP (USING range + len)
# ---------------------------------------------------------
# Useful when index position is required in logs or reporting

for i in range(len(programming)):
    print(programming[i])



# =========================================================
# LEAD SQA REAL-WORLD USE CASES
# =========================================================

# Example 1: Iterating API response fields (fixed structure)
api_response = ("200", "Success", "User Created")

for item in api_response:
    print("API Field:", item)


# Example 2: Validate test case metadata
test_case = ("TC_Login", "High", "Regression")

for detail in test_case:
    print("Test Case Detail:", detail)


# Example 3: Logging execution steps (automation logs)
execution_steps = ("Open Browser", "Enter URL", "Click Login", "Verify Dashboard")

for step in execution_steps:
    print("Step:", step)


# Example 4: Index-based reporting (useful in debugging)
for i in range(len(execution_steps)):
    print(f"Step {i+1}: {execution_steps[i]}")



# =========================================================
# LEAD SQA KEY TAKEAWAYS
# =========================================================

# ✔ Tuple is used when data is FIXED (immutable)
# ✔ Looping is used for:
#    - API response validation
#    - execution step tracking
#    - test metadata reading
#    - structured logging

# ✔ Two ways to loop:
#    - for item in tuple → best practice (clean & readable)
#    - for i in range(len()) → when index is required

# ✔ In automation frameworks:
#    Tuples are used for:
#    - constants
#    - API responses
#    - configuration data
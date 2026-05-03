# =========================================================
# LOOPING THROUGH A SET (SQA AUTOMATION CONTEXT)
# =========================================================

programming = {"Python", "Java", "C#", "C++", "Javascript"}

# ---------------------------------------------------------
# IMPORTANT CONCEPT
# ---------------------------------------------------------
# A SET is:
# - unordered (no fixed sequence)
# - does NOT support indexing
# - automatically removes duplicates

# So we can ONLY iterate through it using a loop


# ---------------------------------------------------------
# LOOPING THROUGH SET
# ---------------------------------------------------------
# Used in QA automation when:
# - validating API fields
# - processing dynamic test data
# - iterating feature lists

for language in programming:
    print(language)



# =========================================================
# SQA REAL-WORLD USE CASES
# =========================================================

# Example 1: API response field validation
api_fields = {"id", "name", "email", "status"}

for field in api_fields:
    print("Validating field:", field)


# Example 2: Validate supported features in system
supported_features = {"login", "search", "payment"}

for feature in supported_features:
    print("Checking feature availability:", feature)


# Example 3: Remove duplicate test cases and execute
test_cases = {"TC_Login", "TC_Logout", "TC_Login"}

for tc in test_cases:
    print("Executing Test Case:", tc)
# duplicates automatically removed


# Example 4: Loop through defect IDs
defect_ids = {101, 102, 103}

for bug in defect_ids:
    print("Processing Bug ID:", bug)



# =========================================================
# LEAD SQA KEY TAKEAWAYS
# =========================================================

# ✔ Sets are used when order does NOT matter
# ✔ Automatically removes duplicates (very important in QA)
# ✔ Best for:
#    - API validation
#    - test case uniqueness
#    - feature verification
#    - defect tracking

# ✔ Limitation:
#    - No indexing
#    - No slicing
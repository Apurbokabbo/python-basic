# =========================================================
# SET - ADD & UPDATE OPERATIONS (SQA AUTOMATION CONTEXT)
# =========================================================

programming = {"Python", "Java", "C#", "C++", "Javascript"}

# ---------------------------------------------------------
# add() -> Adds a SINGLE element to the set
# ---------------------------------------------------------
# Used in automation when adding a new feature/module dynamically

programming.add("Go")
print("After add:", programming)
# Output: set now includes "Go"


# ---------------------------------------------------------
# update() -> Adds MULTIPLE elements to the set
# ---------------------------------------------------------
# Used when merging feature lists, test suites, or data sets

programming.update(["HTML", "CSS"])
# OR programming.update({"HTML", "CSS"})

print("After update:", programming)


# ---------------------------------------------------------
# DUPLICATE HANDLING (VERY IMPORTANT IN SQA)
# ---------------------------------------------------------
# Sets automatically ignore duplicates

programming.add("Python")
# Python already exists → no change in set

print("After adding duplicate:", programming)



# =========================================================
# LEAD SQA EXPLANATION (REAL WORLD USAGE)
# =========================================================

# ✔ add() is used when:
#    - adding a new test case
#    - adding a new feature flag
#    - inserting a new API field

# ✔ update() is used when:
#    - merging regression + smoke suites
#    - combining API response fields
#    - adding multiple test data inputs

# ✔ duplicate handling:
#    - critical in automation to avoid redundant test execution
#    - ensures clean test coverage
#    - prevents double counting in reports


# =========================================================
# REAL SQA EXAMPLE (TEST SUITE MANAGEMENT)
# =========================================================

smoke_tests = {"TC_Login", "TC_Logout"}
regression_tests = {"TC_Payment", "TC_Search"}

# Merge all test cases for full execution cycle
all_tests = smoke_tests.copy()
all_tests.update(regression_tests)

print("Final Test Suite:", all_tests)


# =========================================================
# KEY TAKEAWAYS (LEAD LEVEL)
# =========================================================

# 1. set.add() → single item insertion
# 2. set.update() → bulk insertion
# 3. duplicates are automatically removed (VERY IMPORTANT in QA)
# 4. sets are ideal for:
#    - test suite management
#    - API field validation
#    - deduplication of test data
#    - comparison between expected vs actual results
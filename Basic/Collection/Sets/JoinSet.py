# =========================================================
# SET OPERATIONS - UNION, INTERSECTION, DIFFERENCE
# (USED IN SQA AUTOMATION TESTING)
# =========================================================

set1 = {"Python", "Java", "C#", "C++", "Javascript"}
set2 = {"Go", "HTML", "CSS", "Javascript"}


# ---------------------------------------------------------
# UNION (|) or union()
# ---------------------------------------------------------
# Combines both sets and removes duplicates automatically
# Used in QA for merging test suites or feature lists

joined_set = set1.union(set2)

print("Union (All Features/Test Cases):", joined_set)
# Output: All unique items from both sets


# ---------------------------------------------------------
# INTERSECTION (&) or intersection()
# ---------------------------------------------------------
# Returns ONLY common elements between two sets
# Used in QA to find:
# - common test coverage
# - overlapping features
# - shared API fields

joined_set2 = set1.intersection(set2)

print("Intersection (Common Items):", joined_set2)
# Output: {'Javascript'}


# ---------------------------------------------------------
# DIFFERENCE (-) or difference()
# ---------------------------------------------------------
# Returns items present in set1 but NOT in set2
# Used in QA to find:
# - missing test cases
# - new features not yet in regression
# - differences between API versions

diff_set = set1.difference(set2)

print("Difference (Only in Set1):", diff_set)
# Output: items in set1 excluding common ones



# =========================================================
# LEAD SQA REAL-WORLD SCENARIO
# =========================================================

# Example: API TESTING COMPARISON

expected_fields = {"id", "name", "email", "status", "created_at"}
actual_fields   = {"id", "name", "email"}

# Missing fields in API response (CRITICAL IN QA)
missing_fields = expected_fields.difference(actual_fields)

print("Missing API Fields:", missing_fields)


# Example: Common test coverage between smoke and regression
smoke = {"TC_Login", "TC_Search", "TC_Logout"}
regression = {"TC_Search", "TC_Payment"}

common_tests = smoke.intersection(regression)

print("Common Test Cases:", common_tests)


# Example: Full test execution plan
full_suite = smoke.union(regression)

print("Full Test Suite:", full_suite)

# =========================================================
# SET OPERATIONS WITH NUMBERS (SQA AUTOMATION CONTEXT)
# =========================================================

set1 = {10, 20, 30, 40, 50, 60}
set2 = {40, 50, 60, 70, 80, 90}


# ---------------------------------------------------------
# UNION - Combine all unique numeric values
# ---------------------------------------------------------
# Used in QA for combining performance metrics, logs, or IDs

union_set = set1.union(set2)
print("Union (All Unique Numbers):", union_set)
# Output: {10, 20, 30, 40, 50, 60, 70, 80, 90}


# ---------------------------------------------------------
# INTERSECTION - Common numeric values
# ---------------------------------------------------------
# Used to find overlapping:
# - API response IDs
# - common performance metrics
# - shared test execution IDs

common_set = set1.intersection(set2)
print("Intersection (Common Numbers):", common_set)
# Output: {40, 50, 60}


# ---------------------------------------------------------
# DIFFERENCE - Values only in set1
# ---------------------------------------------------------
# Used to find:
# - missing data in API response
# - failed vs passed execution mismatch
# - new vs old dataset comparison

diff_set = set1.difference(set2)
print("Difference (Set1 - Set2):", diff_set)
# Output: {10, 20, 30}


# ---------------------------------------------------------
# SYMMETRIC DIFFERENCE - Unique to both sets
# ---------------------------------------------------------
# Used in QA to detect ALL mismatches between systems

sym_diff = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff)
# Output: {10, 20, 30, 70, 80, 90}



# =========================================================
# REAL SQA AUTOMATION USE CASES WITH NUMBERS
# =========================================================

# Example 1: API response time comparison (performance testing)
expected_response_times = {100, 200, 300, 400}
actual_response_times   = {200, 300, 500}

slow_endpoints = actual_response_times.difference(expected_response_times)

print("Slow or Unexpected Response Times:", slow_endpoints)


# Example 2: Test execution IDs comparison
expected_test_ids = {101, 102, 103, 104}
executed_test_ids = {102, 103, 105}

missing_tests = expected_test_ids.difference(executed_test_ids)
extra_tests   = executed_test_ids.difference(expected_test_ids)

print("Missing Tests:", missing_tests)
print("Unexpected Extra Tests:", extra_tests)


# Example 3: Performance overlap validation
baseline_metrics = {50, 100, 150, 200}
current_metrics  = {100, 150, 250, 300}

stable_metrics = baseline_metrics.intersection(current_metrics)

print("Stable Performance Metrics:", stable_metrics)


# Example 4: Full regression vs smoke numeric IDs
smoke_ids = {1, 2, 3, 4}
regression_ids = {3, 4, 5, 6}

full_suite = smoke_ids.union(regression_ids)

print("Full Execution Suite:", full_suite)



# =========================================================
# KEY TAKEAWAYS (LEAD QA LEVEL)
# =========================================================

# ✔ union() → combine everything (deduplicated)
# ✔ intersection() → find common coverage
# ✔ difference() → find missing / extra items

# ✔ In Automation Frameworks:
#    - Used for API validation (expected vs actual JSON)
#    - Used for test suite optimization
#    - Used for regression coverage analysis
#    - Used for defect analysis between builds
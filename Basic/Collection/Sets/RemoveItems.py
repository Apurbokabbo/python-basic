# =========================================================
# SET REMOVAL OPERATIONS (SQA AUTOMATION CONTEXT)
# =========================================================

programming = {"Python", "Java", "C#", "C++", "Javascript"}


# ---------------------------------------------------------
# remove() -> removes a specific item (STRICT)
# ---------------------------------------------------------
# ⚠️ If item does NOT exist → raises KeyError
# Used in QA when we are 100% sure data exists

programming.remove("Python")
print("After remove:", programming)



# ---------------------------------------------------------
# discard() -> removes item safely (NO ERROR)
# ---------------------------------------------------------
# ✔ If item exists → removes it
# ✔ If item NOT exists → does NOTHING (no crash)

programming.discard("Python")
# Python already removed → no error

print("After discard:", programming)



# ---------------------------------------------------------
# pop() -> removes RANDOM item (since set is unordered)
# ---------------------------------------------------------
# ✔ Returns removed item
# ⚠️ Useful when we just need to consume data

removed_item = programming.pop()

print("Removed Item:", removed_item)
print("After pop:", programming)



# ---------------------------------------------------------
# clear() -> removes ALL elements
# ---------------------------------------------------------
# Used in QA for:
# - resetting test data
# - cleaning execution cache
# - preparing fresh test runs

programming.clear()

print("After clear:", programming)
# Output: set()



# ---------------------------------------------------------
# del -> deletes entire variable (NOT USED HERE)
# ---------------------------------------------------------
# del programming
# After this, variable no longer exists (NameError if accessed)



# =========================================================
# SQA REAL-WORLD USE CASES
# =========================================================

# Example 1: Clean API response fields (remove unwanted data)
api_fields = {"id", "name", "debug_info", "status"}

api_fields.remove("debug_info")

print("Clean API Fields:", api_fields)


# Example 2: Safe removal of optional field
api_fields.discard("optional_field")  # no crash if missing


# Example 3: Process test cases dynamically
test_cases = {"TC_Login", "TC_Logout", "TC_Signup"}

executed_test = test_cases.pop()

print("Executed Test Case:", executed_test)


# Example 4: Reset test execution data
execution_log = {"TC1", "TC2", "TC3"}

execution_log.clear()

print("Reset Execution Log:", execution_log)



# =========================================================
# LEAD SQA KEY DIFFERENCES
# =========================================================

# remove()   → strict (fails if missing)
# discard()  → safe (no error if missing)
# pop()      → removes random item + returns it
# clear()    → empties the set
# del        → deletes entire object

# =========================================================
# WHEN TO USE IN AUTOMATION
# =========================================================

# ✔ remove()  → validated data cleanup
# ✔ discard() → optional/uncertain data cleanup
# ✔ pop()     → dynamic processing of test data
# ✔ clear()   → reset between test runs
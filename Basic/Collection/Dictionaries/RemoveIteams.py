# =========================
# REMOVING ITEMS FROM DICTIONARY
# =========================

person = {
    "name": "Ebrahim",
    "age": 50,
    "gender": "Male",
    "language": "Bangla",
    "country": "BD",
    "city": "Dhaka",
    "profession": "SQA",
    "email": "test@noemail.com ",
    "phone": "123654789",
}

# =========================
# pop() -> remove by KEY
# =========================
# Removes the key and RETURNS its value

removed_value = person.pop("age")

print("Removed Age:", removed_value)
print("After pop:", person)



# =========================
# popitem() -> removes LAST inserted item
# =========================
# Returns (key, value) as a tuple

removed_value2 = person.popitem()

print("Removed Item:", removed_value2)
print("After popitem:", person)



# =========================
# del -> delete specific key
# =========================
del person["city"]

print("After del:", person)



# =========================
# clear() -> remove ALL items
# =========================
person.clear()

print("After clear:", person)
# Output: {}



# =========================
# del person -> delete entire variable
# =========================
del person

# ⚠️ After this, person no longer exists
# print(person) -> would give ERROR (NameError)



# =========================
# IMPORTANT DIFFERENCES
# =========================

# pop("key")     -> removes specific key + returns value
# popitem()      -> removes last inserted item
# del dict[key]  -> deletes key (no return value)
# clear()        -> empties dictionary
# del dict       -> deletes entire dictionary variable



# =========================
# SQA ENGINEER RELATED EXAMPLES
# =========================

# Example 1: Remove unwanted API field
api_response = {
    "status": 200,
    "message": "Success",
    "debug_info": "internal logs"
}

# Remove debug info before validation
removed_debug = api_response.pop("debug_info")

print("Clean API Response:", api_response)


# Example 2: Remove last test execution entry
test_logs = {
    "TC1": "pass",
    "TC2": "fail",
    "TC3": "pass"
}

last_entry = test_logs.popitem()

print("Last Execution:", last_entry)
print("Remaining Logs:", test_logs)


# Example 3: Delete deprecated field in API testing
user_data = {
    "id": 101,
    "name": "QA User",
    "old_field": "deprecated"
}

del user_data["old_field"]

print("Updated User Data:", user_data)


# Example 4: Reset test data before new run
test_data = {
    "user": "admin",
    "password": "1234"
}

test_data.clear()

print("Reset Test Data:", test_data)


# =========================
# KEY LEARNING POINTS
# =========================

# 1. pop() -> remove by key + get value
# 2. popitem() -> remove last inserted item
# 3. del -> delete key or entire object
# 4. clear() -> empty dictionary
# 5. del variable -> completely removes it from memory

# =========================
# SQA USE CASES
# =========================

# - Cleaning API responses before validation
# - Removing debug/internal fields
# - Resetting test data between runs
# - Handling dynamic JSON responses
# - Log cleanup in automation testing
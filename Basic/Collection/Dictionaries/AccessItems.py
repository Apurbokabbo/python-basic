# =========================
# DICTIONARY BASICS (KEY-VALUE PAIR)
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

# Print entire dictionary
print(person)


# =========================
# ACCESSING VALUES
# =========================

# Direct access using key
print("Gender:", person["gender"])
# ⚠️ If key doesn't exist → error

# Safer way using get()
print("Language:", person.get("language"))
# If key not found → returns None (no crash)


# =========================
# DICTIONARY VIEWS
# =========================

# keys() -> returns all keys
print("Keys:", person.keys())

# values() -> returns all values
print("Values:", person.values())

# items() -> returns key-value pairs as tuples
print("Items:", person.items())


# =========================
# IMPORTANT CONCEPTS
# =========================

# Dictionary = key-value structure
# Fast lookup using keys
# Keys must be unique
# Values can be any type (string, number, list, etc.)


# =========================
# SQA ENGINEER RELATED EXAMPLES
# =========================

# Example 1: API response validation (very common in SQA)
api_response = {
    "status": 200,
    "message": "Success",
    "data": {
        "user_id": 101,
        "username": "test_user"
    }
}

# Validate status code
print("Status:", api_response["status"])

# Safe access
print("Message:", api_response.get("message"))


# Example 2: Check if key exists before validation
if "data" in api_response:
    print("Data exists in response ✔")


# Example 3: Extract all API keys (debugging)
print("API Keys:", api_response.keys())


# Example 4: Loop through response data
for key, value in api_response.items():
    print(key, "=>", value)


# Example 5: Test data management (QA use case)
test_user = {
    "username": "qa_user",
    "password": "1234",
    "role": "admin"
}

print("Login Username:", test_user.get("username"))


# Example 6: Update test data dynamically
test_user["password"] = "new_pass"
print("Updated User:", test_user)


# Example 7: Add new field (common in test setup)
test_user["environment"] = "staging"
print("With Environment:", test_user)



# =========================
# KEY DIFFERENCE
# =========================

# dict["key"]   -> direct access (can crash if missing)
# dict.get(key) -> safe access (recommended in testing)

# =========================
# KEY LEARNING POINTS
# =========================

# 1. Dictionary stores structured data (key-value)
# 2. Very important in API testing
# 3. get() prevents runtime errors
# 4. keys(), values(), items() help debugging
# 5. Common in SQA for:
#    - API validation
#    - Test data storage
#    - JSON response handling
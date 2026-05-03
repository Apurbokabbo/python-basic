# =========================
# DICTIONARY UPDATING METHODS
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

# -------------------------
# ADD NEW KEY-VALUE PAIR
# -------------------------
person["university"] = "University of Washington"
# If key does not exist → it will be added

print("After adding university:", person)


# -------------------------
# ADD KEY WITH None VALUE
# -------------------------
person["license"] = None
# None means "no value assigned" (useful in testing for missing data)

print("After adding license:", person)


# -------------------------
# setdefault() METHOD
# -------------------------
# Adds key ONLY if it does not exist
# If key already exists → it will NOT change value

person.setdefault("zipcode", "12345")

print("After setdefault:", person)



# =========================
# IMPORTANT DIFFERENCE
# =========================

# dict["key"] = value
# -> always adds or updates value

# setdefault(key, value)
# -> adds ONLY if key is missing



# =========================
# SQA ENGINEER RELATED EXAMPLES
# =========================

# Example 1: Add missing API field
api_response = {
    "status": 200,
    "message": "Success"
}

api_response["response_time"] = 120  # adding new metric
print("API Response:", api_response)


# Example 2: Handle optional field (very common in APIs)
api_response["error_code"] = None
print("With optional field:", api_response)


# Example 3: Safe default value in test data
test_user = {
    "username": "qa_user"
}

test_user.setdefault("role", "guest")
print("User with default role:", test_user)


# Example 4: Prevent overwriting existing value
test_user.setdefault("username", "new_user")
print("After setdefault attempt overwrite:", test_user)


# Example 5: Add environment info for testing
test_config = {
    "browser": "Chrome"
}

test_config["env"] = "staging"
test_config.setdefault("timeout", 30)

print("Test Config:", test_config)



# =========================
# KEY LEARNING POINTS
# =========================

# 1. dict["key"] = value → add or update
# 2. setdefault() → add only if missing
# 3. None → used for missing/unknown values
# 4. Very important in SQA for:
#    - API testing (optional fields)
#    - Test data setup
#    - JSON validation
#    - Default configuration handling
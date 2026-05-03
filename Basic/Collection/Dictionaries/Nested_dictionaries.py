# =========================
# NESTED DICTIONARY (DICTIONARY INSIDE DICTIONARY)
# =========================

information = {
    "person": {
        "name": "Ebrahim",
        "age": 50,
        "gender": "Male",
        "language": "Bangla",
        "country": "BD",
        "city": "Dhaka",
        "profession": "SQA",
        "email": "test@noemail.com ",
        "phone": "123654789",
    },

    "education": {
        "SSC": "Education",
        "HSC": "Education",
        "University": "Education",
    },

    "languages": {
        "Python": "Python",
        "Java": "Java",

        # Nested dictionary inside another dictionary
        "programming": {
            "books": "Python",
        }
    }
}

# =========================
# PRINT FULL STRUCTURE
# =========================
print(information)


# =========================
# ACCESSING NESTED DATA
# =========================

# Accessing top-level → second-level → key
print("Country:", information["person"]["country"])
# Output: BD

# Accessing nested dictionary value
print("Java Language:", information["languages"]["Java"])
# Output: Java

# Accessing deeply nested value
print("Books:", information["languages"]["programming"]["books"])
# Output: Python



# =========================
# HOW IT WORKS (STEP BY STEP)
# =========================

# information
# └── person
#     └── country → "BD"
#
# information
# └── languages
#     └── programming
#         └── books → "Python"



# =========================
# SQA ENGINEER RELATED EXAMPLES
# =========================

# Example 1: API response (VERY COMMON IN REAL SQA)
api_response = {
    "status": 200,
    "data": {
        "user": {
            "id": 101,
            "name": "QA User",
            "address": {
                "city": "Dhaka",
                "zip": "1200"
            }
        }
    }
}

print("User Name:", api_response["data"]["user"]["name"])
print("City:", api_response["data"]["user"]["address"]["city"])


# Example 2: Validate nested JSON fields
if api_response["data"]["user"]["id"] == 101:
    print("User ID is correct ✔")


# Example 3: Test configuration structure
test_config = {
    "browser": {
        "chrome": {
            "version": "120",
            "headless": True
        }
    }
}

print("Chrome Version:", test_config["browser"]["chrome"]["version"])


# Example 4: Deep validation in automation
if api_response["data"]["user"]["address"]["zip"] == "1200":
    print("Zip code is valid ✔")


# =========================
# IMPORTANT CONCEPTS
# =========================

# 1. Nested dictionary = dictionary inside dictionary
# 2. Used for structured data (JSON APIs, configs)
# 3. Access using multiple keys:
#    dict["level1"]["level2"]["level3"]

# 4. If any key is missing → KeyError (important in testing)

# Safer way in real SQA:
print(api_response.get("data", {}).get("user", {}).get("name"))



# =========================
# SQA REAL-WORLD USE CASES
# =========================

# - API response validation (JSON parsing)
# - Test environment configuration
# - Database-like structured data
# - User profile verification
# - Automation test data handling
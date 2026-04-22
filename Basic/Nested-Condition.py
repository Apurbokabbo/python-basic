# =========================================================
# NESTED IF + LOGICAL OPERATORS
# =========================================================

# =========================
# Example 1: Voting System (Improved Logic)
# =========================

age = 20
citizenship = "Dhaka"
zone = "Dhanmondi"

if citizenship == "Dhaka":

    if age >= 18:

        # FIXED LOGIC: consistent zone check
        if zone == "Dhanmondi":
            print("You are allowed to vote in Dhaka (Dhanmondi zone)")
        else:
            print("You are NOT in a valid voting zone")

    else:
        print("You are under 18, not allowed to vote")

elif citizenship == "Sylet":

    if age >= 18:
        print("You are allowed to vote in Sylet")
    else:
        print("You are under 18, not allowed to vote in Sylet")

else:
    print("You are not allowed to vote in Bangladesh")


# =========================
# Example 2: Login System (Nested Validation)
# =========================

username = "admin"
password = "1234"
role = "tester"

if username == "admin":

    if password == "1234":

        if role == "tester":
            print("Login Successful: Tester Access")
        else:
            print("Login Successful: Limited Access")

    else:
        print("Wrong Password")

else:
    print("User Not Found")


# =========================
# Example 3: E-commerce Discount System
# =========================

is_member = True
total_amount = 6000

if is_member:

    if total_amount >= 5000:
        print("You get 20% discount")

    elif total_amount >= 2000:
        print("You get 10% discount")

    else:
        print("You get 5% discount")

else:
    print("No discount for non-members")


# =========================
# Example 4: Exam Eligibility System
# =========================

attendance = 85
fee_paid = True

if fee_paid:

    if attendance >= 75:
        print("Eligible for exam")
    else:
        print("Not eligible: Low attendance")

else:
    print("Not eligible: Fee not paid")


# =========================
# Example 5: API Access Control (SQA REAL CASE)
# =========================

api_key_valid = True
user_role = "admin"
request_limit = 100

if api_key_valid:

    if user_role == "admin":

        if request_limit > 0:
            print("API Access Granted")
        else:
            print("Request limit exceeded")

    else:
        print("Access Denied: Not Admin")

else:
    print("Invalid API Key")


# =========================
# Example 6: AND / OR Conditions (Simplified Logic)
# =========================

age = 25
citizenship = "Dhaka"
zone = "Dhanmondi"

# Using AND (all conditions must be true)
if (age >= 18) and (citizenship == "Dhaka") and (zone == "Dhanmondi"):
    print("Allowed (AND condition passed)")
else:
    print("Not allowed (AND condition failed)")


# Using OR (any condition can be true)
if (age < 18) or (citizenship != "Dhaka"):
    print("Restricted Access (OR condition triggered)")


# =========================
# Example 7: Travel Eligibility System
# =========================

passport_valid = True
visa_approved = True
age = 22

if passport_valid:

    if visa_approved:

        if age >= 18:
            print("You can travel")
        else:
            print("Underage traveler")

    else:
        print("Visa not approved")

else:
    print("Invalid passport")


# =========================
# IMPORTANT LEARNING POINTS
# =========================

# 1. Nested IF = step-by-step validation flow
# 2. AND = all conditions must be TRUE
# 3. OR = any one condition can be TRUE
# =========================================================
# MODIFYING A TUPLE (SQA AUTOMATION CONTEXT)
# =========================================================

# IMPORTANT:
# Tuple is IMMUTABLE → cannot be changed directly
# So we use a workaround: convert → modify → convert back

programming = ("Python", "Java", "C#", "C++", "Javascript")


# ---------------------------------------------------------
# STEP 1: CONVERT TUPLE TO LIST
# ---------------------------------------------------------
# Reason: List is mutable (can be changed)

x = list(programming)


# ---------------------------------------------------------
# STEP 2: MODIFY THE LIST
# ---------------------------------------------------------

# Update existing value
x[1] = "Go"
# Java → Go

# Add new value
x.append("HTML")


# ---------------------------------------------------------
# STEP 3: CONVERT BACK TO TUPLE
# ---------------------------------------------------------
programming = tuple(x)

print(programming)
# Output: ('Python', 'Go', 'C#', 'C++', 'Javascript', 'HTML')


api_response = ("200", "Success", "OldValue")

data = list(api_response)
data[2] = "NewValue"
api_response = tuple(data)

print(api_response)


# Config adjustment in automation
config = ("Chrome", "Windows", "v120")

cfg = list(config)
cfg[2] = "v121"
config = tuple(cfg)

print(config)
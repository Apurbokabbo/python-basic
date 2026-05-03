# =========================
# BUILT-IN FUNCTIONS EXAMPLES
# =========================

# max() -> returns the largest value
print("Max:", max(1, 4, 22, 21, 5, 3, 9))   # Output: 22

# min() -> returns the smallest value
print("Min:", min(1, 4, 22, 21, 5, 3, 9))   # Output: 1

# round() -> rounds a number to given decimal places
print("Round:", round(3.141623432, 2))   # Output: 3.14

# sum() -> adds all elements in a list
print("Sum of List:", sum([1,2,3,4,5,6,7,8,9,10]))   # Output: 55

# len() -> returns total number of elements
print(len([1,2,3,4,5,6,7,8,9,10]))   # Output: 10

# len() also works with strings (counts characters)
print(len("Hello"))   # Output: 5

# sorted() -> returns a new sorted list
print(sorted([3,6,5,1,8,9]))   # Output: [1, 3, 5, 6, 8, 9]


# =========================
# AVERAGE CALCULATION
# =========================

numbers = [1,2,3,4,5,6,7,8,9,10]

# Formula: average = total sum / total count
average = sum(numbers) / len(numbers)

print("Average:", average)   # Output: 5.5



# =========================
# SQA ENGINEER RELATED EXAMPLES
# =========================

# Example 1: Find Highest Response Time (Performance Testing)
response_times = [120, 200, 150, 300, 250]
print("Max Response Time:", max(response_times))  # Slowest API

# Example 2: Find Fastest Response Time
print("Min Response Time:", min(response_times))  # Fastest API

# Example 3: Average Response Time
avg_response = sum(response_times) / len(response_times)
print("Average Response Time:", avg_response)

# Example 4: Sort Test Case Execution Time
execution_times = [5, 2, 8, 1, 3]
print("Sorted Execution Times:", sorted(execution_times))

# Example 5: Count Total Test Cases
test_cases = ["TC1", "TC2", "TC3", "TC4"]
print("Total Test Cases:", len(test_cases))

# Example 6: Count Passed Tests
results = ["pass", "fail", "pass", "pass", "fail"]
passed = results.count("pass")   # count() is also useful
print("Passed Test Cases:", passed)

# Example 7: Round Performance Metrics
load_time = 2.678945
print("Rounded Load Time:", round(load_time, 2))

# =========================
# MORE BUILT-IN FUNCTIONS
# =========================

# abs() -> returns absolute (positive) value
print("Absolute:", abs(-10))   # Output: 10

# pow() -> power calculation (x^y)
print("Power:", pow(2, 3))   # Output: 8

# divmod() -> returns quotient and remainder as tuple
print("Divmod:", divmod(10, 3))   # Output: (3, 1)

# type() -> shows data type
print("Type:", type(100))   # Output: <class 'int'>

# isinstance() -> checks type (True/False)
print("Is Integer:", isinstance(10, int))   # Output: True

# all() -> returns True if all elements are True
print("All True:", all([True, True, False]))   # Output: False

# any() -> returns True if at least one True
print("Any True:", any([False, False, True]))   # Output: True

# zip() -> combines multiple lists
names = ["TC1", "TC2", "TC3"]
status = ["pass", "fail", "pass"]
print("Zipped:", list(zip(names, status)))
# Output: [('TC1', 'pass'), ('TC2', 'fail'), ('TC3', 'pass')]

# enumerate() -> adds index to iterable
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)

# map() -> applies function to all elements
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x*x, nums))
print("Squared:", squared)

# filter() -> filters elements based on condition
even_numbers = list(filter(lambda x: x % 2 == 0, nums))
print("Even Numbers:", even_numbers)


# =========================
# STRING BUILT-IN METHODS
# =========================

text = "  qa automation  "

print(text.upper())      # QA AUTOMATION
print(text.lower())      # qa automation
print(text.strip())      # removes spaces
print(text.replace("qa", "SQA"))  # replace word
print(text.split())      # ['qa', 'automation']

# =========================
# SQA ENGINEER REAL-LIFE EXAMPLES
# =========================

# Example 1: Check if ALL test cases passed
results = ["pass", "pass", "pass"]
print("All Passed:", all(r == "pass" for r in results))


# Example 2: Check if ANY test failed
results = ["pass", "fail", "pass"]
print("Any Failed:", any(r == "fail" for r in results))


# Example 3: Combine test case IDs with results
test_ids = ["TC01", "TC02", "TC03"]
statuses = ["pass", "fail", "pass"]

report = list(zip(test_ids, statuses))
print("Test Report:", report)


# Example 4: Add index to test cases (useful in logs)
for i, tc in enumerate(test_ids, start=1):
    print(f"{i}. Executing {tc}")


# Example 5: Filter failed test cases
results = ["pass", "fail", "pass", "fail"]
failed = list(filter(lambda x: x == "fail", results))
print("Failed Tests:", failed)


# Example 6: Convert response times to milliseconds
times_sec = [1.2, 0.8, 1.5]
times_ms = list(map(lambda x: x * 1000, times_sec))
print("Response Times (ms):", times_ms)


# Example 7: Validate data type of API response
response = {"status": 200}

if isinstance(response["status"], int):
    print("Valid status code")


# Example 8: Clean input data (important for testing)
raw_input = "   login_test   "
clean_input = raw_input.strip()
print("Clean Input:", clean_input)


# Example 9: Check string contains keyword
error_message = "Invalid credentials"
print("Contains 'Invalid':", "Invalid" in error_message)


# Example 10: Sort bug priorities
priorities = ["low", "high", "medium"]
print("Sorted Priorities:", sorted(priorities))
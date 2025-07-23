# 1. Practice: Simple if Statements (30 examples)

# 1. Is dataset empty
data_rows = 0
if data_rows == 0:
    print("Dataset is empty")

# 2. Check if feature exists
feature = "price"
columns = ["id", "name", "price"]
if feature in columns:
    print("Feature found in dataset")

# 3. Outlier check
value = 1000
if value > 500:
    print("Potential outlier detected")

# 4. Server health
cpu_usage = 85
if cpu_usage > 80:
    print("High CPU usage warning")

# 5. Is string empty
input_text = ""
if input_text == "":
    print("No input provided")

# 6. API response check
status_code = 200
if status_code == 200:
    print("API call successful")

# 7. File extension check
filename = "report.csv"
if filename.endswith(".csv"):
    print("CSV file detected")

# 8. Dataframe shape check
rows = 1000
if rows > 500:
    print("Large dataset loaded")

# 9. Connection active
is_connected = True
if is_connected:
    print("Database connected")

# 10. Memory usage
ram = 90
if ram >= 90:
    print("Memory almost full")

# 11. Weekend check
day = "Sunday"
if day in ["Saturday", "Sunday"]:
    print("It's the weekend!")

# 12. Feature importance threshold
importance = 0.1
if importance < 0.05:
    print("Feature not important")

# 13. Model accuracy
accuracy = 0.95
if accuracy > 0.9:
    print("Model is highly accurate")

# 14. Check permission
role = "developer"
if role == "admin":
    print("Full permissions granted")

# 15. Browser detection
browser = "Chrome"
if browser == "Chrome":
    print("Optimized for Chrome")

# 16. Password length
password = "pass123"
if len(password) < 8:
    print("Password too short")

# 17. Email validation
email = "test@example.com"
if "@" in email:
    print("Email looks valid")

# 18. Environment type
env = "production"
if env == "production":
    print("Running in production")

# 19. Data type check
var = 5.5
if isinstance(var, float):
    print("Variable is float")

# 20. Loop counter
i = 10
if i % 2 == 0:
    print("Even index")

# 21. API token presence
token = None
if token is None:
    print("API token missing")

# 22. String match
username = "Admin"
if username.lower() == "admin":
    print("Admin user detected")

# 23. Data point value
temperature = -5
if temperature < 0:
    print("Freezing temperature")

# 24. Disk space
disk_free = 15
if disk_free < 20:
    print("Low disk space warning")

# 25. Time format
time_str = "14:30"
if ":" in time_str:
    print("Valid time format")

# 26. Character in text
msg = "Hello, world!"
if "!" in msg:
    print("Message is exclamatory")

# 27. Feature enabled
feature_flag = False
if not feature_flag:
    print("Feature disabled")

# 28. Deprecated API usage
api_version = "v1"
if api_version == "v1":
    print("Deprecated API version used")

# 29. Integer check
number = 100
if isinstance(number, int):
    print("Variable is integer")

# 30. Login attempt
attempts = 3
if attempts > 2:
    print("Too many login attempts")



#2. Practice: if-else Statements (30 examples)

# 1. Data source availability
source_online = False
if source_online:
    print("Data source online")
else:
    print("Data source offline")

# 2. Data upload status
upload_success = True
if upload_success:
    print("Upload completed")
else:
    print("Upload failed")

# 3. User active status
active = False
if active:
    print("User is active")
else:
    print("User inactive")

# 4. Password match
password = "1234"
confirm = "abcd"
if password == confirm:
    print("Passwords match")
else:
    print("Passwords do not match")

# 5. SSL enabled
ssl = True
if ssl:
    print("Secure connection")
else:
    print("Insecure connection")

# 6. Login limit
logins_today = 4
if logins_today < 5:
    print("Login allowed")
else:
    print("Login limit exceeded")

# 7. Data saved confirmation
saved = False
if saved:
    print("Data saved")
else:
    print("Failed to save data")

# 8. Is image grayscale
channels = 1
if channels == 1:
    print("Image is grayscale")
else:
    print("Image is colored")

# 9. Meeting duration
duration = 55
if duration <= 60:
    print("Meeting within time")
else:
    print("Meeting over time")

# 10. Temperature alert
temp = 38
if temp > 37:
    print("Fever detected")
else:
    print("Temperature normal")

# 11. Database backup
backup_done = True
if backup_done:
    print("Backup successful")
else:
    print("Backup failed")

# 12. Even or odd ID
record_id = 567
if record_id % 2 == 0:
    print("Even ID")
else:
    print("Odd ID")

# 13. Subscription status
subscription = "inactive"
if subscription == "active":
    print("Premium features unlocked")
else:
    print("Limited features")

# 14. Folder exists
folder = True
if folder:
    print("Folder found")
else:
    print("Folder missing")

# 15. Deployment status
deployed = False
if deployed:
    print("Deployment complete")
else:
    print("Deployment pending")

# 16. Update check
new_version = False
if new_version:
    print("Update available")
else:
    print("Software up to date")

# 17. User feedback
rating = 2
if rating >= 4:
    print("Positive feedback")
else:
    print("Needs improvement")

# 18. Sensor triggered
sensor = True
if sensor:
    print("Motion detected")
else:
    print("No movement")

# 19. Meeting slot availability
slots = 0
if slots > 0:
    print("Slots available")
else:
    print("Fully booked")

# 20. Test case result
test_pass = True
if test_pass:
    print("Test passed")
else:
    print("Test failed")

# 21. Data correction needed
data_valid = True
if data_valid:
    print("No correction needed")
else:
    print("Data correction required")

# 22. Download complete
download = True
if download:
    print("Download finished")
else:
    print("Download interrupted")

# 23. External API status
api_working = False
if api_working:
    print("External API working")
else:
    print("API down")

# 24. Encryption check
encrypted = True
if encrypted:
    print("Data is encrypted")
else:
    print("Data not encrypted")

# 25. Payment completion
payment_done = True
if payment_done:
    print("Payment successful")
else:
    print("Payment failed")

# 26. Password strength
password = "123"
if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")

# 27. Notification on
notify = False
if notify:
    print("Notifications enabled")
else:
    print("Notifications disabled")

# 28. Comment moderation
approved = True
if approved:
    print("Comment approved")
else:
    print("Comment rejected")

# 29. QR code scan
scanned = True
if scanned:
    print("QR code scanned")
else:
    print("QR code not scanned")

# 30. Daylight mode
sunlight = False
if sunlight:
    print("Day mode active")
else:
    print("Night mode active")



# 3. Practice: if-elif-else Ladders (30 examples)

# 1. Data volume check
records = 750
if records < 100:
    print("Small dataset")
elif records < 1000:
    print("Medium dataset")
else:
    print("Large dataset")

# 2. Connection speed
speed_mbps = 200
if speed_mbps < 50:
    print("Slow connection")
elif speed_mbps < 150:
    print("Moderate connection")
else:
    print("Fast connection")

# 3. User role privileges
role = "editor"
if role == "admin":
    print("Full access")
elif role == "editor":
    print("Edit access")
elif role == "viewer":
    print("Read-only access")
else:
    print("No access")

# 4. Customer loyalty
points = 1500
if points >= 5000:
    print("Diamond customer")
elif points >= 2000:
    print("Gold customer")
elif points >= 1000:
    print("Silver customer")
else:
    print("Bronze customer")

# 5. Battery health
battery_health = 80
if battery_health > 90:
    print("Excellent")
elif battery_health > 70:
    print("Good")
elif battery_health > 50:
    print("Average")
else:
    print("Poor")

# 6. Data quality score
quality_score = 85
if quality_score >= 95:
    print("Excellent data")
elif quality_score >= 80:
    print("Good data")
elif quality_score >= 60:
    print("Moderate data")
else:
    print("Poor data")

# 7. Employee experience
years = 12
if years < 2:
    print("Junior")
elif years < 5:
    print("Mid-level")
elif years < 10:
    print("Senior")
else:
    print("Expert")

# 8. Ticket severity
severity = "critical"
if severity == "low":
    print("Low priority")
elif severity == "medium":
    print("Medium priority")
elif severity == "high":
    print("High priority")
else:
    print("Critical priority")

# 9. Learning progress
percent_complete = 45
if percent_complete < 25:
    print("Getting started")
elif percent_complete < 50:
    print("In progress")
elif percent_complete < 75:
    print("Almost there")
else:
    print("Completed")

# 10. Product rating
rating = 3
if rating == 5:
    print("Excellent")
elif rating == 4:
    print("Very Good")
elif rating == 3:
    print("Good")
elif rating == 2:
    print("Fair")
else:
    print("Poor")

# 11. Weather forecast
temperature = 18
if temperature >= 35:
    print("Hot day")
elif temperature >= 25:
    print("Warm day")
elif temperature >= 15:
    print("Cool day")
else:
    print("Cold day")

# 12. Response time
response_ms = 900
if response_ms < 100:
    print("Instant response")
elif response_ms < 500:
    print("Fast response")
elif response_ms < 1000:
    print("Acceptable response")
else:
    print("Slow response")

# 13. Bug impact
users_affected = 5000
if users_affected < 100:
    print("Minor issue")
elif users_affected < 1000:
    print("Moderate issue")
elif users_affected < 10000:
    print("Major issue")
else:
    print("Critical issue")

# 14. Disk usage
disk_used = 85
if disk_used < 50:
    print("Low usage")
elif disk_used < 75:
    print("Moderate usage")
elif disk_used < 90:
    print("High usage")
else:
    print("Critical usage")

# 15. Order quantity
quantity = 120
if quantity < 50:
    print("Small order")
elif quantity < 100:
    print("Medium order")
elif quantity < 500:
    print("Large order")
else:
    print("Bulk order")

# 16. API request volume
requests = 800
if requests < 100:
    print("Low API usage")
elif requests < 500:
    print("Moderate API usage")
elif requests < 1000:
    print("High API usage")
else:
    print("Excessive API usage")

# 17. Data backup age
days_since_backup = 5
if days_since_backup <= 1:
    print("Recent backup")
elif days_since_backup <= 7:
    print("Weekly backup")
elif days_since_backup <= 30:
    print("Monthly backup")
else:
    print("Outdated backup")

# 18. Support response time
response_hours = 3
if response_hours <= 1:
    print("Immediate support")
elif response_hours <= 4:
    print("Fast support")
elif response_hours <= 12:
    print("Average support")
else:
    print("Slow support")

# 19. Training completion
progress = 75
if progress < 25:
    print("Just started")
elif progress < 50:
    print("Making progress")
elif progress < 75:
    print("Almost done")
else:
    print("Completed training")

# 20. Discount offer
cart_value = 600
if cart_value >= 2000:
    print("30% discount")
elif cart_value >= 1000:
    print("20% discount")
elif cart_value >= 500:
    print("10% discount")
else:
    print("No discount")

# 21. Project status
completion = 95
if completion == 100:
    print("Project complete")
elif completion >= 75:
    print("Almost complete")
elif completion >= 50:
    print("Halfway done")
else:
    print("In early stages")

# 22. Risk level
risk_score = 40
if risk_score >= 80:
    print("Critical risk")
elif risk_score >= 50:
    print("High risk")
elif risk_score >= 20:
    print("Moderate risk")
else:
    print("Low risk")

# 23. App rating
stars = 4.2
if stars >= 4.5:
    print("Excellent app")
elif stars >= 4.0:
    print("Very good app")
elif stars >= 3.0:
    print("Good app")
else:
    print("Needs improvement")

# 24. Energy consumption
consumption_kwh = 300
if consumption_kwh < 100:
    print("Low usage")
elif consumption_kwh < 300:
    print("Moderate usage")
elif consumption_kwh < 500:
    print("High usage")
else:
    print("Very high usage")

# 25. Test execution time
execution_sec = 120
if execution_sec <= 30:
    print("Fast test")
elif execution_sec <= 60:
    print("Acceptable speed")
elif execution_sec <= 180:
    print("Slow test")
else:
    print("Very slow test")

# 26. Database query time
query_ms = 250
if query_ms < 100:
    print("Optimal performance")
elif query_ms < 300:
    print("Acceptable performance")
elif query_ms < 1000:
    print("Slow performance")
else:
    print("Critical performance issue")

# 27. Attendance percentage
attendance = 65
if attendance >= 90:
    print("Excellent attendance")
elif attendance >= 75:
    print("Good attendance")
elif attendance >= 50:
    print("Low attendance")
else:
    print("Very poor attendance")

# 28. Credit score
score = 780
if score >= 800:
    print("Excellent credit")
elif score >= 700:
    print("Good credit")
elif score >= 600:
    print("Fair credit")
else:
    print("Poor credit")

# 29. Video resolution
resolution = "1080p"
if resolution == "4K":
    print("Ultra HD")
elif resolution == "1080p":
    print("Full HD")
elif resolution == "720p":
    print("HD")
else:
    print("SD")

# 30. Employee rating
rating = 4.8
if rating >= 4.5:
    print("Outstanding employee")
elif rating >= 4.0:
    print("Excellent employee")
elif rating >= 3.0:
    print("Good employee")
else:
    print("Needs improvement")


#4. Practice: Nested if-else Statements

# 1. Data cleaning: check missing and invalid values
missing_values = False
invalid_values = True
if missing_values:
    print("Missing values found")
else:
    if invalid_values:
        print("Invalid values detected")
    else:
        print("Data is clean")

# 2. User authentication
username = "john"
password = "secret"
if username == "john":
    if password == "secret":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Unknown user")

# 3. File download and size check
file_downloaded = True
file_size = 200
if file_downloaded:
    if file_size > 100:
        print("Large file downloaded")
    else:
        print("Small file downloaded")
else:
    print("Download failed")

# 4. Temperature check with humidity
temperature = 35
humidity = 85
if temperature > 30:
    if humidity > 80:
        print("Hot and humid day")
    else:
        print("Hot but dry day")
else:
    print("Cool day")

# 5. Model evaluation
model_trained = True
accuracy = 0.88
if model_trained:
    if accuracy >= 0.9:
        print("Excellent model")
    else:
        print("Model needs improvement")
else:
    print("Model not trained")

# 6. Server status with load
server_up = True
load = 75
if server_up:
    if load > 80:
        print("Server overloaded")
    else:
        print("Server healthy")
else:
    print("Server down")

# 7. Payment gateway check
gateway_online = False
transaction_successful = False
if gateway_online:
    if transaction_successful:
        print("Payment processed")
    else:
        print("Payment failed")
else:
    print("Gateway unavailable")

# 8. Access rights
is_employee = True
department = "Finance"
if is_employee:
    if department == "Finance":
        print("Access to financial reports granted")
    else:
        print("Limited access")
else:
    print("No access")

# 9. Subscription validity
subscription_active = True
days_remaining = 3
if subscription_active:
    if days_remaining <= 5:
        print("Subscription expiring soon")
    else:
        print("Subscription valid")
else:
    print("Subscription expired")

# 10. Resource usage
cpu = 45
ram = 75
if cpu > 50:
    if ram > 70:
        print("High CPU and RAM usage")
    else:
        print("High CPU usage only")
else:
    if ram > 70:
        print("High RAM usage only")
    else:
        print("System resources normal")

# 11. API key validation
api_key = "abc123"
api_active = False
if api_key:
    if api_active:
        print("API key valid")
    else:
        print("API key inactive")
else:
    print("API key missing")

# 12. Product availability
product_in_stock = True
quantity = 0
if product_in_stock:
    if quantity > 0:
        print("Product available")
    else:
        print("Out of stock")
else:
    print("Product not listed")

# 13. Feature flag and beta user
feature_enabled = True
is_beta_user = True
if feature_enabled:
    if is_beta_user:
        print("Beta feature enabled")
    else:
        print("Feature available for production")
else:
    print("Feature disabled")

# 14. Meeting schedule
day = "Monday"
time = 15
if day in ["Monday", "Tuesday"]:
    if time < 12:
        print("Morning meeting")
    else:
        print("Afternoon meeting")
else:
    print("No meeting scheduled")

# 15. Student eligibility for exam
attendance = 85
assignment_submitted = False
if attendance >= 75:
    if assignment_submitted:
        print("Eligible for exam")
    else:
        print("Assignment pending")
else:
    print("Not eligible due to low attendance")

# 16. Delivery status
order_placed = True
shipped = False
if order_placed:
    if shipped:
        print("Order shipped")
    else:
        print("Processing order")
else:
    print("No order found")

# 17. Device online and firmware update
device_online = True
firmware_version = 2.0
if device_online:
    if firmware_version < 2.5:
        print("Firmware update required")
    else:
        print("Device up-to-date")
else:
    print("Device offline")

# 18. Financial transaction
account_balance = 1000
withdraw_amount = 1500
if account_balance >= withdraw_amount:
    print("Withdrawal allowed")
else:
    if account_balance > 0:
        print("Partial withdrawal possible")
    else:
        print("Insufficient funds")

# 19. Customer feedback
feedback_given = True
satisfaction_score = 8
if feedback_given:
    if satisfaction_score >= 7:
        print("Customer satisfied")
    else:
        print("Customer dissatisfied")
else:
    print("No feedback received")

# 20. Enrollment check
course_active = True
seats_available = 0
if course_active:
    if seats_available > 0:
        print("Enrollment open")
    else:
        print("Course full")
else:
    print("Course inactive")

# 21. Email delivery
email_sent = True
bounced = False
if email_sent:
    if bounced:
        print("Email delivery failed")
    else:
        print("Email delivered successfully")
else:
    print("Email not sent")

# 22. Time-based greeting
hour = 20
if hour < 12:
    print("Good morning")
else:
    if hour < 18:
        print("Good afternoon")
    else:
        print("Good evening")

# 23. Git commit status
changes_staged = True
commit_done = False
if changes_staged:
    if commit_done:
        print("Changes committed")
    else:
        print("Commit pending")
else:
    print("No changes staged")

# 24. User registration
email_verified = True
profile_completed = False
if email_verified:
    if profile_completed:
        print("Registration complete")
    else:
        print("Complete your profile")
else:
    print("Verify your email")

# 25. Cloud service status
service_online = False
maintenance_scheduled = True
if service_online:
    print("Service available")
else:
    if maintenance_scheduled:
        print("Service under maintenance")
    else:
        print("Unexpected downtime")

# 26. Weekly sales performance
sales_target = 5000
actual_sales = 4500
if actual_sales >= sales_target:
    print("Target achieved")
else:
    if actual_sales >= 0.8 * sales_target:
        print("Near target")
    else:
        print("Below target")

# 27. API rate limiting
api_calls = 950
api_limit = 1000
if api_calls < api_limit:
    print("API usage within limits")
else:
    print("API limit reached")

# 28. Document upload
doc_uploaded = True
file_size = 55
if doc_uploaded:
    if file_size <= 50:
        print("Document accepted")
    else:
        print("File too large")
else:
    print("Document upload failed")

# 29. Cloud storage plan
plan = "basic"
storage_used = 90
if plan == "basic":
    if storage_used > 80:
        print("Upgrade recommended")
    else:
        print("Storage within limits")
else:
    print("Premium plan active")

# 30. Data pipeline run
pipeline_ready = True
error_count = 0
if pipeline_ready:
    if error_count == 0:
        print("Pipeline executed successfully")
    else:
        print("Pipeline completed with errors")
else:
    print("Pipeline not ready")


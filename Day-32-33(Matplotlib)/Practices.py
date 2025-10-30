"""
Python File: matplotlib_practice_full.py
Purpose: Complete practice file for Matplotlib covering 50 real-world, situation-based examples.
Author: Shalini Verma
Includes: Line, Scatter, Bar, Histogram, Pie, Area, Box, 3D, Polar, Customizations, Subplots, Error Bars
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(0)

# ============================================================
# 1. LINE PLOT - Monthly Sales Trend
# ============================================================
months = ['Jan','Feb','Mar','Apr','May','Jun']
sales_productA = [120, 150, 170, 130, 160, 180]
sales_productB = [100, 130, 150, 120, 140, 170]

plt.plot(months, sales_productA, label="Product A", marker='o')
plt.plot(months, sales_productB, label="Product B", marker='s')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales Units")
plt.legend()
plt.show()

# ============================================================
# 2. SCATTER PLOT - Employee Performance
# ============================================================
experience = np.random.randint(1,11,20)
performance = experience*5 + np.random.randint(-5,6,20)
plt.scatter(experience, performance, color='green')
plt.title("Employee Performance vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Performance Score")
plt.grid(True)
plt.show()

# ============================================================
# 3. BAR PLOT - Product Sales Comparison
# ============================================================
products = ['Laptop','Tablet','Mobile','Monitor','Printer']
sales_q1 = [50, 70, 90, 30, 40]
sales_q2 = [60, 80, 85, 35, 45]

x = np.arange(len(products))
plt.bar(x - 0.2, sales_q1, width=0.4, label='Q1', color='blue')
plt.bar(x + 0.2, sales_q2, width=0.4, label='Q2', color='orange')
plt.xticks(x, products)
plt.title("Product Sales Q1 vs Q2")
plt.ylabel("Units Sold")
plt.legend()
plt.show()

# ============================================================
# 4. HISTOGRAM - Website Traffic Distribution
# ============================================================
daily_visitors = np.random.randint(100,1000,200)
plt.hist(daily_visitors, bins=20, color='purple', edgecolor='black')
plt.title("Website Daily Visitors Distribution")
plt.xlabel("Visitors")
plt.ylabel("Frequency")
plt.show()

# ============================================================
# 5. PIE CHART - Market Share
# ============================================================
companies = ['Company A','Company B','Company C','Company D']
market_share = [35,25,20,20]
colors = ['gold','lightblue','lightgreen','pink']
plt.pie(market_share, labels=companies, autopct='%1.1f%%', colors=colors, shadow=True)
plt.title("Market Share of Companies")
plt.show()

# ============================================================
# 6. STACKED AREA - Energy Consumption
# ============================================================
months_num = np.arange(1,7)
residential = np.array([120,130,125,140,135,150])
industrial = np.array([80,90,85,95,100,110])
commercial = np.array([60,65,70,75,80,85])

plt.stackplot(months_num, residential, industrial, commercial, labels=['Residential','Industrial','Commercial'], colors=['blue','red','green'])
plt.legend()
plt.title("Monthly Energy Consumption")
plt.xlabel("Month")
plt.ylabel("Energy Units")
plt.show()

# ============================================================
# 7. BOX PLOT - Student Test Scores
# ============================================================
scores = np.random.randint(40,100,50)
plt.boxplot(scores, vert=True, patch_artist=True)
plt.title("Distribution of Student Test Scores")
plt.ylabel("Scores")
plt.show()

# ============================================================
# 8. ERROR BAR - Experiment Data
# ============================================================
time = np.arange(0,10,1)
measurement = np.array([2,3,4,5,6,5,6,7,8,9])
error = np.random.rand(10)*0.5
plt.errorbar(time, measurement, yerr=error, fmt='o', ecolor='red', capsize=4)
plt.title("Experimental Measurement with Error")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.show()

# ============================================================
# 9. POLAR PLOT - Wind Direction
# ============================================================
angles = np.linspace(0, 2*np.pi, 100)
wind_speed = np.abs(np.sin(angles)*10)
plt.polar(angles, wind_speed, color='blue')
plt.title("Wind Speed by Direction")
plt.show()

# ============================================================
# 10. 3D SCATTER - Sales Performance
# ============================================================
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
region = np.random.randint(1,5,30)
sales = np.random.randint(100,500,30)
profit = np.random.randint(10,100,30)

ax.scatter(region, sales, profit, c=profit, cmap='viridis', s=50)
ax.set_xlabel("Region")
ax.set_ylabel("Sales")
ax.set_zlabel("Profit")
ax.set_title("3D Scatter: Region vs Sales vs Profit")
plt.show()

# ============================================================
# 11. LINE PLOT WITH MOVING AVERAGE - Stock Prices
# ============================================================
days = np.arange(1,31)
stock_price = np.random.randint(100,200,30)
moving_avg = np.convolve(stock_price, np.ones(5)/5, mode='valid')

plt.plot(days, stock_price, label="Stock Price", marker='o')
plt.plot(days[4:], moving_avg, label="5-day Moving Avg", linestyle='--', color='red')
plt.title("Stock Price with Moving Average")
plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()
plt.show()

# ============================================================
# 12. SCATTER WITH SIZE & COLOR - Customer Segmentation
# ============================================================
age = np.random.randint(18,60,50)
income = np.random.randint(20000,100000,50)
spending_score = np.random.randint(1,100,50)

plt.scatter(age, income, s=spending_score*2, c=spending_score, cmap='cool', alpha=0.6)
plt.colorbar(label="Spending Score")
plt.title("Customer Segmentation Scatter Plot")
plt.xlabel("Age")
plt.ylabel("Income")
plt.show()

# ============================================================
# 13. HORIZONTAL BAR - Top Products
# ============================================================
top_products = ['Laptop','Tablet','Mobile','Monitor','Printer']
units_sold = [120, 90, 150, 80, 60]

plt.barh(top_products, units_sold, color='orange')
plt.title("Top Selling Products")
plt.xlabel("Units Sold")
plt.show()

# ============================================================
# 14. STACKED BAR - Category-wise Sales
# ============================================================
categories = ['Electronics','Furniture','Clothing','Food']
sales_online = [200, 150, 300, 100]
sales_offline = [180, 170, 250, 120]

plt.bar(categories, sales_online, label='Online')
plt.bar(categories, sales_offline, bottom=sales_online, label='Offline')
plt.title("Stacked Sales by Category")
plt.ylabel("Units Sold")
plt.legend()
plt.show()

# ============================================================
# 15. HISTOGRAM WITH DENSITY - Customer Age Distribution
# ============================================================
ages = np.random.randint(18,70,200)
plt.hist(ages, bins=15, density=True, color='green', edgecolor='black', alpha=0.7)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Density")
plt.show()

# ============================================================
# 16. PIE CHART WITH EXPLODED SLICES - Market Share
# ============================================================
labels = ['Brand A','Brand B','Brand C','Brand D']
sizes = [30,40,20,10]
explode = (0,0.1,0,0)
colors = ['yellow','blue','green','red']

plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, colors=colors)
plt.title("Market Share with Exploded Slice")
plt.show()

# ============================================================
# 17. BOX PLOT WITH OUTLIERS - Salary Distribution
# ============================================================
salaries = np.random.randint(30000,120000,50)
plt.boxplot(salaries, patch_artist=True, flierprops=dict(marker='o', color='red', markersize=8))
plt.title("Salary Distribution with Outliers")
plt.ylabel("Salary")
plt.show()

# ============================================================
# 18. AREA PLOT - Website Traffic Trends
# ============================================================
days = np.arange(1,11)
organic = np.random.randint(100,200,10)
paid = np.random.randint(50,150,10)

plt.stackplot(days, organic, paid, labels=['Organic','Paid'], colors=['blue','orange'])
plt.title("Website Traffic Trends")
plt.xlabel("Day")
plt.ylabel("Visitors")
plt.legend()
plt.show()

# ============================================================
# 19. SUBPLOTS FOR MULTIPLE KPIs
# ============================================================
x = np.arange(1,11)
y1 = np.random.randint(50,100,10)
y2 = np.random.randint(30,80,10)

plt.subplot(2,1,1)
plt.plot(x, y1, marker='o', color='blue')
plt.title("KPI 1")

plt.subplot(2,1,2)
plt.plot(x, y2, marker='s', color='green')
plt.title("KPI 2")

plt.tight_layout()
plt.show()

# ============================================================
# 20. LINE + SCATTER COMBINATION - Temperature Trend
# ============================================================
days = np.arange(1,11)
temperature = np.random.randint(20,35,10)
plt.plot(days, temperature, color='red', label='Temperature')
plt.scatter(days, temperature, color='blue')
plt.title("Temperature Trend")
plt.xlabel("Days")
plt.ylabel("°C")
plt.legend()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(1)

# ============================================================
# 21. BAR CHART WITH VALUE ANNOTATIONS - Product Sales
# ============================================================
products = ['Laptop','Tablet','Mobile','Monitor','Printer']
sales = [120,90,150,80,60]
plt.bar(products, sales, color='skyblue')
for i, v in enumerate(sales):
    plt.text(i, v + 2, str(v), ha='center')
plt.title("Product Sales with Value Annotations")
plt.ylabel("Units Sold")
plt.show()

# ============================================================
# 22. POLAR BAR CHART - Cyclical Sales Data
# ============================================================
angles = np.linspace(0, 2*np.pi, 6, endpoint=False)
sales = [100,150,130,160,180,140]
plt.subplot(projection='polar')
plt.bar(angles, sales, width=0.4, color='coral', alpha=0.7)
plt.title("Monthly Sales in Polar Bar Chart")
plt.show()

# ============================================================
# 23. 3D SURFACE PLOT - Temperature Map
# ============================================================
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.arange(-5,5,0.5)
Y = np.arange(-5,5,0.5)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title("3D Surface Plot - Temperature Map")
plt.show()

# ============================================================
# 24. HEATMAP USING IMSHOW - Correlation Matrix
# ============================================================
data = np.random.rand(5,5)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title("Heatmap of Random Data")
plt.show()

# ============================================================
# 25. CUSTOMIZED PLOT WITH STYLE AND GRID - Revenue Trend
# ============================================================
months = np.arange(1,13)
revenue = np.random.randint(2000,5000,12)
plt.style.use('ggplot')
plt.plot(months, revenue, marker='o', linestyle='--', color='purple')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.show()

# ============================================================
# 26. FILLED PLOT - Confidence Interval Example
# ============================================================
x = np.linspace(0,10,100)
y = np.sin(x)
error = 0.2
plt.plot(x, y, color='blue', label='sin(x)')
plt.fill_between(x, y-error, y+error, color='blue', alpha=0.2)
plt.title("Filled Plot - Confidence Interval")
plt.legend()
plt.show()

# ============================================================
# 27. LOG SCALE PLOT - Revenue Growth
# ============================================================
months = np.arange(1,13)
revenue = np.random.randint(100,10000,12)
plt.plot(months, revenue, marker='o')
plt.yscale('log')
plt.title("Revenue Growth (Log Scale)")
plt.xlabel("Month")
plt.ylabel("Revenue (log scale)")
plt.show()

# ============================================================
# 28. DUAL AXIS PLOT - Sales vs Profit
# ============================================================
months = np.arange(1,13)
sales = np.random.randint(100,500,12)
profit = np.random.randint(10,100,12)
fig, ax1 = plt.subplots()
ax1.plot(months, sales, 'b-o', label='Sales')
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales", color='b')
ax2 = ax1.twinx()
ax2.plot(months, profit, 'r-s', label='Profit')
ax2.set_ylabel("Profit", color='r')
plt.title("Sales vs Profit Dual Axis")
fig.tight_layout()
plt.show()

# ============================================================
# 29. ERROR BARS WITH DIFFERENT COLORS
# ============================================================
x = np.arange(0,10)
y = np.random.randint(1,10,10)
y_err = np.random.rand(10)
plt.errorbar(x, y, yerr=y_err, fmt='o', ecolor='red', mec='blue', mfc='yellow', capsize=5)
plt.title("Error Bars with Custom Colors")
plt.show()

# ============================================================
# 30. SCATTER WITH REGRESSION LINE
# ============================================================
x = np.random.randint(1,20,20)
y = 2*x + np.random.randint(-5,5,20)
plt.scatter(x,y)
m, b = np.polyfit(x,y,1)
plt.plot(x, m*x+b, color='red', label=f'Y={m:.2f}X+{b:.2f}')
plt.title("Scatter with Regression Line")
plt.legend()
plt.show()

# ============================================================
# 31. HISTOGRAM OVERLAY FOR COMPARISON
# ============================================================
groupA = np.random.randint(50,100,50)
groupB = np.random.randint(30,80,50)
plt.hist(groupA, bins=10, alpha=0.5, label='Group A')
plt.hist(groupB, bins=10, alpha=0.5, label='Group B')
plt.title("Histogram Overlay Comparison")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# ============================================================
# 32. BOX PLOT COMPARISON BETWEEN GROUPS
# ============================================================
group1 = np.random.randint(40,90,50)
group2 = np.random.randint(50,95,50)
plt.boxplot([group1, group2], labels=['Group1','Group2'], patch_artist=True)
plt.title("Box Plot Comparison Between Groups")
plt.show()

# ============================================================
# 33. AREA PLOT WITH MULTIPLE REGIONS STACKED
# ============================================================
days = np.arange(1,11)
region1 = np.random.randint(20,50,10)
region2 = np.random.randint(10,40,10)
region3 = np.random.randint(5,30,10)
plt.stackplot(days, region1, region2, region3, labels=['Region1','Region2','Region3'], colors=['blue','orange','green'])
plt.title("Stacked Area Plot for Multiple Regions")
plt.xlabel("Days")
plt.ylabel("Units")
plt.legend()
plt.show()

# ============================================================
# 34. BAR CHART WITH HATCHING - Survey Results
# ============================================================
categories = ['Option A','Option B','Option C']
values = [30,45,25]
plt.bar(categories, values, color='lightblue', hatch='//')
plt.title("Survey Results with Hatching")
plt.show()

# ============================================================
# 35. LINE PLOT WITH MARKERS & DASHED LINES
# ============================================================
x = np.arange(1,11)
y = np.random.randint(10,50,10)
plt.plot(x, y, linestyle='--', marker='o', color='purple')
plt.title("Line Plot with Markers & Dashed Lines")
plt.show()

# ============================================================
# 36. PIE CHART WITH SHADOW AND START ANGLE
# ============================================================
sizes = [40,30,20,10]
labels = ['A','B','C','D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Pie Chart with Shadow & Start Angle")
plt.show()

# ============================================================
# 37. STACKED HORIZONTAL BARS
# ============================================================
departments = ['HR','Sales','IT','Finance']
male = [20,30,40,25]
female = [25,35,30,20]
plt.barh(departments, male, color='blue', label='Male')
plt.barh(departments, female, left=male, color='pink', label='Female')
plt.title("Gender Distribution in Departments")
plt.legend()
plt.show()

# ============================================================
# 38. 3D LINE PLOT - Trajectory Simulation
# ============================================================
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
t = np.linspace(0,10,100)
x = np.sin(t)
y = np.cos(t)
z = t
ax.plot(x,y,z, label='Trajectory', color='red')
ax.set_title("3D Line Plot - Trajectory")
plt.show()

# ============================================================
# 39. LINE PLOT WITH ANNOTATIONS - Highlight Peaks
# ============================================================
x = np.arange(1,11)
y = np.random.randint(10,50,10)
plt.plot(x,y, marker='o')
peak_index = np.argmax(y)
plt.annotate(f'Peak: {y[peak_index]}', xy=(x[peak_index], y[peak_index]), xytext=(x[peak_index]+0.5, y[peak_index]+5), arrowprops=dict(facecolor='red', arrowstyle='->'))
plt.title("Line Plot with Peak Annotation")
plt.show()

# ============================================================
# 40. HISTOGRAM WITH CUMULATIVE DISTRIBUTION
# ============================================================
data = np.random.randint(0,100,50)
plt.hist(data, bins=10, cumulative=True, color='orange', edgecolor='black')
plt.title("Cumulative Histogram")
plt.show()

# ============================================================
# 41. SCATTER WITH TRANSPARENCY
# ============================================================
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x,y, alpha=0.5)
plt.title("Scatter Plot with Transparency")
plt.show()

# ============================================================
# 42. BAR PLOT WITH LOG SCALE
# ============================================================
categories = ['A','B','C','D']
values = [10,100,1000,10000]
plt.bar(categories, values)
plt.yscale('log')
plt.title("Bar Plot with Log Scale")
plt.show()

# ============================================================
# 43. COMBINED PLOTS IN SUBPLOTS
# ============================================================
x = np.arange(1,6)
y1 = np.random.randint(10,50,5)
y2 = np.random.randint(20,60,5)

plt.subplot(1,2,1)
plt.plot(x,y1,'r-o')
plt.title("Line Plot")

plt.subplot(1,2,2)
plt.bar(x,y2, color='green')
plt.title("Bar Plot")
plt.tight_layout()
plt.show()

# ============================================================
# 44. POLAR LINE PLOT - Periodic Pattern
# ============================================================
theta = np.linspace(0,2*np.pi,100)
r = np.abs(np.sin(2*theta))
plt.subplot(projection='polar')
plt.plot(theta,r)
plt.title("Polar Line Plot - Periodic Pattern")
plt.show()

# ============================================================
# 45. CUSTOM COLORMAP USAGE
# ============================================================
data = np.random.rand(10,10)
plt.imshow(data, cmap='plasma')
plt.colorbar()
plt.title("Custom Colormap Example")
plt.show()

# ============================================================
# 46. FILLED AREA UNDER CURVE
# ============================================================
x = np.linspace(0,10,100)
y = np.sin(x)
plt.fill_between(x,y, color='skyblue', alpha=0.4)
plt.plot(x,y, color='blue')
plt.title("Filled Area Under Curve")
plt.show()

# ============================================================
# 47. STEP PLOT FOR CUMULATIVE METRICS
# ============================================================
x = np.arange(1,11)
y = np.cumsum(np.random.randint(1,10,10))
plt.step(x,y, where='mid', color='purple')
plt.title("Step Plot for Cumulative Metrics")
plt.show()

# ============================================================
# 48. ERROR BAR WITH ASYMMETRIC ERRORS
# ============================================================
x = np.arange(1,6)
y = np.random.randint(10,20,5)
yerr = [1,2,1,2,1]
yerr_upper = [1.5,1,2,1.5,1]
plt.errorbar(x,y, yerr=[yerr, yerr_upper], fmt='o', color='red', capsize=5)
plt.title("Error Bars with Asymmetric Errors")
plt.show()

# ============================================================
# 49. MULTI-LINE TREND COMPARISON
# ============================================================
x = np.arange(1,11)
y1 = np.random.randint(10,50,10)
y2 = np.random.randint(20,60,10)
y3 = np.random.randint(5,40,10)
plt.plot(x,y1,label='Line 1')
plt.plot(x,y2,label='Line 2')
plt.plot(x,y3,label='Line 3')
plt.title("Multi-Line Trend Comparison")
plt.legend()
plt.show()

# ============================================================
# 50. MULTI-FIGURE PLOTS FOR REPORTS
# ============================================================
for i in range(1,4):
    plt.figure()
    plt.plot(np.arange(1,11), np.random.randint(10,50,10), marker='o')
    plt.title(f"Report Figure {i}")
plt.show()

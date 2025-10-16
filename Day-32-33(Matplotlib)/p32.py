"""
Matplotlib Library – Basic to Intermediate Visualization

Install Matplotlib and NumPy-->
- pip install matplotlib numpy

You can also upgrade them if needed:
- pip install --upgrade matplotlib numpy

matplotlib.pyplot → For creating plots (line, bar, scatter, etc.)
numpy → For generating data arrays and mathematical operations
"""

#Step 1: Import Libraries
# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

#Step 2: Create Data
# Create a sequence of numbers from 0 to 10
x = np.linspace(0, 10, 100)  # 100 evenly spaced points
y = np.sin(x)  # sine of each x

#Step 3: Create a Simple Plot
plt.plot(x, y)        # Line plot
plt.title("Sine Wave")  # Add title
plt.xlabel("X-axis")   # X-axis label
plt.ylabel("Y-axis")   # Y-axis label
plt.grid(True)         # Show grid
plt.show()             # Display plot


# ============================================================
""" 
Matplotlib is a Python library used for data visualization(2D plotting), 
which means it helps us convert data into visual plots like graphs, charts, and histograms.

Examples -->
1. School Grades: Show a bar chart comparing marks in different subjects.
2. Weather Data: Plot temperature trends over a week.
3. Sports: Compare goals scored by players using a line chart.
4. Business: Show monthly sales trends with a line or bar chart.

Importance:
1. Visualize data for better understanding & Helps understand data patterns quickly
2. Identify patterns, trends, and outliers
3. Communicate results effectively and very Useful for data analysis, statistics, and machine learning
4. Works well with NumPy, Pandas, and other libraries
5. Makes reports and presentations more visual and meaningful

Different Plot Types --> 
| Plot Type    | Use Case Example       |
| ------------ | ---------------------- |
| Line Plot    | Monthly sales trend    |
| Bar Chart    | Compare student marks  |
| Histogram    | Distribution of ages   |
| Pie Chart    | Market share           |
| Scatter Plot | Height vs Weight       |
| Area Plot    | Website traffic trends |
| Box Plot     | Salary distribution    |

"""
# ============================================================

# -------------------------
# 1. LINE PLOT
# -------------------------
"""
Line Plot: Shows the relationship between two variables.
Used for: Trend over time or sequence data.
"""

# Example 1: Basic Line Plot
# Import required libraries
import matplotlib.pyplot as plt
import numpy as np
# --------------------------
x = [1,2,3,4,5]  # X-axis values (independent variable)
y = [10,20,25,30,40]  # Y-axis values (dependent variable)

# Plot the line
plt.plot(x, y, label="Line 1", color="blue", marker='o')  
# label="Line 1" -> name of the line in legend
# color="blue" -> line color
# marker='o' -> show circle markers at each point

plt.title("Basic Line Plot Example 1")  # Add a title to the plot
plt.xlabel("X-axis")  # Label for X-axis
plt.ylabel("Y-axis")  # Label for Y-axis
plt.legend()  # Display legend
plt.show()  # Display the plot

# ------------------------------------------------------------
# Example 2: Multiple Lines
# --------------------------
y2 = [5,15,20,25,35]  # Second set of Y-axis values

# Plot first line
plt.plot(x, y, label="Line 1")
# Plot second line with dashed style and red color
plt.plot(x, y2, label="Line 2", linestyle='--', color='red')

plt.title("Multiple Line Plot")  # Add title
plt.legend()  # Show legend
plt.show()

# ------------------------------------------------------------
# Example 3: Using NumPy arrays for smoother line
# --------------------------
x = np.linspace(0, 10, 100)  # 100 evenly spaced points between 0 and 10
y = np.sin(x)  # Compute sine values for each x

plt.plot(x, y, label="Sine Wave")  # Plot sine wave
plt.title("Sine Wave using NumPy")
plt.xlabel("X values")
plt.ylabel("Sin(X)")
plt.legend()
plt.show()

# ------------------------------------------------------------
# Example 4: Line Width and Style
# --------------------------
plt.plot(x, y, color='green', linestyle='-.', linewidth=2)
# linestyle='-.' -> dash-dot line style
# linewidth=2 -> thickness of the line
plt.title("Line with Style and Width")
plt.show()

# ------------------------------------------------------------
# Example 5: Line Plot with Markers
# --------------------------
plt.plot(x, y, marker='x', markersize=5, label="Sine Wave")
# marker='x' -> show X markers at each point
# markersize=5 -> size of the marker
plt.title("Line Plot with Markers")
plt.legend()
plt.show()

# ------------------------------------------------------------
# Example 6: Adding Horizontal Reference Line
# --------------------------
plt.axhline(y=0.5, color='red', linestyle='--')  
# Draws a horizontal line at y=0.5
plt.plot(x, y)  # Plot sine wave on top
plt.title("Horizontal Reference Line")
plt.show()

# ------------------------------------------------------------
# Example 7: Adding Vertical Reference Line
# --------------------------
plt.axvline(x=5, color='purple', linestyle=':')  
# Draws a vertical line at x=5
plt.plot(x, y)  # Plot sine wave on top
plt.title("Vertical Reference Line")
plt.show()

# ------------------------------------------------------------
# Example 8: Line Plot with Grid
# --------------------------
plt.plot(x, y)
plt.grid(True)  # Display grid lines
plt.title("Line Plot with Grid")
plt.show()

# ------------------------------------------------------------
# Example 9: Line Plot with Logarithmic Y-axis
# --------------------------
y = np.exp(x/3)  # Exponential growth data
plt.plot(x, y)
plt.yscale('log')  # Set Y-axis to logarithmic scale
plt.title("Line Plot with Log Scale")
plt.show()

# ------------------------------------------------------------
# Example 10: Filled Area Under Line
# --------------------------
plt.plot(x, y)  
plt.fill_between(x, y, color="lightblue", alpha=0.5)  
# fill_between() -> fills the area under the line
# color -> fill color
# alpha -> transparency level (0.0 transparent, 1.0 opaque)
plt.title("Line Plot with Filled Area")
plt.show()

# -------------------------
# 2. SCATTER PLOT
# -------------------------
"""
Scatter Plot: Shows relationship between two variables using points.
Used for: Observing correlation, clusters, and outliers.
"""

# Example 1: Basic Scatter Plot
# -----------------------------
x = np.random.rand(50)  # Generate 50 random values for X-axis (0 to 1)
y = np.random.rand(50)  # Generate 50 random values for Y-axis

# Plot scatter points
plt.scatter(x, y, color='red', label="Points")
# color='red' -> color of points
# label="Points" -> legend name

plt.title("Basic Scatter Plot")  # Add plot title
plt.xlabel("X-axis")            # Label X-axis
plt.ylabel("Y-axis")            # Label Y-axis
plt.legend()                    # Show legend
plt.show()                      # Display the plot

# ------------------------------------------------------------
# Example 2: Scatter Plot with Varying Sizes
# -----------------------------
sizes = np.random.randint(10, 200, size=50)  # Random sizes for each point
plt.scatter(x, y, s=sizes)
# s -> size of each point
plt.title("Scatter Plot with Varying Sizes")
plt.show()

# ------------------------------------------------------------
# Example 3: Scatter Plot with Colors
# -----------------------------
colors = np.random.rand(50)  # Random values to assign color
plt.scatter(x, y, c=colors, cmap='viridis')
# c -> assigns color to each point based on array values
# cmap='viridis' -> color map for gradient effect
plt.colorbar()  # Display color scale
plt.title("Scatter Plot with Colors")
plt.show()

# ------------------------------------------------------------
# Example 4: Multiple Scatter Groups
# -----------------------------
y2 = np.random.rand(50)  # Second group of Y-axis values
plt.scatter(x, y, color='blue', label="Group 1")     # First group
plt.scatter(x, y2, color='orange', label="Group 2")  # Second group
plt.title("Multiple Scatter Groups")
plt.legend()  # Show legend
plt.show()

# ------------------------------------------------------------
# Example 5: Scatter Plot with Transparency
# -----------------------------
plt.scatter(x, y, alpha=0.5)
# alpha=0.5 -> transparency (0=transparent, 1=opaque)
plt.title("Scatter Plot with Transparency")
plt.show()

# ------------------------------------------------------------
# Example 6: Different Marker Styles
# -----------------------------
plt.scatter(x, y, marker='*', color='green', s=100)
# marker='*' -> star-shaped marker
# s=100 -> size of marker
plt.title("Scatter Plot with Star Marker")
plt.show()

# ------------------------------------------------------------
# Example 7: Scatter Plot with Line
# -----------------------------
plt.scatter(x, y)  # Plot scatter points
plt.plot(np.sort(x), np.sort(y), color='red')  
# Overlay line connecting sorted points
plt.title("Scatter Plot with Line")
plt.show()

# ------------------------------------------------------------
# Example 8: Highlight Specific Points
# -----------------------------
plt.scatter(x, y, color='blue')  # Normal points
plt.scatter(x[0], y[0], color='red', s=200, label="Highlighted Point")  
# Highlight first point in red
plt.legend()
plt.title("Scatter Plot with Highlighted Point")
plt.show()

# ------------------------------------------------------------
# Example 9: Scatter Plot with Grid
# -----------------------------
plt.scatter(x, y)
plt.grid(True)  # Show grid lines
plt.title("Scatter Plot with Grid")
plt.show()

# ------------------------------------------------------------
# Example 10: Scatter Plot with Custom Colormap
# -----------------------------
plt.scatter(x, y, c=colors, cmap='plasma', s=100)
# cmap='plasma' -> different color map for visual appeal
plt.colorbar()  # Display color scale
plt.title("Scatter Plot with Custom Colormap")
plt.show()


# -------------------------
# 3. BAR PLOT
# -------------------------
"""
Bar Plot: Represents categorical data with rectangular bars.
Used for: Comparing categories.
"""

# Example 1: Basic Vertical Bar Plot
# ----------------------------------
categories = ['A', 'B', 'C', 'D']  # Categories for X-axis
values = [10, 20, 15, 25]         # Corresponding values for Y-axis

# Plot vertical bars
plt.bar(categories, values, color='skyblue')  
# color -> fill color of bars

plt.title("Basic Vertical Bar Plot")  # Add title
plt.show()                            # Display plot

# ------------------------------------------------------------
# Example 2: Horizontal Bar Plot
# -------------------------------
plt.barh(categories, values, color='lightgreen')  
# barh -> horizontal bars
plt.title("Horizontal Bar Plot")
plt.show()

# ------------------------------------------------------------
# Example 3: Grouped Bar Plot (Multiple bars side by side)
# --------------------------------------------------------
values2 = [5, 15, 10, 20]           # Second dataset
x_pos = np.arange(len(categories))   # Numeric positions for X-axis

plt.bar(x_pos - 0.2, values, width=0.4, label="Group1")  # First group
plt.bar(x_pos + 0.2, values2, width=0.4, label="Group2") # Second group
plt.xticks(x_pos, categories)  # Replace numeric ticks with category names
plt.title("Grouped Bar Plot")
plt.legend()                   # Show legend
plt.show()

# ------------------------------------------------------------
# Example 4: Bar with Edge Color
# -------------------------------
plt.bar(categories, values, color='orange', edgecolor='black')  
# edgecolor -> outline color of bars
plt.title("Bar with Edge Color")
plt.show()

# ------------------------------------------------------------
# Example 5: Bar Plot with Value Labels
# -------------------------------------
bars = plt.bar(categories, values)
# Loop through each bar to display value on top
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2,  # X-coordinate (center of bar)
             bar.get_height() + 0.5,          # Y-coordinate (slightly above bar)
             str(bar.get_height()),            # Text to display
             ha='center')                      # Center text horizontally

plt.title("Bar Plot with Values")
plt.show()

# ------------------------------------------------------------
# Example 6: Bar Plot with Custom Width
# -------------------------------------
plt.bar(categories, values, width=0.3, color='purple')  
# width -> thickness of bars
plt.title("Bar Plot with Custom Width")
plt.show()

# ------------------------------------------------------------
# Example 7: Stacked Bar Plot
# ---------------------------
plt.bar(categories, values, label='Values1')           # Bottom layer
plt.bar(categories, values2, bottom=values, label='Values2')  
# bottom -> stack second dataset on top of first
plt.title("Stacked Bar Plot")
plt.legend()
plt.show()

# ------------------------------------------------------------
# Example 8: Bar with Hatch Pattern
# ---------------------------------
plt.bar(categories, values, hatch='//', color='cyan')  
# hatch -> pattern inside bars for visual distinction
plt.title("Bar with Hatch Pattern")
plt.show()

# ------------------------------------------------------------
# Example 9: Horizontal Stacked Bars
# ----------------------------------
plt.barh(categories, values, label='Values1')          # Bottom layer
plt.barh(categories, values2, left=values, label='Values2')  
# left -> stack second dataset to the right
plt.title("Horizontal Stacked Bar Plot")
plt.legend()
plt.show()

# ------------------------------------------------------------
# Example 10: Bar Plot with Logarithmic Y-axis
# --------------------------------------------
plt.bar(categories, [100, 1000, 10000, 100000])  
plt.yscale('log')  # Logarithmic scale for Y-axis (useful for large ranges)
plt.title("Bar Plot with Log Scale")
plt.show()

# -------------------------
# 4. HISTOGRAM
# -------------------------
"""
Histogram: Represents frequency distribution of numeric data.
Used for: Understanding distribution, skewness, and patterns.
"""

# Example 1: Basic Histogram
# ---------------------------
data = np.random.randn(1000)  # Generate 1000 random numbers from standard normal distribution

plt.hist(data, bins=20, color='skyblue')  
# bins=20 -> number of intervals (bars) in histogram
# color -> color of bars

plt.title("Basic Histogram")  # Plot title
plt.show()

# ------------------------------------------------------------
# Example 2: Histogram with Custom Bins
# -------------------------------------
plt.hist(data, bins=50, color='orange')  
# bins=50 -> more bars for detailed distribution
plt.title("Histogram with 50 bins")
plt.show()

# ------------------------------------------------------------
# Example 3: Normalized Histogram (Density)
# -----------------------------------------
plt.hist(data, bins=20, density=True, color='green')  
# density=True -> normalizes histogram (area sums to 1)
plt.title("Normalized Histogram")
plt.show()

# ------------------------------------------------------------
# Example 4: Cumulative Histogram
# --------------------------------
plt.hist(data, bins=20, cumulative=True, color='purple')  
# cumulative=True -> each bin adds to previous, shows cumulative frequency
plt.title("Cumulative Histogram")
plt.show()

# ------------------------------------------------------------
# Example 5: Histogram with Multiple Datasets
# -------------------------------------------
data2 = np.random.randn(1000)  # Second dataset
plt.hist([data, data2], bins=20, color=['blue', 'red'], label=['Data1','Data2'])  
# Plot multiple histograms on same axes
plt.title("Histogram with Multiple Data")
plt.legend()  # Show legend
plt.show()

# ------------------------------------------------------------
# Example 6: Horizontal Histogram
# --------------------------------
plt.hist(data, bins=20, orientation='horizontal', color='pink')  
# orientation='horizontal' -> bars drawn horizontally
plt.title("Horizontal Histogram")
plt.show()

# ------------------------------------------------------------
# Example 7: Histogram with Edge Color
# ------------------------------------
plt.hist(data, bins=20, color='lightgreen', edgecolor='black')  
# edgecolor -> outline color for bars
plt.title("Histogram with Edge Color")
plt.show()

# ------------------------------------------------------------
# Example 8: Step Type Histogram
# -------------------------------
plt.hist(data, bins=20, histtype='step', color='red')  
# histtype='step' -> line-style histogram without filled bars
plt.title("Step Histogram")
plt.show()

# ------------------------------------------------------------
# Example 9: Bar Type Histogram
# ------------------------------
plt.hist(data, bins=20, histtype='bar', color='yellow')  
# histtype='bar' -> default bar-style histogram
plt.title("Bar Histogram")
plt.show()

# ------------------------------------------------------------
# Example 10: Stacked Histogram with Multiple Datasets
# ----------------------------------------------------
plt.hist([data, data2], bins=20, stacked=True, color=['blue','orange'])  
# stacked=True -> bars stacked on top of each other for comparison
plt.title("Stacked Histogram")
plt.show()


# ============================================================
# ADVANCED REAL-TIME DATA ANALYSIS: ONLINE STORE SALES
# ============================================================

# Import Libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Simulate daily sales data for 30 days
# ----------------------------------------------
days = np.arange(1, 31)  # Days 1 to 30
sales_units = np.random.randint(50, 200, size=30)            # Random units sold
revenue = sales_units * np.random.uniform(10, 20, size=30)   # Revenue in $

# Additional variables for advanced analysis
discounts = np.random.randint(0, 30, size=30)                # Discount % per day
customer_ratings = np.random.uniform(3.0, 5.0, size=30)     # Customer rating 3-5
returns = np.random.randint(0, 10, size=30)                 # Number of returns per day

# ============================================================
# 1. Line Plot - Daily Revenue Trend
# ============================================================
plt.plot(days, revenue, marker='o', color='blue', label="Revenue")
plt.title("Daily Revenue Trend")
plt.xlabel("Day")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.show()

# ============================================================
# 2. Line Plot - Highlight High Revenue Days
# ============================================================
plt.plot(days, revenue, marker='o', color='blue', label="Revenue")
plt.scatter(days[revenue>2500], revenue[revenue>2500], color='red', s=100, label="High Revenue Days")
plt.title("Revenue Trend with High Revenue Highlights")
plt.xlabel("Day")
plt.ylabel("Revenue ($)")
plt.legend()
plt.grid(True)
plt.show()

# ============================================================
# 3. Scatter Plot - Units Sold vs Revenue
# ============================================================
plt.scatter(sales_units, revenue, color='green', s=100, alpha=0.6)
plt.title("Units Sold vs Revenue")
plt.xlabel("Units Sold")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.show()

# ============================================================
# 4. Scatter Plot - Highlight High Units Sold (>150)
# ============================================================
plt.scatter(sales_units, revenue, color='green', s=100, alpha=0.6, label="Sales")
plt.scatter(sales_units[sales_units>150], revenue[sales_units>150], color='orange', s=120, label="High Units Sold")
plt.title("Units Sold vs Revenue with High Units Highlight")
plt.xlabel("Units Sold")
plt.ylabel("Revenue ($)")
plt.legend()
plt.grid(True)
plt.show()

# ============================================================
# 5. Bar Plot - Units Sold per Day
# ============================================================
plt.bar(days, sales_units, color='lightblue', edgecolor='black')
plt.title("Units Sold per Day")
plt.xlabel("Day")
plt.ylabel("Units Sold")
plt.show()

# ============================================================
# 6. Bar Plot - Highlight Low Selling Days (<80 units)
# ============================================================
plt.bar(days, sales_units, color='lightblue', edgecolor='black')
plt.title("Units Sold with Low-Selling Days Highlighted")
plt.xlabel("Day")
plt.ylabel("Units Sold")
for day, units in zip(days, sales_units):
    color = 'red' if units<80 else 'black'
    plt.text(day, units+2, str(units), ha='center', color=color, fontsize=8)
plt.show()

# ============================================================
# 7. Histogram - Revenue Distribution
# ============================================================
plt.hist(revenue, bins=10, color='skyblue', edgecolor='black')
plt.title("Revenue Distribution")
plt.xlabel("Revenue ($)")
plt.ylabel("Frequency")
plt.show()

# ============================================================
# 8. Histogram - Highlight High Revenue Bins (>2500)
# ============================================================
plt.hist(revenue, bins=10, color='skyblue', edgecolor='black')
for r in revenue:
    if r > 2500:
        plt.axvline(r, color='red', linestyle='--', alpha=0.5)
plt.title("Revenue Distribution with High Revenue Highlight")
plt.xlabel("Revenue ($)")
plt.ylabel("Frequency")
plt.show()

# ============================================================
# 9. Line Plot - Units Sold & Revenue (Dual Line Plot)
# ============================================================
plt.plot(days, sales_units, color='orange', marker='o', label="Units Sold")
plt.plot(days, revenue, color='blue', marker='x', label="Revenue")
plt.title("Units Sold vs Revenue Trend")
plt.xlabel("Day")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

# ============================================================
# 10. Scatter Plot - Discounts vs Revenue
# ============================================================
plt.scatter(discounts, revenue, color='purple', s=100, alpha=0.6)
plt.title("Discount vs Revenue")
plt.xlabel("Discount (%)")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.show()

# ============================================================
# 11. Conditional Scatter - Revenue Drops with High Discount (>20%)
# ============================================================
plt.scatter(discounts, revenue, color='purple', s=100, alpha=0.6, label="All Days")
plt.scatter(discounts[(discounts>20) & (revenue<1500)], 
            revenue[(discounts>20) & (revenue<1500)], color='red', s=120, label="High Discount & Low Revenue")
plt.title("Discount Impact on Revenue")
plt.xlabel("Discount (%)")
plt.ylabel("Revenue ($)")
plt.legend()
plt.grid(True)
plt.show()

# ============================================================
# 12. Bar Plot - Returns per Day
# ============================================================
plt.bar(days, returns, color='pink', edgecolor='black')
plt.title("Number of Returns per Day")
plt.xlabel("Day")
plt.ylabel("Returns")
plt.show()

# ============================================================
# 13. Highlight Days with Returns >5
# ============================================================
plt.bar(days, returns, color='pink', edgecolor='black')
plt.title("High Return Days Highlighted")
plt.xlabel("Day")
plt.ylabel("Returns")
plt.bar(days[returns>5], returns[returns>5], color='red', edgecolor='black')
plt.show()

# ============================================================
# 14. Histogram - Customer Ratings
# ============================================================
plt.hist(customer_ratings, bins=5, color='lightgreen', edgecolor='black')
plt.title("Customer Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()

# ============================================================
# 15. Line Plot - Revenue vs Customer Ratings
# ============================================================
plt.plot(days, revenue, color='blue', marker='o', label="Revenue")
plt.plot(days, customer_ratings*500, color='green', marker='x', label="Customer Rating x500")  # scale ratings for comparison
plt.title("Revenue vs Customer Ratings")
plt.xlabel("Day")
plt.ylabel("Revenue / Rating")
plt.legend()
plt.grid(True)
plt.show()

# ============================================================
# 16. Scatter Plot - Revenue vs Returns
# ============================================================
plt.scatter(returns, revenue, color='red', s=100)
plt.title("Revenue vs Returns")
plt.xlabel("Returns")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.show()

# ============================================================
# 17. Conditional Scatter - Revenue <1500 & Returns >5
# ============================================================
plt.scatter(returns, revenue, color='red', s=100, label="All Days")
plt.scatter(returns[(returns>5) & (revenue<1500)], revenue[(returns>5) & (revenue<1500)], 
            color='black', s=120, label="High Returns & Low Revenue")
plt.title("Revenue vs Returns with Conditional Highlight")
plt.xlabel("Returns")
plt.ylabel("Revenue ($)")
plt.legend()
plt.grid(True)
plt.show()

# ============================================================
# 18. Dual Histogram - Revenue vs Discounts
# ============================================================
plt.hist(revenue, bins=10, alpha=0.5, label='Revenue', color='blue')
plt.hist(discounts, bins=10, alpha=0.5, label='Discounts', color='orange')
plt.title("Revenue vs Discounts Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# ============================================================
# 19. Line Plot - Cumulative Revenue
# ============================================================
cumulative_revenue = np.cumsum(revenue)
plt.plot(days, cumulative_revenue, color='green', marker='o')
plt.title("Cumulative Revenue Over Month")
plt.xlabel("Day")
plt.ylabel("Cumulative Revenue ($)")
plt.grid(True)
plt.show()

# ============================================================
# 20. Highlight Peak Revenue Day
# ============================================================
plt.bar(days, revenue, color='lightblue', edgecolor='black')
peak_day = days[np.argmax(revenue)]
plt.bar(peak_day, revenue[np.argmax(revenue)], color='red', edgecolor='black', label="Peak Revenue Day")
plt.title("Highlight Peak Revenue Day")
plt.xlabel("Day")
plt.ylabel("Revenue ($)")
plt.legend()
plt.show()

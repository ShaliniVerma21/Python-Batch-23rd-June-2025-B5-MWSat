"""
===============================================================
Matplotlib Library – Advanced Visualization
===============================================================

Purpose:
Learn and implement all advanced visualization plots in Python 
using Matplotlib for data analytics, reporting, and research.

Matplotlib helps visualize data patterns, relationships, and 
distributions using various advanced plots like Pie Charts, 
Stacked Area Charts, Box Plots, Error Bars, Polar Plots, 
3D Plots, and more.

---------------------------------------------------------------
Key Advanced Concepts:
---------------------------------------------------------------
1. Subplots → Multiple plots in one figure.
2. 3D Plots → For representing three-dimensional data.
3. Error Bars & Filled Plots → To show uncertainty or variation.
4. Custom Colormaps & Styles → For presentation-ready visuals.
---------------------------------------------------------------
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# ============================================================
# 1️⃣ PIE CHART – 10 Examples
# ============================================================
"""
PIE CHART:
Represents proportions of categories in a circular chart.
- Used for: Showing % contribution of each category.
- Common in: Business reports, sales distribution, market share.
"""

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['red', 'blue', 'green', 'orange']

# Example 1: Basic Pie
plt.pie(sizes)
plt.title("Example 1 - Basic Pie Chart")
plt.show()

# Example 2: With Labels
plt.pie(sizes, labels=labels)
plt.title("Example 2 - Pie with Labels")
plt.show()

# Example 3: With Percentage
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Example 3 - Pie with Percentages")
plt.show()

# Example 4: Exploded Slice
plt.pie(sizes, labels=labels, explode=(0, 0.1, 0, 0))
plt.title("Example 4 - Exploded Slice")
plt.show()

# Example 5: Shadow
plt.pie(sizes, labels=labels, shadow=True)
plt.title("Example 5 - Pie with Shadow")
plt.show()

# Example 6: Custom Colors
plt.pie(sizes, labels=labels, colors=colors)
plt.title("Example 6 - Custom Colors")
plt.show()

# Example 7: Start Angle
plt.pie(sizes, labels=labels, startangle=180)
plt.title("Example 7 - Start Angle")
plt.show()

# Example 8: Donut Chart
plt.pie(sizes, labels=labels, wedgeprops=dict(width=0.4))
plt.title("Example 8 - Donut Chart")
plt.show()

# Example 9: Combined Features
plt.pie(sizes, labels=labels, explode=(0, 0.1, 0, 0), autopct='%1.1f%%', shadow=True)
plt.title("Example 9 - Combined Features Pie")
plt.show()

# Example 10: Equal Aspect Ratio
plt.pie(sizes, labels=labels)
plt.axis('equal')  # equal, auto, scaled,tight
plt.title("Example 10 - Equal Aspect Pie")
plt.show()


# ============================================================
# 2️⃣ STACKED AREA PLOT – 10 Examples
# ============================================================
"""
STACKED AREA PLOT:
Displays cumulative totals of multiple variables over time.
"""

x = np.arange(1, 6)
y1 = [3, 5, 7, 9, 10]
y2 = [1, 2, 4, 6, 7]
y3 = [2, 3, 5, 7, 8]

# Example 1: Basic Stack
plt.stackplot(x, y1, y2)
plt.title("Example 1 - Basic Stacked Area")
plt.show()

# Example 2: With Labels
plt.stackplot(x, y1, y2, y3, labels=['A', 'B', 'C'])
plt.legend()
plt.title("Example 2 - With Labels")
plt.show()

# Example 3: Custom Colors
plt.stackplot(x, y1, y2, colors=['red', 'green'])
plt.title("Example 3 - Custom Colors")
plt.show()

# Example 4: Trend Visualization
plt.stackplot(x, y1, y2, y3, labels=['Sales', 'Profit', 'Cost'])
plt.legend()
plt.title("Example 4 - Sales Trend")
plt.show()

# Example 5: Different Data Sets
x = np.arange(1, 11)
plt.stackplot(x, np.random.randint(1, 10, 10), np.random.randint(1, 10, 10))
plt.title("Example 5 - Random Data Stack")
plt.show()

# Example 6: Alpha Transparency
plt.stackplot(x, y1, y2, alpha=0.5)
plt.title("Example 6 - Transparent Stack")
plt.show()

# Example 7: With Grid
plt.stackplot(x, y1, y2)
plt.grid(True)
plt.title("Example 7 - Stack with Grid")
plt.show()

# Example 8: Styled Stack
plt.stackplot(x, y1, y2, colors=['skyblue', 'lightgreen'], labels=['Region 1', 'Region 2'])
plt.legend()
plt.title("Example 8 - Styled Stack")
plt.show()

# Example 9: Larger Dataset
x = np.arange(1, 21)
y1 = np.random.randint(10, 50, 20)  # 10-50 random integers size=20
y2 = np.random.randint(5, 25, 20)  # 5-25 random integers size=20
plt.stackplot(x, y1, y2)
plt.title("Example 9 - 20 Points Stack")
plt.show()

# Example 10: Area Trend
plt.stackplot(x, np.sin(x), np.cos(x))
plt.title("Example 10 - Sine-Cosine Stack")
plt.show()


# ============================================================
# 3️⃣ BOX PLOT – 10 Examples
# ============================================================
"""
BOX PLOT:
Shows data spread, median, quartiles, and outliers.
"""

data = np.random.randn(100)

# Example 1: Basic
plt.boxplot(data)
plt.title("Example 1 - Basic Box Plot")
plt.show()

# Example 2: Horizontal
plt.boxplot(data, vert=False)
plt.title("Example 2 - Horizontal Box")
plt.show()

# Example 3: Multiple Boxes
data2 = np.random.randn(100)
plt.boxplot([data, data2])
plt.title("Example 3 - Multiple Box Plot")
plt.show()

# Example 4: With Labels
plt.boxplot([data, data2], labels=['Data1', 'Data2'])
plt.title("Example 4 - Labeled Box Plot")
plt.show()

# Example 5: Show Mean
plt.boxplot(data, showmeans=True)
plt.title("Example 5 - Box with Mean")
plt.show()

# Example 6: Custom Flier Props
plt.boxplot(data, flierprops=dict(marker='o', color='red', markersize=8))
plt.title("Example 6 - Custom Outliers")
plt.show()

# Example 7: Patch Artist
plt.boxplot([data, data2], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title("Example 7 - Colored Box Plot")
plt.show()

# Example 8: Notched
plt.boxplot(data, notch=True)
plt.title("Example 8 - Notched Box")
plt.show()

# Example 9: Wider Box
plt.boxplot(data, widths=0.7)
plt.title("Example 9 - Wider Box")
plt.show()

# Example 10: Dataset Comparison
data3 = np.random.randn(100) * 2
plt.boxplot([data, data2, data3], labels=['A', 'B', 'C'])
plt.title("Example 10 - 3 Dataset Comparison")
plt.show()


# ============================================================
# 4️⃣ ERROR BAR PLOT – 10 Examples
# ============================================================
"""
ERROR BAR:
Used to show uncertainty or variation.
"""

x = np.arange(5)
y = [3, 5, 7, 9, 11]
yerr = [0.5, 0.2, 0.3, 0.4, 0.1]

# Example 1: Basic
plt.errorbar(x, y, yerr=yerr)
plt.title("Example 1 - Basic Error Bar")
plt.show()

# Example 2: Custom Color
plt.errorbar(x, y, yerr=yerr, color='red')
plt.title("Example 2 - Red Error Bar")
plt.show()

# Example 3: Capsize
plt.errorbar(x, y, yerr=yerr, capsize=5)
plt.title("Example 3 - With Caps")
plt.show()

# Example 4: Custom Marker
plt.errorbar(x, y, yerr=yerr, fmt='o', color='blue')
plt.title("Example 4 - Circle Markers")
plt.show()

# Example 5: Horizontal Error
plt.errorbar(x, y, xerr=0.3)
plt.title("Example 5 - Horizontal Error Bar")
plt.show()

# Example 6: Both Axes Error
plt.errorbar(x, y, yerr=yerr, xerr=0.2)
plt.title("Example 6 - Both Axis Error")
plt.show()

# Example 7: Thick Lines
plt.errorbar(x, y, yerr=yerr, lw=2)
plt.title("Example 7 - Thick Error Bar")
plt.show()

# Example 8: Color + Marker Combo
plt.errorbar(x, y, yerr=yerr, fmt='s', color='green', ecolor='black')
plt.title("Example 8 - Styled Error Bar")
plt.show()

# Example 9: With Grid
plt.errorbar(x, y, yerr=yerr)
plt.grid(True)
plt.title("Example 9 - Error Bar with Grid")
plt.show()

# Example 10: Randomized Data
for i in range(3):
    plt.errorbar(x, np.random.randint(5, 15, 5), yerr=np.random.rand(5), fmt='--o', label=f'Set {i+1}')
plt.legend()
plt.title("Example 10 - Multiple Error Bars")
plt.show()

# ============================================================
# ADVANCED VISUALIZATION – SITUATION-BASED PROBLEMS (PART 2)
# ============================================================

"""
Purpose:
Solve more real-world problems using advanced Matplotlib features 
such as histograms, annotations, barh charts, 3D surfaces, subplots, and color maps.
"""
# ------------------------------------------------------------
# Problem 11: Compare sales performance across regions (Bar Chart)
# ------------------------------------------------------------
regions = ['North', 'South', 'East', 'West']
sales_2024 = [420, 380, 460, 310]
sales_2025 = [480, 400, 520, 350]

x = np.arange(len(regions))
plt.bar(x - 0.2, sales_2024, width=0.4, label='2024', color='skyblue')
plt.bar(x + 0.2, sales_2025, width=0.4, label='2025', color='orange')
plt.xticks(x, regions)
plt.xlabel("Regions")
plt.ylabel("Sales (in units)")
plt.title("Regional Sales Comparison 2024 vs 2025")
plt.legend()
plt.show()

# ------------------------------------------------------------
# Problem 12: Visualize student marks distribution (Histogram)
# ------------------------------------------------------------
marks = np.random.normal(70, 10, 200)
plt.hist(marks, bins=15, color='purple', edgecolor='white')
plt.title("Student Marks Distribution")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.show()

# ------------------------------------------------------------
# Problem 13: Visualize weather temperature (Line + Fill)
# ------------------------------------------------------------
days = np.arange(1, 11)
temperature = np.random.randint(25, 40, 10)
plt.plot(days, temperature, color='red', marker='o')
plt.fill_between(days, temperature, color='orange', alpha=0.3)
plt.title("10-Day Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.show()

# ------------------------------------------------------------
# Problem 14: Display product share (Horizontal Bar)
# ------------------------------------------------------------
products = ['Laptops', 'Mobiles', 'Tablets', 'Accessories']
shares = [40, 55, 25, 15]
plt.barh(products, shares, color='green')
plt.title("Product Share in Market")
plt.xlabel("Percentage Share")
plt.show()

# ------------------------------------------------------------
# Problem 15: Visualize error trend with confidence interval
# ------------------------------------------------------------
x = np.linspace(0, 10, 100)
y = np.sin(x)
error = 0.2 + 0.2 * np.sqrt(x)
plt.plot(x, y, 'b-', label='Sine Curve')
plt.fill_between(x, y - error, y + error, color='blue', alpha=0.2)
plt.title("Sine Wave with Confidence Interval")
plt.legend()
plt.show()

# ------------------------------------------------------------
# Problem 16: 3D Surface Plot for Mathematical Function
# ------------------------------------------------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title("3D Surface Plot")
plt.show()

# ------------------------------------------------------------
# Problem 17: Annotate highest point in data
# ------------------------------------------------------------
x = np.linspace(0, 10, 100)
y = np.sin(x)
max_y = np.max(y)
max_x = x[np.argmax(y)]
plt.plot(x, y)
plt.scatter(max_x, max_y, color='red')
plt.annotate('Peak Point', xy=(max_x, max_y), xytext=(max_x+0.5, max_y),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.title("Annotated Sine Curve")
plt.show()

# ------------------------------------------------------------
# Problem 18: Display correlation between two variables (Scatter)
# ------------------------------------------------------------
x = np.random.rand(100)
y = x * 2 + np.random.rand(100) * 0.5
plt.scatter(x, y, color='teal', alpha=0.6)
plt.title("Correlation between X and Y")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# ------------------------------------------------------------
# Problem 19: Monthly revenue trend using multiple subplots
# ------------------------------------------------------------
months = np.arange(1, 13)
revenue_2024 = np.random.randint(40, 100, 12)
revenue_2025 = np.random.randint(60, 120, 12)

fig, ax = plt.subplots(2, 1, figsize=(8, 6))
ax[0].plot(months, revenue_2024, 'bo-', label='2024')
ax[1].plot(months, revenue_2025, 'go-', label='2025')
ax[0].set_title("Revenue 2024")
ax[1].set_title("Revenue 2025")
for a in ax:
    a.set_xlabel("Month")
    a.set_ylabel("Revenue")
    a.legend()
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# Problem 20: Visualize data with color mapping (Heatmap)
# ------------------------------------------------------------
data = np.random.rand(10, 10)
plt.imshow(data, cmap='coolwarm', interpolation='nearest')
plt.title("Heatmap Example")
plt.colorbar(label="Intensity")
plt.show()

# ============================================================
# THEORY – ADVANCED MATPLOTLIB CONCEPTS
# ============================================================
"""
1. **Customization Options**
   - Color styles: 'dark_background', 'ggplot', 'seaborn'
   - Line styles: '-', '--', '-.', ':'
   - Marker styles: 'o', '*', '^', 's'
   - Titles, legends, grids, and axes control.

2. **Performance Optimization**
   - Use NumPy arrays for faster computations.
   - Avoid unnecessary redraws in large datasets.
   - Use interactive backends like `%matplotlib notebook`.

3. **3D and Interactive Plots**
   - `Axes3D`: For line, scatter, and surface plots in 3D.
   - Widgets and sliders from `matplotlib.widgets` can be used for interactivity.

4. **Subplots & Layout**
   - `plt.subplot()` for quick layouts.
   - `plt.subplots()` for flexible control with figure and axes objects.

5. **Color Maps**
   - Used to represent intensity (like in heatmaps).
   - Popular colormaps: `viridis`, `plasma`, `coolwarm`, `inferno`.

6. **Annotations & Text**
   - Use `plt.annotate()` to highlight key points.
   - Useful in scientific and financial charts for clarity.

7. **Exporting Figures**
   - Save plots as image or PDF using `plt.savefig('chart.png', dpi=300)`.

8. **Integration**
   - Matplotlib works with Pandas, NumPy, and Seaborn for advanced data visualization pipelines.

9. **Presentation Tips**
   - Use consistent colors, legends, and labels.
   - Avoid overloading charts with too much data.
   - Make use of gridlines and axis labels.

10. **Real-world Usage**
    - Data analysts use Matplotlib for:
        * Sales trend visualization
        * Financial data analytics
        * Machine learning feature analysis
        * Academic & scientific reporting
"""

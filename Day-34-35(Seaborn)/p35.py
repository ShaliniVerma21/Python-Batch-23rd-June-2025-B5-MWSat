""" 
Seaborn Advanced Visualization
--------------------------------------
1. Distribution, Regression, Categorical & Matrix plots
2. Pair plots, Heatmaps, Violin, Swarm, etc.
3. Advanced customization & palette control
4. Real-life dataset analysis (Tips Dataset – Restaurant Billing & Tips Analysis)
"""

"""
===============================================================
Day 34: Seaborn - Advanced Visualization
File: p35.py
===============================================================

📘 Objective:
Learn and implement advanced visualizations in Seaborn including
distributions, regression, categorical, and matrix plots.

Understand how to explore relationships, trends, and patterns
using real-world data.

===============================================================
"""

# --------------------------------------------------------------
# Import Libraries
# --------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load built-in dataset
df = sns.load_dataset("tips")
print("Tips Dataset Preview:\n", df.head())

# --------------------------------------------------------------
# Example 1: Distribution Plot
# --------------------------------------------------------------
sns.displot(df["total_bill"], kde=True, color="green")
plt.title("Distribution of Total Bill")
plt.show()

# --------------------------------------------------------------
# Example 2: Joint Plot
# --------------------------------------------------------------
sns.jointplot(x="total_bill", y="tip", data=df, kind="scatter")
plt.suptitle("Joint Plot - Bill vs Tip", y=1.02)
plt.show()

# --------------------------------------------------------------
# Example 3: Regression Plot
# --------------------------------------------------------------
sns.regplot(x="total_bill", y="tip", data=df)
plt.title("Regression Plot - Bill vs Tip with Regression Line")
plt.show()

# --------------------------------------------------------------
# Example 4: Pair Plot
# --------------------------------------------------------------
sns.pairplot(df, hue="sex")
plt.suptitle("Pair Plot - Tips Dataset Relationships", y=1.02)
plt.show()

# --------------------------------------------------------------
# Example 5: Heatmap
# --------------------------------------------------------------
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap - Numerical Columns")
plt.show()

# --------------------------------------------------------------
# Example 6: Cat Plot
# --------------------------------------------------------------
sns.catplot(x="day", y="total_bill", hue="sex", kind="bar", data=df)
plt.title("Categorical Plot - Bill by Day and Gender")
plt.show()

# --------------------------------------------------------------
# Example 7: Violin Plot
# --------------------------------------------------------------
sns.violinplot(x="day", y="tip", hue="sex", split=True, data=df)
plt.title("Violin Plot - Tip Distribution by Gender & Day")
plt.show()

# --------------------------------------------------------------
# Example 8: Swarm Plot
# --------------------------------------------------------------
sns.swarmplot(x="day", y="total_bill", data=df)
plt.title("Swarm Plot - Total Bill Distribution by Day")
plt.show()

# --------------------------------------------------------------
# Example 9: Boxen Plot
# --------------------------------------------------------------
sns.boxenplot(x="day", y="total_bill", data=df)
plt.title("Boxen Plot - Detailed Distribution of Bills")
plt.show()

# --------------------------------------------------------------
# Example 10: KDE Plot
# --------------------------------------------------------------
sns.kdeplot(df["tip"], shade=True, color="orange")
plt.title("KDE Plot - Tip Amount Density")
plt.show()

# --------------------------------------------------------------
# Real-Life Analysis: Restaurant Tips Analysis
# --------------------------------------------------------------
"""
🎯 Objective:
Analyze restaurant tipping behavior to understand how total bill,
day, and gender affect the tip amount.

Dataset: Seaborn 'tips' dataset
"""

sns.lmplot(x="total_bill", y="tip", hue="sex", col="day", data=df, aspect=0.8)
plt.suptitle("Tipping Pattern Analysis by Day and Gender", y=1.05)
plt.show()

"""
✅ Insights:
- Tips increase linearly with total bill amount.
- Males tend to give slightly higher tips on weekends.
- Sunday has the highest average bill and tip combination.

🎓 Use Case:
Such analysis is used by restaurants to optimize service quality,
staff allocation, and promotional offers based on customer
spending behavior.
"""

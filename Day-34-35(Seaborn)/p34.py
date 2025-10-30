""" 
Seaborn Basic to Intermediate Visualization
----------------------------------------------
1. Introduction to Seaborn
2. Dataset loading
3. Basic plots (10 types)
4. Customization, styling, and labeling
5. Real-life dataset analysis (Titanic Dataset)
"""

"""
Objective:
Learn and implement basic and intermediate data visualizations
using Seaborn library to understand patterns, distributions, and
comparisons in datasets.

Seaborn is built on top of Matplotlib and integrates well with
pandas DataFrames.
===============================================================
"""

# --------------------------------------------------------------
# Import Libraries
# --------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load sample dataset
df = sns.load_dataset("titanic")
print("Titanic Dataset Preview:\n", df.head())

# --------------------------------------------------------------
# Example 1: Scatter Plot
# --------------------------------------------------------------
sns.scatterplot(data=df, x="age", y="fare", hue="class")
plt.title("Scatter Plot - Age vs Fare by Class")
plt.show()

# --------------------------------------------------------------
# Example 2: Line Plot
# --------------------------------------------------------------
sns.lineplot(x="age", y="fare", data=df)
plt.title("Line Plot - Age vs Fare")
plt.show()

# --------------------------------------------------------------
# Example 3: Histogram
# --------------------------------------------------------------
sns.histplot(df["age"], kde=True, bins=30, color="skyblue")
plt.title("Histogram - Age Distribution")
plt.show()

# --------------------------------------------------------------
# Example 4: Bar Plot
# --------------------------------------------------------------
sns.barplot(x="class", y="fare", data=df)
plt.title("Bar Plot - Average Fare by Class")
plt.show()

# --------------------------------------------------------------
# Example 5: Count Plot
# --------------------------------------------------------------
sns.countplot(x="class", data=df, hue="sex")
plt.title("Count Plot - Class Distribution by Gender")
plt.show()

# --------------------------------------------------------------
# Example 6: Box Plot
# --------------------------------------------------------------
sns.boxplot(x="class", y="fare", data=df)
plt.title("Box Plot - Fare Distribution by Class")
plt.show()

# --------------------------------------------------------------
# Example 7: Violin Plot
# --------------------------------------------------------------
sns.violinplot(x="class", y="age", data=df, palette="pastel")
plt.title("Violin Plot - Age by Class")
plt.show()

# --------------------------------------------------------------
# Example 8: Strip Plot
# --------------------------------------------------------------
sns.stripplot(x="class", y="fare", data=df, jitter=True)
plt.title("Strip Plot - Fare by Class")
plt.show()

# --------------------------------------------------------------
# Example 9: Swarm Plot
# --------------------------------------------------------------
sns.swarmplot(x="class", y="age", data=df)
plt.title("Swarm Plot - Age Distribution per Class")
plt.show()

# --------------------------------------------------------------
# Example 10: Pair Plot
# --------------------------------------------------------------
sns.pairplot(df[["age", "fare", "pclass", "survived"]], hue="survived")
plt.suptitle("Pair Plot - Relationship among Key Variables", y=1.02)
plt.show()

# --------------------------------------------------------------
# Real-Life Analysis: Titanic Survival Study
# --------------------------------------------------------------
"""
🎯 Objective:
Analyze the relationship between class, gender, and survival rate
in the Titanic dataset using Seaborn visualizations.
"""

sns.barplot(x="class", y="survived", hue="sex", data=df)
plt.title("Survival Rate by Class and Gender")
plt.ylabel("Survival Probability")
plt.show()

"""
✅ Insights:
- Females had a much higher survival rate than males.
- First-class passengers had better survival chances.
- Lower-class male passengers were least likely to survive.

🎓 Use Case:
This type of analysis helps data scientists understand human
survival factors in disasters, applicable in safety & evacuation
planning for transport industries.
"""

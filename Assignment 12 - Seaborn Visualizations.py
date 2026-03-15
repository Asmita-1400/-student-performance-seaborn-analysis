# ===============================
# Assignment 12 - Seaborn Visualizations
# Libraries: Pandas, Seaborn, Matplotlib
# ===============================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("StudentsPerformance.csv")

# Display first rows
print(df.head())

# =====================================
# Task 1: Relational Plot
# =====================================

sns.relplot(
    data=df,
    x="math score",
    y="reading score",
    hue="gender"
)

plt.title("Relational Plot: Math vs Reading Score")
plt.show()

# Scatter style relational plot
sns.relplot(
    data=df,
    x="math score",
    y="reading score",
    hue="gender",
    kind="scatter"
)

plt.title("Scatter Relational Plot")
plt.show()


# =====================================
# Task 2: Line Plot + Facet
# =====================================

sns.lineplot(
    data=df,
    x="math score",
    y="reading score"
)

plt.title("Line Plot: Math vs Reading")
plt.show()

# Scatter style line
sns.lineplot(
    data=df,
    x="math score",
    y="reading score",
    marker="o"
)

plt.title("Scatter Style Line Plot")
plt.show()

# Faceting using categorical column
sns.relplot(
    data=df,
    x="math score",
    y="reading score",
    col="gender",
    kind="scatter"
)

plt.show()


# =====================================
# Task 3: Distribution Plots
# =====================================

# Histogram
sns.histplot(df["math score"], bins=10)
plt.title("Histogram of Math Scores")
plt.show()

# KDE plot
sns.kdeplot(df["math score"])
plt.title("KDE Plot of Math Scores")
plt.show()

# Rug plot
sns.rugplot(df["math score"])
plt.title("Rug Plot of Math Scores")
plt.show()

# Histogram + KDE
sns.histplot(df["math score"], kde=True)
plt.title("Histogram + KDE")
plt.show()


# =====================================
# Task 4: Bivariate Distribution
# =====================================

# Bivariate Histogram
sns.histplot(
    data=df,
    x="math score",
    y="reading score"
)

plt.title("Bivariate Histogram")
plt.show()

# Bivariate KDE
sns.kdeplot(
    data=df,
    x="math score",
    y="reading score"
)

plt.title("Bivariate KDE")
plt.show()


# =====================================
# Task 5: Matrix Plots
# =====================================

# Pairplot
sns.pairplot(df[["math score","reading score","writing score"]])
plt.show()

# Correlation Heatmap
corr = df[["math score","reading score","writing score"]].corr()

sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")
plt.show()


# =====================================
# Task 6: Categorical Plots
# =====================================

# Bar Plot
sns.barplot(
    data=df,
    x="gender",
    y="math score"
)

plt.title("Bar Plot")
plt.show()

# Box Plot
sns.boxplot(
    data=df,
    x="gender",
    y="math score"
)

plt.title("Box Plot")
plt.show()

# Violin Plot
sns.violinplot(
    data=df,
    x="gender",
    y="math score"
)

plt.title("Violin Plot")
plt.show()

# Count Plot
sns.countplot(
    data=df,
    x="gender"
)

plt.title("Count Plot")
plt.show()


# =====================================
# Task 7: Regression Plots
# =====================================

# Regression Plot
sns.regplot(
    data=df,
    x="math score",
    y="reading score"
)

plt.title("Regression Plot")
plt.show()

# lmplot with categorical hue
sns.lmplot(
    data=df,
    x="math score",
    y="reading score",
    hue="gender"
)

plt.show()


# =====================================
# Task 8: Multi-Plots / FacetGrid
# =====================================

# FacetGrid
g = sns.FacetGrid(df, col="gender")
g.map(sns.scatterplot, "math score", "reading score")
plt.show()

# Multi-plot dashboard using relplot
sns.relplot(
    data=df,
    x="math score",
    y="reading score",
    hue="gender",
    col="test preparation course"
)

plt.show()

# Multi-plot categorical
sns.catplot(
    data=df,
    x="gender",
    y="math score",
    kind="box",
    col="test preparation course"
)

plt.show()

# Distribution multi-plot
sns.displot(
    data=df,
    x="math score",
    col="gender",
    kde=True
)

plt.show()
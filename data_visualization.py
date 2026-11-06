# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Taxis dataset
df = sns.load_dataset("taxis")

# Display first 5 rows
print(df.head())

# Display dataset information
print(df.info())

# Display number of rows and columns
print("Dataset Shape:", df.shape)

# Display column names
print("Column Names:", df.columns)
# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check total missing values
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# Separate numerical and categorical columns
numerical_columns = df.select_dtypes(include=np.number).columns
categorical_columns = df.select_dtypes(include="object").columns

# Fill numerical missing values using median
for column in numerical_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill categorical missing values using mode
for column in categorical_columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna(df[column].mode()[0])

# Remove rows with missing critical values
df = df.dropna(subset=["pickup", "fare"])

# Check missing values again
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nCleaned Dataset Shape:", df.shape)
# Convert pickup column into datetime format
df["pickup"] = pd.to_datetime(df["pickup"])

# Sort data by pickup time
df = df.sort_values("pickup")

# Create line chart
plt.figure(figsize=(10, 5))

plt.plot(df["pickup"], df["fare"])

plt.title("Fare Over Time")
plt.xlabel("Pickup Time")
plt.ylabel("Fare Amount")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# BAR CHART

borough_fare = df.groupby("pickup_borough")["fare"].sum()

plt.figure(figsize=(8, 5))

borough_fare.plot(kind="bar")

plt.title("Total Fare by Pickup Borough")
plt.xlabel("Pickup Borough")
plt.ylabel("Total Fare")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
# PIE CHART

payment_counts = df["payment"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    payment_counts,
    labels=payment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Distribution of Trips by Payment Method")
plt.show()
# HISTOGRAM

plt.figure(figsize=(8, 5))

df["distance"].dropna().plot(
    kind="hist",
    bins=20,
    edgecolor="black"
)

plt.title("Distribution of Taxi Trip Distance")
plt.xlabel("Distance")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
# BOX PLOT

plt.figure(figsize=(9, 5))

df.boxplot(
    column="tip",
    by="pickup_borough"
)

plt.title("Tip Distribution by Pickup Borough")
plt.suptitle("")
plt.xlabel("Pickup Borough")
plt.ylabel("Tip Amount")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# COUNT PLOT

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="pickup_borough"
)

plt.title("Number of Trips by Pickup Borough")
plt.xlabel("Pickup Borough")
plt.ylabel("Number of Trips")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# SCATTER PLOT

plt.figure(figsize=(9, 5))

sns.scatterplot(
    data=df,
    x="distance",
    y="fare",
    hue="pickup_borough"
)

plt.title("Relationship Between Distance and Fare")
plt.xlabel("Distance")
plt.ylabel("Fare")

plt.tight_layout()
plt.show()
# HEATMAP

numeric_data = df[
    ["distance", "fare", "tip", "tolls", "total"]
]

correlation = numeric_data.corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()
# PAIR PLOT

pair_data = df[
    ["distance", "fare", "tip", "total", "pickup_zone"]
].dropna()

# Use a sample of 500 rows for faster plotting
pair_data = pair_data.sample(
    n=min(500, len(pair_data)),
    random_state=42
)

sns.pairplot(
    pair_data,
    vars=["distance", "fare", "tip", "total"],
    hue="pickup_zone"
)

plt.show()
# VIOLIN PLOT

plt.figure(figsize=(8, 5))

sns.violinplot(
    data=df,
    x="payment",
    y="fare"
)

plt.title("Fare Distribution by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Fare Amount")

plt.tight_layout()
plt.show()
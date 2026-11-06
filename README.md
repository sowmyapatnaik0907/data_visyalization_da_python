# Python Data Analytics Assignment 2 – Data Visualization

## Project Overview
This project focuses on data visualization using Python. The Seaborn Taxis dataset is used to analyze taxi trip information and create different visualizations to understand patterns and relationships in the data.

## Dataset
- **Dataset Name:** Taxis Dataset
- **Source:** Seaborn
- **Dataset Loading:** `sns.load_dataset("taxis")`

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code

## Project Tasks

### 1. Loading the Dataset
Loaded the Taxis dataset using Seaborn.

### 2. Handling Missing Values
- Identified missing values.
- Filled numerical missing values using median.
- Filled categorical missing values using mode.
- Removed rows with missing critical values.

### 3. Data Visualization

**Visualizations using Matplotlib and Pandas:**

1. Line Chart – Fare over time.
2. Bar Chart – Total fare by pickup borough.
3. Pie Chart – Distribution of trips by payment method.
4. Histogram – Distribution of trip distance.
5. Box Plot – Tip distribution by pickup borough.

**Visualizations using Seaborn:**

6. Count Plot – Number of trips by pickup borough.
7. Scatter Plot – Relationship between distance and fare.
8. Heatmap – Correlation between numerical variables.
9. Pair Plot – Pairwise relationships between numerical variables.
10. Violin Plot – Fare distribution by payment method.

## Project Structure

```text
Python_DA_Assignment_2/
│
├── data_visualization.py
├── taxis.csv
└── README.md
```

## How to Run the Project

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

4. Run the Python file:

```bash
python data_visualization.py
```

## Learning Outcomes
- Understanding dataset loading and cleaning.
- Handling missing values.
- Creating different types of data visualizations.
- Understanding relationships between numerical variables.
- Analyzing data using Python libraries.

## Conclusion
This project demonstrates how Python libraries can be used to clean, analyze, and visualize real-world taxi trip data through different graphical representations.

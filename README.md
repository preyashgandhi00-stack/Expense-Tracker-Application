# Expense-Tracker-Application
# Smart Expense Tracker

## Project Overview

The **Smart Expense Tracker** is a Python-based application that helps users manage and analyze their daily expenses. It allows users to add expenses, view summary statistics, filter records, and generate visual reports using graphs. The system reads and stores data in a **CSV file** and uses data analysis libraries to process and visualize the information.

---

## Features

* Add new expense records to the dataset
* View summary statistics such as **total expenses** and **average expense**
* Filter expenses by **category, amount, or date range**
* Generate visual reports using graphs
* View all stored CSV data
* Upload a custom dataset or use the default dataset

---

## Technologies Used

* **Python**
* **Pandas** – Dataset handling
* **NumPy** – Numerical calculations
* **Matplotlib** – Graph visualization
* **Seaborn** – Statistical visualizations

---

## Dataset Structure

The dataset is stored in a CSV file named **expenses_100_records.csv**.

### Columns

| Column      | Description                                                        |
| ----------- | ------------------------------------------------------------------ |
| Date        | Date of the expense (YYYY-MM-DD)                                   |
| Amount      | Expense amount                                                     |
| Category    | Expense category (Food, Transport, Utilities, Entertainment, etc.) |
| Description | Additional details about the expense                               |

Example:

```
Date,Amount,Category,Description
2024-01-01,50,Food,Lunch
2024-01-02,20,Transport,Bus ticket
2024-01-03,100,Utilities,Electricity bill
```

---

## Program Workflow

1. Choose dataset option:

   * Use default dataset (`expenses_100_records.csv`)
   * Upload custom dataset

2. Main Menu Options:

   * Add Expense
   * View Summary
   * Filter Expenses
   * Generate Graph
   * Show All CSV Data
   * Exit

---

## Graph Reports

The program can generate the following graphs:

1. **Bar Chart** – Total expenses by category
2. **Line Graph** – Spending trend over time
3. **Pie Chart** – Expense distribution by category
4. **Histogram** – Distribution of expense amounts


---

## Example Output

```
====== Smart Expense Tracker ======

1. Add Expense
2. View Summary
3. Filter Expenses
4. Generate Graph
5. Show All CSV Data
6. Exit
```

---

## Project Structure

```
SmartExpenseTracker/
│
├── expense_tracker.py
├── expenses.csv
└── README.md
```

---

## Learning Outcomes

This project demonstrates:

* Object-Oriented Programming in Python
* Data handling using Pandas
* Numerical analysis using NumPy
* Data visualization using Matplotlib and Seaborn
* File handling using CSV datasets

---

## Author

Preyash Gandhi

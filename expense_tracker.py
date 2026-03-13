import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ExpenseTracker class using OOP
class ExpenseTracker:

    # Constructor: load dataset from CSV file
    def __init__(self, file_name):
        self.file_name = file_name

        try:
            # Try reading existing dataset
            self.data = pd.read_csv(self.file_name)

        except FileNotFoundError:
            # If file does not exist, create a new empty dataset
            print("File not found. Creating new dataset.")

            self.data = pd.DataFrame(
                columns=["Date", "Amount", "Category", "Description"]
            )

            # Save empty dataset
            self.data.to_csv(self.file_name, index=False)

        # filtered_data is used when user filters dataset
        self.filtered_data = self.data


    # Function to add new expense into dataset
    def add_expense(self, date, amount, category, description):

        # Validate amount
        if amount <= 0:
            print("Amount must be positive.")
            return

        # Create new row
        new_expense = pd.DataFrame({
            "Date": [date],
            "Amount": [amount],
            "Category": [category],
            "Description": [description]
        })

        # Append row to dataset
        self.data = pd.concat([self.data, new_expense], ignore_index=True)

        # Save updated dataset to CSV file
        self.data.to_csv(self.file_name, index=False)

        print("Expense added successfully!")


    # Function to calculate summary statistics
    def get_summary(self):

        # Check if dataset is empty
        if self.data.empty:
            print("Dataset is empty")
            return

        # Convert Amount column into numpy array
        amounts = np.array(self.data["Amount"])

        # Calculate statistics
        total = np.sum(amounts)
        avg = np.mean(amounts)

        print("\n====== Expense Summary ======")
        print("Total Expenses:", total)
        print("Average Expense:", avg)

        # Group expenses by category
        print("\nCategory-wise Expenses:")
        print(self.data.groupby("Category")["Amount"].sum())


    # Show full dataset from CSV
    def show_all_data(self):

        print("\nAll CSV Data\n")
        print(self.data)


    # Filter dataset based on condition
    def filter_expenses(self, condition):

        if condition == "category":

            # Filter by category
            category = input("Enter category: ")
            result = self.data[self.data["Category"] == category]

        elif condition == "amount":

            # Filter by minimum amount
            amount = float(input("Enter minimum amount: "))
            result = self.data[self.data["Amount"] >= amount]

        elif condition == "date":

            # Filter between date range
            start = input("Enter start date (YYYY-MM-DD): ")
            end = input("Enter end date (YYYY-MM-DD): ")

            result = self.data[
                (self.data["Date"] >= start) &
                (self.data["Date"] <= end)
            ]

        elif condition == "all":

            # Show all dataset
            result = self.data

        else:
            print("Invalid filter")
            return

        # Save filtered data for graph generation
        self.filtered_data = result

        print("\nFiltered Expenses:\n")
        print(result)


    # Generate visual reports
    def generate_report(self):

        # If filtered dataset empty
        if self.filtered_data.empty:
            print("No data available for graph")
            return

        # Work on filtered dataset
        df = self.filtered_data.copy()

        # Convert date column into datetime format
        df["Date"] = pd.to_datetime(df["Date"])

        # Group expenses by category
        category_total = df.groupby("Category")["Amount"].sum()

        print("\n====== Graph Reports ======")
        print("1. Bar Chart")
        print("2. Line Graph")
        print("3. Pie Chart")
        print("4. Histogram")

        try:
            choice = int(input("Enter graph choice: "))
        except:
            print("Invalid input")
            return


        # Bar Chart
        if choice == 1:

            plt.figure()
            category_total.plot(kind="bar")

            plt.title("Total Expenses by Category")
            plt.xlabel("Category")
            plt.ylabel("Amount")

            plt.show()


        # Line Graph (spending trend)
        elif choice == 2:

            monthly = df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum()

            plt.figure()
            monthly.plot(kind="line", marker="o")

            plt.title("Spending Trend Over Time")
            plt.xlabel("Month")
            plt.ylabel("Amount")

            plt.show()


        # Pie Chart
        elif choice == 3:

            plt.figure()
            category_total.plot(kind="pie", autopct="%1.1f%%")

            plt.title("Spending Distribution")
            plt.ylabel("")

            plt.show()


        # Histogram
        elif choice == 4:

            plt.figure()

            sns.histplot(df["Amount"], bins=10)

            plt.title("Expense Distribution")
            plt.xlabel("Amount")
            plt.ylabel("Frequency")

            plt.show()

        else:
            print("Invalid choice")


# Main function (Program entry point)
def main():

    print("Choose Dataset Option")
    print("1. Use Default Dataset (expenses.csv)")
    print("2. Upload Custom Dataset")

    try:
        dataset_choice = int(input("Enter choice: "))
    except:
        print("Invalid input")
        return


    # Select dataset file
    if dataset_choice == 1:
        file_name = "expenses.csv"

    elif dataset_choice == 2:
        file_name = input("Enter CSV file path: ")

    else:
        print("Invalid choice")
        return


    # Create tracker object
    tracker = ExpenseTracker(file_name)


    # Main program loop
    while True:

        print("\n====== Smart Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Filter Expenses")
        print("4. Generate Graph")
        print("5. Show All CSV Data")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Invalid input")
            continue


        # Add new expense
        if choice == 1:

            date = input("Enter Date (YYYY-MM-DD): ")

            try:
                amount = float(input("Enter Amount: "))
            except:
                print("Invalid amount")
                continue

            category = input("Enter Category: ")
            description = input("Enter Description: ")

            tracker.add_expense(date, amount, category, description)


        # View summary statistics
        elif choice == 2:

            tracker.get_summary()


        # Filter dataset
        elif choice == 3:

            print("\nFilter Options")
            print("1 Category")
            print("2 Amount")
            print("3 Date")
            print("4 Show All")

            try:
                f = int(input("Enter filter option: "))
            except:
                print("Invalid option")
                continue

            if f == 1:
                tracker.filter_expenses("category")

            elif f == 2:
                tracker.filter_expenses("amount")

            elif f == 3:
                tracker.filter_expenses("date")

            elif f == 4:
                tracker.filter_expenses("all")


        # Generate graphs
        elif choice == 4:

            tracker.generate_report()


        # Show full dataset
        elif choice == 5:

            tracker.show_all_data()


        # Exit program
        elif choice == 6:

            print("Exiting program")
            break

        else:
            print("Invalid option")


# Run program
if __name__ == "__main__":
    main()
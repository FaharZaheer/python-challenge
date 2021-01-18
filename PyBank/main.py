import csv
import os
#file = os.path.abspath("mydir/myfile.txt")
#print(file)
# Variable Declaration
Total = 0
P_L_List = []
Date_List = []
Change_List = []
#file = "C:/Users/fahar/OneDrive/Desktop/git_repos/python-challenge/PyBank/Resources/budget_data.csv" 
#file = "../Resources/budget_data.csv"
file = os.path.abspath("Resources/budget_data.csv")
with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader: # Extract data from the CSV file
        if line_count == 0:
            line_count += 1
        else:
            Total = Total + int(row[1])
            Date_List.append(str(row[0]))
            P_L_List.append(int(row[1]))
            line_count += 1
    for i in range(len(P_L_List)): # Compute the monthly change and store it in the list
        if i == 0:
            Change_List = []
        else:
            Change_List.append((P_L_List[i] - P_L_List[i - 1]))

    # Display the results in the Terminal
    print("\nFinancial Analysis")
    print("----------------------------")
    print(f'Total Months: {line_count - 1}')
    print(f'Total :$ {Total}')
    print(f'Average  Change: $ {round(sum(Change_List) / len(Change_List),2)}')
    print(f'Greatest Increase in Profits: {Date_List[Change_List.index(max(Change_List)) + 1]} (${Change_List[Change_List.index(max(Change_List))]})')
    print(f'Greatest Decrease in Profits: {Date_List[Change_List.index(min(Change_List)) + 1]} (${Change_List[Change_List.index(min(Change_List))]})')

    # Save the results in a txt file
    f = open("FinancialAnalysis.txt", "w") # open the txt file
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f'Total Months: {line_count - 1}\n')
    f.write(f'Total :$ {Total}\n')
    f.write(f'Average  Change: $ {round(sum(Change_List) / len(Change_List),2)}\n')
    f.write(f'Greatest Increase in Profits: {Date_List[Change_List.index(max(Change_List)) + 1]} (${Change_List[Change_List.index(max(Change_List))]})\n')
    f.write(f'Greatest Decrease in Profits: {Date_List[Change_List.index(min(Change_List)) + 1]} (${Change_List[Change_List.index(min(Change_List))]})\n')
    f.close()  # Close the txt file
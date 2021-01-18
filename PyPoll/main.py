import csv
import os
myList = []
file = os.path.abspath("Resources/election_data.csv")
with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            myList = []
            line_count += 1
        else:
            myList.append({'Candidate':row[2]})
            line_count += 1
    
    s = set( val for dic in myList for val in dic.values()) # to get the number of unique candidates
    
    result_dic = {} 
    for x in s:
        x_count = 0
        
        for row in myList:
            if x == row['Candidate']:
                x_count = x_count +1
        
        result_dic.update({x:x_count})
        
    
    # sort the result_dic in decending order
    sort_result_dic = sorted(result_dic.items(), key=lambda x: x[1], reverse=True) # got this from https://careerkarma.com/blog/python-sort-a-dictionary-by-value
    
    f = open("ElectionResults.txt", "w") # open the txt file
    
    print("\nElections Results")
    print("-------------------------")
    f.write("Elections Results\n")
    f.write("-------------------------\n")

    print(f'Total Votes: {line_count - 1}')
    f.write(f'Total Votes: {line_count - 1}\n')

    print("-------------------------")
    f.write("-------------------------\n")

    for i in sort_result_dic:
        print(i[0],': ', round((i[1]/(line_count-1))*100,3),'% (',i[1],')' )
        f.write(f'{i[0]}: {round((i[1]/(line_count-1))*100,3)}% ({i[1]})\n')
        
    print("-------------------------")
    f.write("-------------------------\n")

    print(f'Winner: {sort_result_dic[0][0]}')
    f.write(f'Winner: {sort_result_dic[0][0]}\n')
    print("-------------------------")
    f.write("-------------------------\n")
    
    f.close()  # Close the txt file
import csv

with open('data.txt') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')#delimiter specifies the character used to separate each field. 
    b=True
    while(b):

        a=input('provide input ')
        for row in csv_reader:
            if a==row[0]:#compare to user inputs in csv file
                print(row[1])#print computer output
        c=input('want to exit(EXIT/n)')#to help exit
        if(c=='EXIT'):
            b==False
            

        
    

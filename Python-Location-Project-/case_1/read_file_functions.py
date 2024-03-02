

# CASE 1 read file functions


from csv import reader


# Open_with_read_file function to read file 
def Open_with_read_file(path):
    
    try:
        
        with open(path, "r") as my_csv_f:
        
            print(' - [ UPCOMING STEP ] - Reading input file...')
            print(' ')
            print(' ')
        
            file = reader(my_csv_f)
            for i in file:
                print(i)
                print(' ')
            print(' - [ STEP COMPLETED ] - File Read Completed! ')
            print(' ')
            print(' ')
    except:
        
        print(' ')
        print('##########################################################################################################################################################')
        print('#######################################################################. No such a file found! .##########################################################')
        print('##########################################################################################################################################################')
        print(' ')
        print(' ')
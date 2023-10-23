import random
import time

def generate_random_line(): #function which generates and returns 3 random integers and their sum in an array 
    line=[]  #intializing empty array
    total=0
    for i in range(0,3):
        line.append(random.randint(0,99)) #using random module to generate 3 integers between 0 and 99
        total+=line[i] #calculating the total sum of the 3 numbers in the same loop
    line.append(total)
    return line

def generate_input_files(no_of_lines): #function to generate file names i.e arr20.txt and store them in an array
    files_name=[]
    for i in no_of_lines:
        files_name.append("arr"+str(i)+".txt") #this line is converting the integer into a string and concatinating it with arr and .txt 
    return files_name

def generate_filled_files(file_name,no_of_lines): #function which fills the text files with random numbers and their sum. 
    file=open(file_name,"w+") #It also returns an array which contains only the sums of the generated numbers of all the lines 
    total_arr=[]
    for i in range (0,no_of_lines):
        line=generate_random_line()
        str_line= " ".join(map(str,line))+"\n" #converting the array received into string to paste it in the text file
        file.write(str_line)
        total_arr.append(line[-1])
    return total_arr

def insertion_sort(arr): #actual insertion sort implementation
    index_arr=[] 
    for i in range(0,len(arr)): #initializing an index array so we can sort the indices of the total_array and keep track of the lines
        index_arr.append(i)
    for i in range(1,len(arr)):
        key=arr[i]
        index_key=index_arr[i]
        j=i-1
        while j>-1 and arr[j]>=key:
            arr[j+1]=arr[j]
            index_arr[j+1]=index_arr[j] #shifting the values of the index array as the sum array sorts itself
            j=j-1
        arr[j+1]=key
        index_arr[j+1]=index_key
    return index_arr #finally we have an array which has indices of the actual input text file on how it should be sorted
        
def generate_output_files(sorted_index,input_file_name,no_of_lines,time): #function generates output files
    output_file_name="arrIS_O_"+str(no_of_lines)+".txt" #generates name of the output file
    output_file=open(output_file_name,"w+")
    input_file=open(input_file_name,"r")
    input_file_lines=input_file.readlines() #this variable has all the lines of the input file as a a string array
    for i in sorted_index:
        output_file.write(input_file_lines[i]) # in the output file,we are pasting lines of the input files according to the line numbers 
    output_file.write(str(time)) #adding the time to the output file


no_of_lines=[20,100,2000,6000]    #defining all different lines required in the project
files=generate_input_files(no_of_lines) #calling the function to generate file names i.e arr20.txt
for i in range(0,4):
    arr=generate_filled_files(files[i],no_of_lines[i]) #calling the function to fill the specified file names with 3 random integers b/w 0 and 99 and their total in the end
    start_time=time.perf_counter() #starting time counter to calculate the time required for our function to run
    sorted_index=insertion_sort(arr) #function which sorts the array and returns the indices of the sorted lines
    end_time=time.perf_counter()  #ending the time counter
    generate_output_files(sorted_index,files[i],no_of_lines[i],end_time-start_time) #calling the function to generate the output files

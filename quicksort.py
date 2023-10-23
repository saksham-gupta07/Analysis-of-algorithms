import time


def quick_sort(arr, p, r): #implementation of quick sort
    if p < r: #p is the index of the first element, r is the index of the last element
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)

def partition(arr, p, r): 
    x = arr[r]  # Choosing the pivot as the last element
    i = p - 1  # Initializing the index of the smaller element

    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] #swapping the elements which are smaller than pivot

    arr[i + 1], arr[r] = arr[r], arr[i + 1] 
    return i + 1
        
def generate_output_files(sorted_array,file_array,no_of_lines,time):
    output_file_name="arrQK_O_"+str(no_of_lines)+".txt" #generating the output file name
    output_file=open(output_file_name,"w+")
    for element in sorted_array:
        for line_array in file_array:
            if line_array[-1]==element:
                str_line= " ".join(map(str,line_array))+"\n" #converting int array into string 
                output_file.write(str_line)
                file_array.remove(line_array) #removing the already copied line from the 2-d integer array
    output_file.write(str(time)) #pasting the time it took to run
        


no_of_lines=[20,100,2000,6000]  
for num in no_of_lines: #num has the value of the no_of_lines array i.e. 20
    file_array=[] #initalizing an array to store the lines in input text files
    sum_array=[] #initializing an array to store sum of the generated numbers by line
    file_name="arr"+str(num)+".txt" #stores the name of the input files generated in insertion sort i.e. arr20.txt
    file=open(file_name,"r") 
    lines=file.readlines() # variable stores the lines of the input file as a string array
    for line in lines:
        int_arr = [int(n) for n in line.split()] #converting the string line into an integer array
        file_array.append(int_arr) # A 2 dimensional array storing the values in each lines as integer array
        sum_array.append(int_arr[-1]) #A 1 dimensional array storing the sum values of each line 
    start_time=time.perf_counter()
    quick_sort(sum_array,0,num-1)  #performing quick sort on the total of each line array
    end_time=time.perf_counter()
    generate_output_files(sum_array,file_array,num,end_time-start_time)


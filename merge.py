import time 

def merge_sort(arr): #merge sort implementation
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2     # Spliting the array into two halves
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)     # Recursively sorting both halves
    right = merge_sort(right)

    return merge(left, right)    # Merging the sorted halves

def merge(left, right):
    merged = []
    left_index =0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])  # Adding any remaining elements from both lists
    merged.extend(right[right_index:])
    
    return merged
        
def generate_output_files(sorted_array,file_array,no_of_lines,time):
    output_file_name="arrMR_O_"+str(no_of_lines)+".txt" #generating the output file name
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
    sorted_array=merge_sort(sum_array) #performing merge sort on the total of each line array
    end_time=time.perf_counter()
    generate_output_files(sorted_array,file_array,num,end_time-start_time)

        


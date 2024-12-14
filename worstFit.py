def worst_fit(block_size, process_size):
    number_blocks = len(block_size)
    number_processes = len(process_size)
    
    # Initialize allocation array
    allocation = [-1] * number_processes

    # iterate through each process
    for i in range(number_processes):
        max_index = -1

        # Find  worst fit block
        for j in range(number_blocks):
            if block_size[j] >= process_size[i]:
                if max_index == -1 or block_size[j] > block_size[max_index]:
                    max_index = j

        # If a worst fit block was found, allocate it
        if max_index != -1:
            allocation[i] = max_index
            block_size[max_index] -= process_size[i]

    # output the  results
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(number_processes):
        print(f"{i + 1}\t\t{process_size[i]}\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated (Starvation)")


# exmple input & calling the function
block_size = [100, 500, 200, 300, 600] # remain 288 size in block no 5 
process_size = [312, 417, 289, 426] 

worst_fit(block_size, process_size)

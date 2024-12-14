def worst_fit(block_size, process_size):
    number_blocks = len(block_size)
    number_processes = len(process_size)


    #initialize alloc array
   allocation = [-1] * number_processes 
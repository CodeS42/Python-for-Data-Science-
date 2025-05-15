import os
import time

def ft_tqdm(lst: range) -> None:
    print_block = round(int(lst[-1]) / 24)
    print_percent = round(int(lst[-1]) / 100)
    step_percent = print_percent
    count = 0
    term_columns = os.get_terminal_size().columns
    start = time.time()
    
    for elem in lst:
        elapsed_time = time.time() - start
        if elapsed_time > 0:
            it_per_sec = round(int(elem + 1) / elapsed_time, 2)
        else:
            it_per_sec = 0
        it_per_sec = str(it_per_sec) + "it/s"
        
        # nb_characters = len(lst) + + len(it_per_sec)
        # max_loading_bar = term_columns - 
        count += 1
        if count == print_block:
            print(int(elem) + 1)
            # f"100%|████████████████████████| 333/333 [00:01<00:00, 171.42it/s]"
            # f"{percent}%|{loading_bar}| {passed_elements}/{total_elements} [00:01<00:00, 171.42it/s]"
            # print(f"\r{str(print_percent)}%|", end="", flush=True)
            # print_percent += step_percent
            print('\u2588', end="", flush=True)
            count = 0
        if count == 333:
            print(333)
        yield lst
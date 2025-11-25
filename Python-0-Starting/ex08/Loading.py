from shutil import get_terminal_size
from time import time

def ft_tqdm(lst: range) -> None:
    nb_elements = len(lst)
    terminal_width = get_terminal_size().columns
    done = 0
    time_start = time()
    last_print = 0

    for elem in lst:
        done += 1
        if elem == 0 or elem == nb_elements - 1 or (time() - last_print) >= 0.1:
            percent = int((done / nb_elements) * 100)
            elapsed = time() - time_start
            it_per_sec = done / elapsed
            time_left = (nb_elements - done) / it_per_sec

            hours = int(elapsed // 3600)
            minutes = int((elapsed % 3600) // 60)
            seconds = int(elapsed % 60)
            if hours >= 1:
                str_elapsed = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            else:
                str_elapsed = f"{minutes:02d}:{seconds:02d}"

            hours = int(time_left // 3600)
            minutes = int((time_left % 3600) // 60)
            seconds = int(time_left % 60)
            if hours >= 1:
                str_time_left = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            else:
                str_time_left = f"{minutes:02d}:{seconds:02d}"

            if percent < 100:
                str_percent = f"{percent: 3d}%"
            else:
                str_percent = f"{percent}%"

            str_it_per_sec = f"{it_per_sec:.2f}it/s"
            str_done = f"{done}/{nb_elements}"

            size_loading_bar = terminal_width - len(str_percent) - len(str_elapsed) - len(str_it_per_sec) - len(str_done) - len(str_time_left) - 9
            nb_blocks = int((size_loading_bar * done) / nb_elements)
            
            loading_bar = '█' * nb_blocks + ' ' * (size_loading_bar - nb_blocks)
            line = f"{str_percent}|{loading_bar}| {str_done} [{str_elapsed}<{str_time_left}, {str_it_per_sec}]"
            print('\r' + line, end='')
            last_print = time()
        yield elem

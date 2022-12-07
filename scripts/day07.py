with open("inputs/input07.txt", "r") as input:
    input = input.read().rstrip().split('$ ')
    input = [x.rstrip().split('\n') for x in input[2:]]


dirs_w_content = {}
current_dir = '.'
for io in input:
    command = io[0]
    if command.startswith('cd '):
        cd_path = command[3:]
        if cd_path == '..':
            current_dir = '/'.join(current_dir.split('/')[:-1])
        else:
            current_dir += f'/{cd_path}'
    else:
        file_sizes = [int(output.split(' ')[0]) for output in io[1:] if not output.startswith("dir")]
        dirs_w_content[current_dir] = sum(file_sizes)


all_dirs = list(dirs_w_content.keys())
dir_sizes = {}
for dir, content in dirs_w_content.items():
    subdirs = [d for d in all_dirs if d.startswith(dir)]
    dir_sizes[dir] = sum([dirs_w_content[subdir] for subdir in subdirs])


# part 1
sizes = dir_sizes.values()
print(sum([dir_size for dir_size in sizes if dir_size <= 100000]))

# part 2
print(min([size for size in sizes if (size + 70000000 - max(sizes) >= 30000000)]))

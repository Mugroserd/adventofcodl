def check_range(first_elf_beg, first_elf_end, second_elf_beg, second_elf_end) -> int:
    if first_elf_end - first_elf_beg >= second_elf_end - second_elf_beg:
        for a in range(first_elf_beg, first_elf_end + 1):
            if a in range(second_elf_beg, second_elf_end + 1):
                return True
    elif second_elf_end - second_elf_beg >= first_elf_end - first_elf_beg:
        for a in range(second_elf_beg, second_elf_end + 1):
            if a in range(first_elf_beg, first_elf_end + 1):
                return True
    else:
        return False

score = 0
with open("input") as f:
    count = 0
    for line in f:
        assignments  = line[:-1]
        first_elf, second_elf = assignments.split(',')
        first_elf_beg, first_elf_end = [int(a) for a in first_elf.split('-')]
        second_elf_beg, second_elf_end = [int(a) for a in second_elf.split('-')]
        if check_range(first_elf_beg, first_elf_end, second_elf_beg, second_elf_end):
            count += 1
print(count)
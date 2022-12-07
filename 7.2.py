class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.files = []
        self.directories = []
        self.parent = parent
        self.size = 0

    def find_closest_size_to_min(self, cur_min, val):
        if cur_min > self.size and self.size >= val:
            cur_min = self.size
            print(cur_min)  # а потом смотрим глазками ищем минимальный
        for directory in self.directories:
            directory.find_closest_size_to_min(cur_min, val)

    def add_file(self, size, name):
        self.files.append(File(size, name))

    def add_directory(self, name):
        self.directories.append(Directory(name=name, parent=self))

    def calculate_size(self):
        self.size = 0
        for directory in self.directories:
            self.size += directory.calculate_size()
        for file in self.files:
            self.size += file.size
        return self.size

    def find_directory(self, name):
        for directory in self.directories:
            if name == directory.name:
                return directory
        return None


class File:
    def __init__(self, size: int, name: str):
        self.size = size
        self.name = name


directories = []
with open("input") as f:
    current_dir = Directory('/')
    directories.append(current_dir)
    f.readline()
    for line in f:
        line = line[:-1]
        if line[:4] == '$ cd':
            if line[5:7] == '..':
                current_dir = current_dir.parent
            else:
                dir_name = line[5:]
                if current_dir.find_directory(dir_name) is None:
                    current_dir = Directory(dir_name, parent=current_dir)
                    directories.append(current_dir)
                else:
                    current_dir = current_dir.find_directory(dir_name)
        elif line[:4] == '$ ls':
            pass
        else:
            if line[:3] == 'dir':
                current_dir.add_directory(line[4:])
            else:
                size, name = [a for a in line.split(' ')]
                current_dir.add_file(int(size), name)

required_size = -70000000 + directories[0].calculate_size() + 30000000
print(required_size)
directories[0].find_closest_size_to_min(70000000, required_size)

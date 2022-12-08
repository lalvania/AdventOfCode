
class Obj:
    def __init__(self, name, root, type="dir", level=0, size=0, parent=None):
        self.name = name
        self.root = root
        self.type = type
        self.size = size
        self.level = level
        self.children: dict = {}
        self.parent = parent

    def __eq__(self, other):
        if isinstance(other, Obj):
            return self.root == other.root
        if isinstance(other, str):
            return self.root == other

    def __str__(self):
        ret = self.root + "\t" + str(self.size) + "\n"
        for child in self.children.values():
            ret += child.__str__()
        return ret


def set_sizes(root: Obj) -> int:
    if root.type == "file":
        return root.size
    for path, child in root.children.items():
        if child.type == "file":
            root.size += child.size
        else:
            root.size += set_sizes(child)
    return root.size


def get_dict(root: Obj) -> dict:
    d = {}

    def recurse(r: Obj):
        d[r.root] = r.size
        for path, child in r.children.items():
            if child.type == "file":
                d[child.root] = child.size
            else:
                recurse(child)
    recurse(root)
    return d


def read(file_path: str) -> Obj:
    file = open(file_path, "r")
    root = Obj(root="/", name="/")
    current: Obj = None

    for l in file.readlines():
        line = l.strip()
        if line == "$ cd /":
            current = root
        elif line.startswith("$ cd .."):
            current = current.parent
        elif line.startswith("$ cd "):
            name = line.split(" ")[2]
            new_root = current.root + name + "/"
            if new_root not in current.children:
                new_node = Obj(
                    name=name,
                    root=new_root,
                    type="dir",
                    level=current.level + 1,
                    parent=current
                )
                current.children[new_root] = new_node
            current = current.children[new_root]
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir "):
            name = line.split(" ")[1]
            new_root = current.root + name + "/"
            if new_root not in current.children:
                new_node = Obj(
                    name=name,
                    root=new_root,
                    type="dir",
                    level=current.level + 1,
                    parent=current
                )
                current.children[new_root] = new_node
        elif line[0].isdigit():
            name = line.split(" ")[1]
            new_root = current.root + name
            if new_root not in current.children:
                new_node = Obj(
                    name=name,
                    root=new_root,
                    type="file",
                    level=current.level + 1,
                    parent=current,
                    size=int(line.split(" ")[0])
                )
                current.children[new_root] = new_node
    set_sizes(root)
    return root


def part1(file_path: str, max_size: int) -> int:
    root = read(file_path=file_path)
    dirs = get_dict(root)
    return sum([v for k, v in dirs.items() if v < max_size and k[-1] == "/"])


def part2(file_path:str, total_disk_size: int, target_unused_space) -> int:
    root = read(file_path=file_path)
    dirs = get_dict(root)
    used_space = total_disk_size - dirs["/"]
    i = []
    for k, v in dirs.items():
        if k[-1] == "/" and v+used_space > target_unused_space:
            space_freed = v + used_space
            i.append(v)
    i.sort()
    return i[0]


if __name__ == '__main__':
    # test
    # print(part1("resources/test", 100000))
    print(part2("resources/test", 70000000, 30000000))

    # input
    # print(part1("resources/input", 100000))
    print(part2("resources/input", 70000000, 30000000))

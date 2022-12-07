from pprint import pprint as p


aoc_7 = open("./AOC_door_7.txt", "r").read().splitlines()
aoc_7 = aoc_7  # [1:]


lines = aoc_7
fs = {("/",): 0}
path = []
for line in lines:
    match line.split():
        case ["$", "ls"]:
            # nothing to be done
            pass
        case ["$", "cd", ".."]:
            # cwd is parent
            path = path[:-1]
        case ["$", "cd", directory]:
            # cwd is one deeper now
            path += [directory]
        case ["dir", directory]:
            # if the ls reveals a dir, we set a default size of 0
            fs.setdefault(tuple(path + [directory]), 0)
        case [size, filename]:
            # for files, we add each one to the cwd and all parent directories
            for i in range(1, len(path) + 1):
                fs[tuple(path[:i])] += int(size)


print("p1", sum([x for x in fs.values() if x <= 100000]))

print("p1")
fs_size = 70_000_000
space_needed = 30_000_000
unused = fs_size - fs[("/",)]
size_to_del = space_needed - unused
big_enough_dirs = {k: v for (k, v) in fs.items() if v >= size_to_del}
print(" + possible folders ")
for k, v in big_enough_dirs.items():
    print("  ∟", end="")
    print("/".join(k), end="")
    print(": ", v)
print("smallest: ", min(big_enough_dirs.values()))


## trials with stuff
##

# @dataclass
# class FSobject:
#     name: str
#     size: int
#     content: list


# f = FSobject("/", 124, content=[FSobject("dir1", 1, content=[FSobject("f1", 123, [])])])

# print(f)


# def walk_dirs(structure, position, mode="mkdir"):
#     pass


# def walk(node):
#     for key, item in node.items():
#         if item is a collection:
#             walk(item)
#         else:
#             It is a leaf, do your thing

## my 1st trial
##


# def depth(path_str):
#     return len(path_str.split("/")) - 1


# def cp_str(cwd):
#     """make string for cwd"""
#     return "/".join(cwd)


# aoc_7 = open("./AOC_door_7.txt", "r").read().splitlines()
# aoc_7 = aoc_7  # [1:]

# structure = dict(list())
# cwd = []  # skipping forst live above
# ls_mode = False
# current_path = "/"

# for ln, line in enumerate(aoc_7):
#     if ls_mode:
#         if current_path not in structure:
#             structure[current_path] = 0  # {"keys": [], "size": 0}
#         if not line.startswith("$"):
#             if not "dir" in line:
#                 size = int(line.split(" ")[0])
#                 # structure[current_path]["keys"] = line
#                 for i in range(len(cwd) - 1, 0, -1):
#                     parent_path = cp_str(cwd[:i])
#                     structure[parent_path] += size
#                 structure[current_path] += size
#     if line.startswith("$"):
#         ls_mode = False
#         line_contents = line.split(" ")
#         command = line_contents[1]
#         if command == "ls":  ## TODO
#             # print("ls-time")
#             ls_mode = True
#         elif command == "cd":
#             arg_1 = line_contents[2]
#             if arg_1 == "..":
#                 cwd.pop(-1)  # leave the current directory
#             else:
#                 cwd.append(arg_1)  # go into the directory
#             current_path = "/".join(cwd)
#             # print(current_path)

#         # path_str = "/".join(cwd)
#         # structure[path_str] = []
#         # for subline in aoc_7[ln:]:
#         #     if subline.startswith("$"):
#         #         break
#         #     else:
#         #         structure[path_str].append(subline)

#         # print(cwd)

# p(structure)

# a = sum([s for f, s in structure.items() if s >= 100000])

# print(a)


##
## https://www.reddit.com/r/adventofcode/comments/zesk40/2022_day_7_solutions/

# currentPath = []
# folders = {}


# def pathToString(pathList):
#     out = ""
#     if len(pathList) == 1:
#         return "/"
#     for e in pathList:
#         if out == "":
#             out = e
#         elif out[-1] == "/":
#             out += e
#         else:
#             out += "/" + e
#     return out


# for l in lines:
#     if "$ cd .." in l:
#         currentFolder = currentPath.pop()
#         strPath = pathToString(currentPath)
#     elif "$ cd" in l:
#         currentFolder = l.split()[-1]
#         currentPath.append(currentFolder)
#         strPath = pathToString(currentPath)
#         if strPath not in folders.keys():
#             folders[strPath] = 0
#     elif l.split()[0].isdigit():
#         fsize, fname = l.split()
#         for i in range(len(currentPath) - 1, 0, -1):
#             parentPath = pathToString(currentPath[:i])
#             folders[parentPath] += int(fsize)
#         folders[strPath] += int(fsize)
# # part 1
# totalSum = 0
# for f in folders.keys():
#     if folders[f] <= 100000:
#         totalSum += folders[f]
# print("part1: ", totalSum)

# # part 2
# freeMem = 70000000 - folders["/"]
# minSize = freeMem
# for f in folders.keys():
#     if folders[f] + freeMem >= 30000000:
#         if folders[f] < minSize:
#             minSize = folders[f]
# print("Part2: ", minSize)

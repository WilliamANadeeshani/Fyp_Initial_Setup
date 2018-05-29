file_object = open('input', 'r')
file = open('frequent_path', 'w')

with open('input') as f:
    content = f.readlines()

content = [x.strip() for x in content]
out = []
read_path = []
path_frequency = []

for x in content:
    line = x.split()
    if line in read_path:
        for x in path_frequency:
            if x[0] == line[2]:
                x[1] = x[1] + 1

    else:
        read_path.append(line)
        temp = [line[2], 1]
        path_frequency.append(temp)

for x in path_frequency:
    if x[1] >= 5:
        file.write(str(x[0]) + "\n")

import os

f = open(r"./_sidebar.md", 'w')
exclude = set([".git"])
for root, dirs, files in os.walk(r"./"):
    dirs[:] = [d for d in set(dirs) - exclude]
    files[:] = [file for file in files if file.split('.')[1] == 'md' and file[0] != '_']
    if root!="./":
        root=root.split('/')[1]
        s1 = "- **" + root + "**\n"
        f.write(s1)
        print(s1)
        for file in files:
            s2 = "   - [" + file.split('.')[0] + '](' + root+'/'+file + ")\n"
            f.write(s2)
            print(s2)
    else:
        for file in files:
            s2 = "- [" + file.split('.')[0] + ']('+file + ")\n"
            f.write(s2)
            print(s2)
f.close()
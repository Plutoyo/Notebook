import os

f = open(r".\_sidebar.md", 'w')
exclude = set([".git"])
for root, dirs, files in os.walk(r".\\"):
    dirs[:] = [d for d in set(dirs) - exclude]
    files[:] = [f for f in files if f.split('.')[1] == 'md' and f[0] != '_']

    s1 = "- **" + root.split('\\')[-1] + "**\n"
    if root.split('\\')[-1]!="":
        f.write(s1)
        for file in files:
            s2 = "   - [" + file.split('.')[0] + '](' + file + ")\n"
            f.write(s2)
    else:
        for file in files:
            s2 = "- [" + file.split('.')[0] + '](' + file + ")\n"
            f.write(s2)
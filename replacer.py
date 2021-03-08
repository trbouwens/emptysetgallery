import os

files = []
for a in os.listdir("."):
    if ".html" in a:
        files.append(a)
print(files)

print("Paste the text you want TO BE REPLACED here:  (end with a blank newline)")

old = input("")
to_replace = old
while old != "":
    old = input("")
    to_replace += "\n" + old

print("Paste the NEW text you REPLACE OTHER TEXT WITH here (end with a blank newline)")

new = input("")
replace_with = new
while new != "":
    new = input("")
    replace_with += "\n" + new

print(f"Replacing {to_replace} with {replace_with}")

for filename in files:
    data = ""
    with open(f"./{filename}", "r") as f:
        data = f.read()
    data = data.replace(to_replace, replace_with)
    with open(f"./{filename}", "w") as f:
        f.write(data)



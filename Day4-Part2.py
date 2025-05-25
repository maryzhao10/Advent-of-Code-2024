count = 0

lines = []
for i in range(140):
    text = input()
    lines.append(text)

cols = len(text)

for c in range(cols):
    columntext = ""


for i in range(140):
    for c in range(cols):
        if 1 <= i < 139 and 1 <= c < cols-1:

            if lines[i][c] == "A":

                if lines[i-1][c-1]=="M" and lines[i-1][c+1]=="M" and lines[i+1][c-1]=="S" and lines[i+1][c+1]=="S":
                    count = count + 1

                if lines[i-1][c-1]=="S" and lines[i-1][c+1]=="M" and lines[i+1][c-1]=="S" and lines[i+1][c+1]=="M":
                        count = count + 1
            
                if lines[i-1][c-1]=="S" and lines[i-1][c+1]=="S" and lines[i+1][c-1]=="M" and lines[i+1][c+1]=="M":
                        count = count + 1
            
                if lines[i-1][c-1]=="M" and lines[i-1][c+1]=="S" and lines[i+1][c-1]=="M" and lines[i+1][c+1]=="S":
                        count = count + 1
        
print(count)

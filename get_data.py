import os

print("Pulling data")

data = "x,y\n1,2"
with open("data/train.csv", os.O_CREAT) as f:
    f.write(data)

# Exercise 3: Slice list into 3 equal chunks and reverse each chunk

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
count = 1
chunk = []

for index,data in enumerate(sample_list):
    chunk.append(data)
    if(count == 3):        
        count = 0
        print(f"Chunk{count}  : ", chunk)
        chunk = []
    count += 1



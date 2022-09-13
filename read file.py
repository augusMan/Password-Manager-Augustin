

f = open("file.txt", "r")
data = f.read() 
print(data)
stripped_data = data.strip() 
print(stripped_data)
dataList = stripped_data.split("   ") 
print(dataList) 


dataList = ["Rick", "Pie", "Australia", "Lan", "Spaghetti", "Vietnam", "Frank", "Apples", "Germany"]
i = 0
border = "|"
print(f"{border}{'Name' : ^20}{border}{'Food' : ^20}{border}{'Country' : ^20}")
print("--------------------------------------------------------------------")
while i < len(dataList): #repeat until 'i' is larger than the list length
    print(f"{border}{dataList[i] : ^20}{border}{dataList[i+1] : ^20}{border}{dataList[i+2] : ^20}")   
    i += 3
else:
    print("\nAll data has now been displayed\n")

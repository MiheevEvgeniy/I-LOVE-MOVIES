row = "Титаник затонувший во льдах"
search="ну вш"
start=0
end=len(search)
success=False
for i in range(0,len(row)):
    if row[start:end] == search:
        success=True
    start+=1
    end+=1
if success==True:
    print("совпадения есть")
else:
    print("совпадения нет")
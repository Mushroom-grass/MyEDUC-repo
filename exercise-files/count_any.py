def CountStr(str, list):
    count = 0
    for i in list:
        if i == str:
            count += 1
    return count

with open("test.txt", "r") as f:
    data = str.split(f.read())
    input_str = input("please enter any string you want to count: ")
    count_str = CountStr(input_str, data)
    
with open("output_any.txt","w") as f:
    f.write(input_str + ":" + str(count_str))
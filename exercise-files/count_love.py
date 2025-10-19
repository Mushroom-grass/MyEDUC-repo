with open("test.txt", "r") as f:
    data = str.split(f.read())
    # print(data)

    total_str = 0
    count_str = 0
    input_str = "love"
    # print(input_str)
    
    for item in data:
        total_str += 1
        if item == input_str:
            count_str += 1
    
with open("output_love.txt","w") as f:
    f.write("Total words:" + str(total_str) + "\n")
    f.write(input_str + ":" + str(count_str))
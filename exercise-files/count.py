with open("test.txt", "r") as f:
    data = f.readlines()

    total_lines = 0
    romeo_count = 0
    juliet_count = 0
    
    for line in data:
        # print(line)
        total_lines += 1
        if line == "JULIET\n":
            juliet_count += 1
        elif line == "ROMEO\n":
            romeo_count += 1
    # print(total_lines, romeo_count, juliet_count)
    
with open("output.txt","w") as f:
    f.write("Total lines:" + str(total_lines) + "\n")
    f.write("Juliet:" + str(juliet_count) + "\n")
    f.write("Romeo:" + str(romeo_count)) 
    
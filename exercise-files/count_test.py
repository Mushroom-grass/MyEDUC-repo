with open("test.txt", "r") as f:
    data = f.readlines()
    print(data)
    
with open("test.txt","w") as f:
    f.write("这是个测试！")  # 自带文件关闭功能，不需要再写f.close()
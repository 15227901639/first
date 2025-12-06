
def list_operations():                                     #定义函数用以操作列表
    numbers=[23,45,12,67,89,12,56,23,78]                   #创建一个列表，numbers并给定整数
    print("列表长度：{}".format(len(numbers)))               #len取列表长度，再通过print输出
    unique_numbers=list(set(numbers))                      #声明unique_numbers新列表通过set去掉重复元素放入新列表
    print("去重后列表：{}".format(unique_numbers))           #print输出去重之后的列表
    ascending=sorted(unique_numbers)                       #通过sorted函数进行升序排列，该函数可对列表元组字符等进行排序，默认为升序
    descending =sorted(unique_numbers,reverse=True)        #对去重后的进行降序处理
    print("升序排列：{}".format(ascending))                  #输出去重后进行升序排列之后的结果
    even_count= 0                                           #声明变量用来记录偶数的个数
    odd_count= 0                                            #用来计数奇数出现的数量
    for num in unique_numbers:                              #for循环一次便利列表中的元素
        if num%2==0:                                        #判断能否被2整除
            even_count+=1                                   #可以说明是偶数，偶数计数＋1
        else:                                               #不满足
            odd_count+=1                                    #排除法为奇数，奇数计数+1
    print("偶数个数：{}".format(even_count))                  #输出去重后偶数的个数
    print("奇数个数：{}".format(odd_count))                    #输出奇数元素的个数
    print("最大值：{},最小值：{}".format((max(unique_numbers)),min(unique_numbers)))#maxmin两个函数分别取出最大最小值，并且print输出
list_operations()                                           #调用函数，进行列表操作

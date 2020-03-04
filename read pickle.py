import pickle

def compare(list1, list2):
    error = []
    error_index = []
    if len(list1) == len(list2):
        for i in range(0, len(list1)):
    #两个列表对应元素相同，则直接过
            if list1[i] == list2[i]:
                pass
            else:#两个列表对应元素不同，则输出对应的索引
                error.append(abs(list1[i]-list2[i]))
                 # print(i)
                error_index.append(i)
    print(error)
    print(error_index)


with open('chosen.pickle', 'rb') as cfile:
    a_dict1 = pickle.load(cfile)

with open('correct_answer.txt', 'rb') as rfile:
    correct_answer = pickle.load(rfile)


print(len(a_dict1))
print(a_dict1)
print(correct_answer)

diff = correct_answer - a_dict1
print(diff)
def solution(num_list):
    if not num_list or len(num_list) ==1 :
        return num_list
    if num_list[-1]>num_list[-2]:
        num_list.append(num_list[-1]-num_list[-2])
    else:
        num_list.append(num_list[-1]*2)
    return num_list
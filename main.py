import copy

#function to get sample data of only specified parameters
def get_sub_sample(parameter_indicies,sample_data):
    sub_sample_data=[]
    for sample in sample_data:
        temp=[]
        for i in parameter_indicies:
            temp.append(sample[i])
        sub_sample_data.append(temp)
    return sub_sample_data

#function to get dictionary of a table given a sample data
def get_sub_dict(sub_table,sub_sample):
    dict={}
    for i in sub_table:
        dict[tuple(i)]=0
    for i in sub_sample:
        dict[tuple(i)]+=1
    return dict

#function to get permutated table by parameter list given
def get_combined_table(param_list):
    param_list=param_list[::-1]
    res=[""]
    for li in param_list:
        new=[]
        for var in li:
            for var2 in res:
                temp=var+' '+var2
                new.append(temp)
        res=copy.deepcopy(new)
    table=[]
    for var in res:
        table.append(var.split(' ')[:len(var.split(' '))-1])
    return table

#function to get dependent variables indicies
def get_row(network,col_index):
    temp=[]
    for i in range(len(network)):
        if(network[i][col_index]=='0'):
            continue
        else:
            temp.append(i)
    return temp

#function to fetch count of a sample from corresponding dictionary
def get_count(sub_dict_num,curr_row):
    return sub_dict_num[tuple(curr_row)]

def util(network,col_index,param_list):
    #indicies of all rows on which current variable is dependent
    row_index_list=get_row(network,col_index)
    #variables of only current parameter and its dependent parameters
    sub_param=[]
    #adding current parameter variables to list
    sub_param.append(param_list[col_index])
    for i in row_index_list:
        sub_param.append(param_list[i])
    #adding current parameter index to list
    row_index_list.insert(0,col_index)
    
    return row_index_list,sub_param
    
#parameters and variables input
num_of_parameters=int (input())
param_list=[]
for i in range(num_of_parameters):
    li=input().split(', ')
    param_list.append(li)

#network input
network=[]
for i in range(num_of_parameters):
    li=input().split(' ')
    network.append(li)


#number of samples input
num_of_samples=int(input())
sample_data=[]

#taking input of sample_data
for i in range(num_of_samples):
    li=input().split(',')
    sample_data.append(li)



for col_index in range(num_of_parameters):
    

    row_index_list,sub_param=util(network,col_index,param_list)
    
    #for numerator part
    sub_table_num=get_combined_table(sub_param)
    sub_sample_data_num=get_sub_sample(row_index_list,sample_data)
    sub_dict_num=get_sub_dict(sub_table_num,sub_sample_data_num)
    
    #for denominator part
    sub_table_den=get_combined_table(sub_param[1:])
    sub_sample_data_den=get_sub_sample(row_index_list[1:],sample_data)
    sub_dict_den=get_sub_dict(sub_table_den,sub_sample_data_den)
    
    #calculating and printing
    curr_line=''
    for curr_row in sub_table_num:
        num=get_count(sub_dict_num,curr_row)
        den=get_count(sub_dict_den,curr_row[1:])
        if den==0:
            curr_line+=str(format((0),'.4f'))+' '
        else:
            curr_line+=str(format((num/den),'.4f'))+' '
    print(curr_line)








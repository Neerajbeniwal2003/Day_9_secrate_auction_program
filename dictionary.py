#syntax
dictionary={"key":"value"}


new_dic={"name":"neeraj","age":21}
print(new_dic)


#get an element from the dictionary
print(new_dic["name"])


#to add and element in the dictionary
new_dic["location"] = "delhi,india"
print(new_dic)



#to edit dictionary elements
new_dic["name"]="ajeet" #where the name is placed if it is in the dictinary then it will chage the value of element in the dictionary
# print(new_dic)          #and if the elment not in the dictionary then it will be added to the right side of the dictionary


#empty dictionary
empty_dic={} 
print(f"empty dictionary:{empty_dic}")
#you can use it to clear out the existing dictionary in programs
# new_dic={}
# print(f"cleared the new_dic dictionary:{new_dic}")



#loop through the dictionary
for key in new_dic:
    print(key)
    print(new_dic[key])
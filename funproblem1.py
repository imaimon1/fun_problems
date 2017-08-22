#print all a,b,c,d such that a^3 +b^3 = c^3 + d^3 and 0<a,b,c,d < n
def function(start,upto):
	
	out_list=[]
	check_list = []
	for i in range(start,upto+1):
		for j in range(start,i+1):
			check_list.append((i,j,i**3+j**3))
	
	new_list = sort_by_element(check_list,2)
	
	i=0
	while i < len(new_list):
		j=i
	
		while new_list[i][2] == new_list[j][2]:
			first = new_list[i][0]
			second = new_list[i][1] 
			third = new_list[j][0]
			fourth = new_list[j][1]
			out = new_list[i][2]
# commented part gives all entries most of which are just "isomorphic" to each other
# isomorphic: different versions of the same thing. 
#			if first == second == third == fourth:
#				out_list.append((first,first,first,first,out))
#			
#			elif first == second and third == fourth:
#				out_list.append((first,first,third,third,out))
#				out_list.append((third,third,first,first,out))
#			elif first == second:
#				combinations(out_list,third,fourth,first,first,out)
#			elif third == fourth: 
#				combinations(out_list,first,second,third,third,out)				
#			elif i==j:
#				out_list.append((first,second,third,fourth,out))
#				out_list.append((first,second,fourth,third,out))
#				out_list.append((second,first,third,fourth,out))
#				out_list.append((second,first,fourth,third,out))
#			else:	
#				combinations(out_list,first,second,third,fourth,out)
#				combinations(out_list,first,second,fourth,third,out)
# all interesting entries
			if j != i:
#				out_list.append(out)			
				out_list.append((first,second,third,fourth,out))
			j+=1
				
			if not j < len(new_list):
				break
		
		i+=1
	return out_list
	
def easier_function(start,upto):
#nontrivial solutions for trivial just change for loops
	result_dict = {}
	out = []

	for i in range(start,upto+1):
		for j in range(start,i+1):
			result_dict[i**3+j**3] = []

	for i in range(start,upto+1):
		for j in range(start,i+1):
			result_dict[i**3+j**3].append((i,j))
			
	for key in result_dict.keys():
		for i in range(0,len(result_dict[key])):
			for j in range(0,i):
					out.append((result_dict[key][j],result_dict[key][i]))
			
	return out		
			
def combinations(list,a,b,c,d,out):
	list.append((a,b,c,d,out))
	list.append((b,a,c,d,out))
	list.append((c,d,a,b,out))
	list.append((c,d,b,a,out))
		
#		
def sort_by_element(list,a):
	if len(list)==1:
		return list
	
	
	first_list = sort_by_element(list[:int(len(list)/2)],a)
	second_list = sort_by_element(list[int(len(list)/2):],a)
	
	out_list =[]
	i,j=0,0
	len(second_list)
	while len(out_list)<(len(first_list)+len(second_list)):
		if i < len(first_list) and j < len(second_list):
			if first_list[i][a] < second_list[j][a]:  
				out_list.append(first_list[i])
				i += 1
			else:
				out_list.append(second_list[j])
				j += 1
		elif i < len(first_list):
			out_list.append(first_list[i])		
			i+=1
		elif j < len(second_list):
			out_list.append(second_list[j])
			j+=1
	return out_list
print easier_function(1,100)
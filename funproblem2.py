#find all permutations of a list within another list O(a+b) time 
def function(large_list,small_list):
	large_len=len(large_list)
	small_len=len(small_list)
	dict_allow = {}
	dict_need = {}
	out = [] 
	
	
	for a in small_list:
		dict_allow[a] = 1
		dict_need[a] = 0

	for b in large_list:
		dict_allow[b] = 0
		
	for a in small_list: 
		dict_need [a] += 1
		
	checks = len(dict_need.keys())

	for i in range(0,large_len):
		
		if small_len <= i:
			if dict_allow[large_list[i-small_len]] = 1:
				dict_need[large_list[i-small_len]] += 1 
			if dict_need[large_list[i-small_len]] == 0:
				checks -= 1
			if dict_need[large_list[i-small_len]] == 1:
				checks += 1
				
		if dict_allow[large_list[i]] = 1:
			if large_list[i] in need:
				dict_need[large_list[i]] -= 1
			if dict_need[large_list[i]] == 0:
				checks -= 1
			if dict_need[large_list[i]] == -1:
				checks +=1
		if checks == 0:
			out.append((i,i+small_len))
#checks if two strings are permutations
def check_permutation(first, second):
	if len(first) != len(second):
		return false
	
	dict1 = {}
	dict2 = {}
	
	for a in first:
		dict1[a] = 0 
		
	for a in first: 
		dict1[a] += 1
		
	for b in second:
		dict1[b] = 0 
		
	for b in second: 
		dict1[b] += 1
	
	for a in dict1.keys:
		if dict1[a] != dict2[a]:
			return false
	return true
	
	
	
	
	
	
	
	
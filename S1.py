# Uses recursion to solve problem 1 from the senior scottish maths challenge
# By Archie Maclean

from copy import deepcopy

all_lockers = []

def print_locker_list(lockers):
	for n in range(len(lockers)):
		for m in range(n):
			if (n-m)%2 == 1 and lockers[n] == lockers[m]:
				return
	print(', '.join(lockers))
	all_lockers.append(deepcopy(lockers))

def print_locker(lockers):
	if len(lockers) == 10:
		print_locker_list(lockers)
		return
	for val in ["red","green","blue"]:
		lockers.append(val)
		print_locker(lockers)
		lockers.pop()

print("All locker combinations:\n")
print_locker([])
print("\nDone\nAll combination types:\n")

locker_maps = []


# Print locker combination types
for lockers in all_lockers:
	first_val = lockers[0]
	second_val = lockers[1]
	string = ""
	for l in lockers:
		if l == first_val: string+="a"
		elif l == second_val: string+="b"
		else: string+="c"
	if string not in locker_maps: locker_maps.append(string)

locker_maps.sort()
print('\n'.join(locker_maps))

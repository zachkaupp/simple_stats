f = open("data/input.txt", "r")
w = open("data/output.txt", "w")

input = f.read().split()
input = [float(x) for x in input]
input.sort()
input_str_array = [str(x) for x in input]
input_str = ""
for x in input_str_array:
	input_str += x + " "
frequency_array = []
frequency_array.append([input[0],1])
for i,j in enumerate(input):
	if i != 0:
		if input[i-1] == j:
			x = frequency_array.pop()
			x[-1] += 1 
			frequency_array.append(x)
		else:
			frequency_array.append([j,1])
frequency_array_str = [str(x) for x in frequency_array]
frequency_str = ""
for x in frequency_array_str:
	frequency_str += x + " "





#no dependency calculations

def find_median(x):
	if len(x)%2 != 0:
		return x[int(((len(x)+1)/2)-1)]
	else:
		return (x[int((len(x)/2)-1)] + x[int(len(x)/2)])/2

def find_mean(x):
	return sum(x)/len(x)

#dependent calculations

def find_q1(x):
	if len(x)%2 != 0:
		i = x[:int((len(x)+1)/2)-1]
	else:
		i = x[:int(len(x)/2)]
	return find_median(i)

def find_q3(x):
	if len(x)%2 != 0:
		i = x[int((len(x)+1)/2):]
	else:
		i = x[int((len(x)/2)):]
	return find_median(i)

def find_sdev(x):
	i = find_mean(x)
	j = [abs(i-y) for y in x]
	return find_mean(j)







#print summary
print("\nsummary:\n") #5 number summary
print("minimum: " + str(input[0]))
print("q1: " + str(find_q1(input)))
print("median: " + str(find_median(input)))
print("q3: " + str(find_q3(input)))
print("maximum: " + str(input[len(input)-1]))

#important things not included in 5 number summary
print("\nmean: " + str(find_mean(input)))
print("standard deviation: " + str(find_sdev(input))) 
print("interquartile range: " + str(find_q3(input)-find_q1(input)))

#extras
print("\ninput count: " + str(len(input)))
print("summation: " + str(sum(input)))


w.write(input_str + "\n\nfrequencies:\n\n" + frequency_str)

f.close()
w.close()
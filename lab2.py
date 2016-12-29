def min(arr):		#минимальное значение
	minimal =arr[0];
	for i,el in enumerate(arr):
		if el<minimal:
			minimal=el
	return minimal

def average(arr):		#среднее значение массива
	summ=0
	for i,el in enumerate(arr):
		summ=summ+el;
	return (summ/(i+1))

###########################	

def reverse(string): 	#Переворот строки
	i=0
	string2=''
	for ch in range(len(string)):
		cnt=len(string)-i-1
		string2=string2+string[cnt]
		i=i+1
	print (string2)

###############################

def childrens(emps):		#работа со словарями
	for i,el in enumerate(emps):
		emp=el['children']
		for i,child in enumerate(emp):
			if child['age']>18:
				print (el['name'])


arr=[8,2,4,5,1,9]
print (min(arr))
print (average(arr))
reverse("Hello, world!")

ivan = {
	"name": "ivan",
	"age": 34,
	"children": [{
		"name": "vasja",
		"age": 12,
   }, {
       "name": "petja",
       "age": 10,
   }],
}
darja = {
   "name": "darja",
   "age": 41,
   "children": [{
       "name": "kirill",
       "age": 21,
   }, {
       "name": "pavel",
       "age": 15,
   }],
}
emps = [ivan, darja]
childrens(emps)
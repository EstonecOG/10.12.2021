from random import*

def find_word(Capitals:dict)->str:
	a=input("Введите столицу или город на английском >>> ")
	for key, value in Capitals.items():
		if a.title()==value:
			ans=( a.title()+" / "+key )
			break
		elif a.title()==key:
			ans=( a.title()+" / "+value )
			break
		else:
			ans="See sõna ei olema"
	return ans,a

def add_word(Capitals:dict, a:str)->dict:
	b=input("Напишите значение слова")
	Capitals.update({a.title():b.title()})
	return Capitals

def change_smth(Capitals:dict)->dict:
	a=input("Напишите слово, значение которого вы хотите изменить")
	if a not in Capitals.keys():
		print("Этого слова нет в словаре")
	else:
		c=input("Введите новое значение")
		Capitals.update({a.title():c.title()})
	return Capitals

def testingknoledge(Capitals:dict)->float:
	result=0
	country=list(Capitals)
	nocount={} 
	with open("Cap.txt") as f:
		for i in f:
			v,k=i.strip().split("-")
			nocount[k.strip()]=v.strip()
	capitals=list(nocount)
	b=input("Хотите пройти тест по странам или столицам? 1-Столицы (10 Вопросов), 2-Страны (10 Вопросов), 3-Страны и столицы (15 Вопросов)")
	if b=="1":
		a=0
		for i in range (1,11): 
			word=choice(country)
			print()
			ans=input(str(i)+". Введите "+word+" столицу >>> ")
			realans=Capitals.get(word)
			if ans.title()==realans:
				print("Верно!")
				a+=1
			else:
				print("Неверно!")
		result=a*100/10
	elif b=="2":
		a=0
		for i in range (1,11):
			word=choice(capitals)
			ans=input(str(i)+". Введите какая столица этой страны "+word+" >>> ")
			realans=findkey(word,Capitals)
			if ans.title()==realans:
				print("Верно!")
				a+=1
			else:
				print("Неверно!")
		result=a*100/10
	elif b=="3":
		country.extend(capitals)
		a=0
		for i in range (1,16):
			word=choice(country)
			for key, value in Capitals.items():
				if word==value:
					realans=key
					ans=input(str(i)+"Введите какой страны эта столица "+word+" >>> ")
					break
				elif word==key:
					realans=value
					ans=input(str(i)+". Введите "+word+" столица >>> ")
					break
			if ans.title()==realans:
				print("Верно!")
				a+=1
			else:
				print("Неверно!")
		result=a*100/15
	else:
		print("Неверная функция")
	return result

def findkey(val:str,Capitals:dict)->str:
	for key, value in Capitals.items():
		if val == value:
			return key
	return "Нету"
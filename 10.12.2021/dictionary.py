from modul import* 
Capitals={}
with open("Cap.txt","r") as f:
	for i in f:
		k,v=i.strip().split("-")
		Capitals[k.strip()]=v.strip()

while True:
	c=input("Искать слово в словаре - 1, Значение слова - 2, Тест - 3, Выход - 4")
	if c=="1":
		ans,a=find_word(Capitals)
		print(ans)
		if ans=="Слова нету":
			b=input("Хотите найти слово в словаре?, 1-jah 2-ei >>> ")
			if b=="1":
				Capitals=add_word(Capitals,a)
			else:
				pass
		else:
			pass
	elif c=="2":
		Capitals=change_smth(Capitals)
	elif c=="3":
		result=testingknoledge(Capitals)
		print("Ваш результат - "+str(result)+"%")
	elif c=="4":
		with open("Cap.txt", "w") as f:
			for key, value in Capitals.items():
				f.write(key+"-"+value+"\n")
		break
	else:
		print("Этой функции нету)
		
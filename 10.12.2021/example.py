from gtts import gTTS
import os
mytext="Столица и страна"
language="et"
myobj=gTTS(text=mytext, lang=language, slow=False)
myobj.save("mpg 321 welcome.mp3")
os.system("welcome.mp3")
Capitals = dict() #2
Capitals['Russia'] = 'Moscow'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'
Countries = ['Russia', 'France', 'USA', 'Russia']
for country in Countries:
	if country in Capitals:
		print('Столица страны ' + country + ': ' + Capitals[country])
	else:
		print('В базе нет страны c названием ' + country)

dictionary = {'персона': 'человек','марафон': 'гонка бегунов длиной около 26 миль','противостоять': 'оставаться сильным, несмотря на давление','бежать': 'двигаться со скоростью'}
print(dictionary['марафон'])
for key, value in dictionary.items():
	print(key, value)


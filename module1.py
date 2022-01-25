def lisa_sõna(Capitals:dict, a:str)->dict:
	"""Lisama sõna sõnavarasse
	"""
	a=input("Siseta sõna tähendus >>> ") #просим ввести значение слова, мы знаем ключ из прошлой функции по поиску
	Capitals.update({a.title():b.title()}) #добавляем в словарь
	return Capitals

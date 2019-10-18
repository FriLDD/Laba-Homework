#(4 балла, Uber) Вы работаете в компании, которая разрабатывает новый 
#компилятор для языка Си. Вам поручили реализовать проверку синтаксиса 
#программ. Вы решили начать с проверки расстановки скобок. Напишите 
#функцию, которая проверяет баланс скобок в строке. Возможные символы 
#скобок: '(', ')', '{', '}', '[' и ']'. Напишите тесты.
def compiler(a):

	assert a != ""

	a = list(a)
	P = cP = S = cS = B = cB = 0 
	for i in range(len(a)):
		if a[i] == "(":
			P += 1
		elif a[i] == ")":
			cP += 1
		elif a[i] == "[":
			S += 1
		elif a[i] == "]":
			cS += 1
		elif a[i] == "{":
			B += 1
		elif a[i] == "}":
			cB += 1
		if P < cP or S < cS or B < cB:
			return print("Ошибка компиляции: начало операции с закрытой скобки ")
	if P == cP and S == cS and B == cB: 
		print("Компиляция прошла успешно ")
	else:
		print("Ошибка компиляции: операция не определена ")
compiler("()(){}[]()dsd()  (")
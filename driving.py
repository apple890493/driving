country = input("請輸入國家: ")
age = input("請輸入年齡: ")
age = int(age)
if country == "台灣":
	if age >= 18:
		print("可以考駕照囉!")
	else:
		print("還不能考駕照唷!")
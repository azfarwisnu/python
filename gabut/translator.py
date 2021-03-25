from googletrans import Translator

translator = Translator()
print("Program Translate Bahasa Indonesia ke apa aja")
print("============================================")

while True:
	text = input("Masukan Text : ")
	trans = input("Translate ke? ")

	if trans == "korea":
		korea = translator.translate(text, dest = 'ko')
		print("Hasil Text   : ",korea.text)
		print("Kalo ngomong begini : ",korea.pronunciation)
		print("@wisnuazfar")
		print("==================== \n")
	elif trans == "jepang":
		jepang = translator.translate(text, dest = 'ja')
		print("Hasil Text   : ",jepang.text)
		print("Kalo ngomong begini : ",jepang.pronunciation)
		print("@wisnuazfar")
		print("==================== \n")
	elif trans == "inggris":
		inggris = translator.translate(text)
		print("Hasil Text   : ",inggris.text)
		print("Kalo ngomong begini : ",inggris.pronunciation)
		print("@wisnuazfar")
		print("==================== \n")






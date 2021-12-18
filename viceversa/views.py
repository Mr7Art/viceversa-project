from django.shortcuts import render


def home(request):
	return render(request,'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	reverse_text = user_text[::-1]
	number_of_words = len(user_text.split())
	print(number_of_words)
	return render(request,'reverse.html',{'usertext':user_text,'reversedtext':reverse_text,'numberwords':number_of_words})
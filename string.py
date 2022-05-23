
#1
lang = 'python'
print(lang[0], lang[2])

#2
license_plate = "24가 2210"
print(license_plate[-4:])

#3
string = "홀짝홀짝홀짝"
print(string[::2])

#4
string = "python"
print(string[::-1])

#5
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-"," ")
print(phone_number1)

#6
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-","")
print(phone_number1)

#7
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

#8
error

#9
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

#10
aBcd가 출력 #틀림 abcd가 그대로 출력 bcs 문자열은 변경할 수 없는 자료형

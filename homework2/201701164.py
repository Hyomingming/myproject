import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

#5
print("@problem5ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def add_vectors(u,v):
    if(len(u)==len(v)):#길이가 같아야 더할수 있으므로
        list=[a+b for a,b in zip(u, v)]#u안에 있는게 a, v안에있는게 b
    return list

test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

#6
print("@problem6ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def scalar_mult(s,v):
    list=[s*a for a in v]#v안에있는 a들에 s를 곱한다
    return list

test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

#7
print("@problem7ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def dot_product(u,v):
    if(len(u)==len(v)):
        list=[a*b for a,b in zip(u,v)]
        result=sum(list)
    return result

test(dot_product([1, 1], [1, 1]) ==  2)
test(dot_product([1, 2], [1, 4]) ==  9)
test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

#8 벡터 외적 공식= (u2v3-u3v2),(u3v1-u1v3),(u1v2-u2v1)
print("@problem8ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def cross_product(u,v):
    if(len(u)==len(v)):
        result=[(u[1]*v[2]-u[2]*v[1]),(u[2]*v[0]-u[0]*v[2]),(u[0]*v[1]-u[1]*v[0])]
    return result

test((cross_product([1,2,3],[4,5,6])) == [-3, 6, -3])
test((cross_product([4,5,6],[1,2,3])) == [3, -6, 3])

#9 어떨때 달라지는지 차이점 쓰기
print("@problem9ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
song = "The rain in Spain..."
song2 = "The rain in Spain... "
print("\" \".join(song.split()) == song 은 true가 나오지만")#공백으로 나눴다가 다시 공백으로 합치기 때문에 같다
print("\" \".join(song2.split()) == song2는 맨뒤에 공백이 있었다가 join을 하게되면 맨뒤 공백이 사라지기 때문에 false가 나오게 된다. ")
#10
print("@problem10ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def replace(s,old,new):
    list = s.split(old) #오래된거 빠지고 나눠짐
    s = new.join(list) #새로운 걸로 합쳐짐
    return s

test(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

print("**************************************************************")

#1
print("@problem1ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print("Python"[1])
print("Strings are sequences of characters."[5])
print(len("wonderful"))
print("Mystery"[:4])
print("p" in "Pineapple")
print("apple" in "Pineapple")
print("pear" not in "Pineapple")
print("apple" > "pineapple")
print("pineapple" < "Peach")

#2
print("@problem2ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
prefixes = "JKLMNOPQ"
suffix = "ack"
for letter in prefixes:#O,Q일때만 u붙이기
    if(letter=="O"or letter=="Q"):
        letter+="u"
    print(letter + suffix)

#3
print("@problem3ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def count_letters(fruit):
    count = 0
    for char in fruit:
        if char == "a":
            count += 1
    print(count)
count_letters("banana")

#4
print("@problem4ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def count_letters2(fruit,c):#파라미터 총3개 friut,c,find함수 안에 c
    count = 0
    for i in range(len(fruit)):
        if fruit.find(c) != -1:
            fruit = fruit.replace(c,"",1)#a를 찾고 없애지 않으면 6번다 첫번째 a를 찾기 때문에 6이 나온다.
            count += 1
    print(count)
count_letters2("banana","a")

#5 구두점=.,:;"-'
print("@problem5ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def sentence(s,e):
    s = s.replace(".", "")
    s = s.replace(",", "")
    s = s.replace(":", "")
    s = s.replace(";", "")
    s = s.replace("\"", "")
    s = s.replace("-", "")
    s = s.replace("\'", "")
    s = s.replace("?","")
    s = s.replace("!","")#구두점 전부 제거
    list=s.split() #공백으로 나눔
    count=len(list)#단어수
    ecount=0 #e가 들어간 단어수
    for i in range(len(list)):
        if e in list[i]:
            ecount += 1
    per=(ecount / count) * 100
    print(s)
    print('Your text contains',count,'words, of which' ,ecount ,'(',round(per,1),'%) contain an "',e,'"')
s=''' hello i'm hyomin.
Nice to meet you;
I love you'''#단어 11개 e들어간 단어 4개
sentence(s,"e")

#6
print("@problem6ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def multiplication_table():
    print("\t\t",end = '')
    for i in range(1,13):
        print('{:3d}'.format(i), end='\t')# 옆으로 쭉써지게
    print()
    print("\t:" + "--------------------------------------------------")#밑줄
    for i in range(1,13):
        print('{:2d}'.format(i), ":", end='\t')#1~12 자릿수 예쁘게 맞추기
        for j in range(1,13):
            print(('{:3d}'.format(i*j)), end='\t')
        print()
multiplication_table()

#7
print("@problem7ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def reverse(s):
    return s[::-1]#거꾸로 출력

test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")

#8
print("@problem8ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def mirror(s):
    return s + s[::-1]#그대로+거꾸로

test(mirror("good") == "gooddoog")
test(mirror("Python") == "PythonnohtyP")
test(mirror("") == "")
test(mirror("a") == "aa")

#9
print("@problem9ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def remove_letter(c,word):
    if c in word:
        word=word.replace(c,"")#만약에 있으면 없앰
    return word

test(remove_letter("a", "apple") == "pple")
test(remove_letter("a", "banana") == "bnn")
test(remove_letter("z", "banana") == "banana")
test(remove_letter("i", "Mississippi") == "Msssspp")
test(remove_letter("b", "") == "")
test(remove_letter("b", "c") == "c")

#10 리버스 함수를 써라
print("@problem10ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def is_palindrome(word):
    if word==reverse(word):
        return True
    else:
        return False

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome(""))# 공백스트링도 팰린드롬이다.

#11
print("@problem11ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def count(c,word):
    count=0
    for i in range(len(word)):
         if c==word[i:i+len(c)]:#인덱스가 한글자씩 생기기때문에 c의 길이만큼으로 정해준다
             count+=1
    return count

test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 4)

#12 원하는 단어 한번만 없애기
print("@problem12ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def remove(c,word):
    return word.replace(c,"",1)

test(remove("an", "banana") == "bana")
test(remove("cyc", "bicycle") == "bile")
test(remove("iss", "Mississippi") == "Missippi")
test(remove("eggs", "bicycle") == "bicycle")

#13 원하는 단어 다 없애기
print("@problem13ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
def remove_all(c,word):
    return word.replace(c,"")

test(remove_all("an", "banana") == "ba")
test(remove_all("cyc", "bicycle") == "bile")
test(remove_all("iss", "Mississippi") == "Mippi")
test(remove_all("eggs", "bicycle") == "bicycle")
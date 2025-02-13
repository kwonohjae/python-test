title='서기 1년 1월 1일부터'\
     ' 오늘까지'\
     ' 일 수 구하기'


title2=('서기 1년'
        ' 1월 1일'
        ' 오늘')
month=[1,2,3,
       4,5,6]
print(month)

a=[0,1,2,3,4,5,6,7,8,9]
print(a[2:3])

year=2001
if(year % 4 == 0) and (year % 100 !=0):
    print(year,"는 윤년")
elif year % 400 == 0:
    print(year,"은 윤년")
else:
    print(year, "윤년 아님")
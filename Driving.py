country = input('請問您是那國人： ')
age = input('請問您的年齡： ')
age = int(age)

if country == '台灣':
    if age >= 18:
        print('您是', country, ',', age ,'歲，可以考駕照哦！')
    else:
        print('您未滿18歲，騎單車吧！')
elif country == '美國':
    if age >= 16:
        print('您是', country, ',', age ,'歲，可以考駕照哦！')
    else:
        print('您未滿16歲，騎單車吧！')      
else:
    print('目前僅能輸入「台灣」與「美國」哦！') 
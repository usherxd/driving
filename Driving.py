country = input('請問您是那國人： ')
age = input('請問您的年齡： ')
age = int(age)

if country == '台灣' or 'taiwan':
    if age >= 18:
        print('您', age ,'歲，可以考駕照哦！')
    else:
        print('您未滿18歲，騎單車吧！')
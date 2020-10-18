s = ('sunny')
r = ('rainy')
S = ('snowy')
user_chose = input('voer weer in:')

if user_chose.lower() == s.lower():
    print('sunglases time')
elif user_chose.lower() == r.lower():
    print('umbrella time')
elif user_chose.lower() == S.lower():
    print('build a snowman')
else:
    print ('wrong input')

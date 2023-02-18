import os
#TRY
try:
    if os.path.exists('Log1.txt'):
        os.remove('Log1.txt')
except:
    pass
try:
    if os.path.exists('Log2.txt'):
        os.remove('Log2.txt')
except:
    pass
try:
    if os.path.exists('Log3.txt'):
        os.remove('Log3.txt')
except:
    pass
try:
    if os.path.exists('Log4.txt'):
        os.remove('Log4.txt')
except:
    pass
try:
    if os.path.exists('Log5.txt'):
        os.remove('Log5.txt')
except:
    pass



#NEW
try:
    new = open("Log1.txt", "w", encoding='utf-8')
except:
    pass






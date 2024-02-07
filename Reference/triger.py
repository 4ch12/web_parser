
string = '410,80'
if '.'and',' in string:
    string = string.split(',')[0].replace('.' , '')+ '.' + string.rsplit(',', 1)[1]
    print(float(string))
elif ',' in string:
    string = string.replace(',' , '.')
    string = ''.join(string) 
    print(float(string))
elif '.' in string:
    string= string.replace('.' , '')
    print(float(string),'DOT')
    




import discord
from langdetect import DetectorFactory
DetectorFactory.seed = 0
import langdetect as ld

dictdata={'Z':'(','z':'ผ','X':')','x':'ป','C':'ฉ','c':'แ','V':'ฮ','v':'อ','B':'ฺ','b':'ิ','N':'์','n':'ื','M':'?','m':'ท','<':'ฒ',',':'ม','>':'ฬ','.':'ใ','?':'ฦ','/':'ฝ',
'A':'ฤ','a':'ฟ','S':'ฆ','s':'ห','D':'ฏ','d':'ก','F':'โ','f':'ด','G':'ฌ','g':'เ','H':'็','h':'้','J':'๋','j':'่','K':'ษ','k':'า','L':'ศ','l':'ส',':':'ซ','"':'.',"'":"ง",':':'ซ',';':'ว',
'Q':'๐','q':'ๆ','W':'"','w':'ไ','E':'ฎ','e':'ำ','R':'ฑ','r':'พ','T':'ธ','t':'ะ','Y':'ํ','y':'ั','U':'๊','u':'ี','I':'ณ','i':'ร','O':'ฯ','o':'น','P':'ญ','p':'ย','{':'ฐ','[':'บ','}':',',']':'ล','|':'ฅ',']':'ฃ',
'~':'%','`':'_','@':'๑','2':'/','#':'๒','3':'-','$':'๓','4':'ภ','%':'๔','5':'ถ','^':'ู','6':'ุ','&':'฿','7':'ึ','*':'๕','8':'ค','(':'๖','9':'ต',')':'๗','0':'จ','_':'๘','-':'ข','+':'๙','=':'ช'}

def en2th_text(data):
    ''' return en -> th mapping '''
    data = list(data)
    data_out = ""
    for letter in data:
        try:
            letter = dictdata[letter]
        except:
            letter = letter
        data_out+=letter
    return data_out

def th2en_text(data):
    ''' return th -> en mapping '''
    data = list(data)
    data_out = ""
    dictdataeng= {v: k for k, v in dictdata.items()} ##สลับ key กับ value ใน dict แล้วแทนค่าใน dict ใหม่
    for letter in data:
        try:
            letter = dictdataeng[letter]
        except:
            letter = letter
        data_out+=letter
    return data_out

def main():
    text = input()
    if text.isspace() == True or text.isnumeric() == True or text.isdecimal() == True:
        quit()
    try:
        if text.isascii() == False and ld.detect(text) != 'th':
            print('Not supported language.')
            quit()
    except:
        quit()

    ask = input('Do you want to decode the text? (Y/N): ')
    if ask == 'Y':
        if ld.detect(text) == 'th':
            print(th2en_text(text))
        else:
            print(en2th_text(text))
    if ask == 'N':
        print(text)



main()

from tkinter import *
from tkinter import messagebox
import os

window = Tk()
window.title("파일 자동 생성")
window.geometry("440x300")
window.resizable(False, False)

# 기능작업 

path = '경로'

def create_folder2():
    result1 = textExample1.get("1.0", 'end-1c') # 이걸로 해야하네; END 도 안되고 "end" 도 안됨 윈도우만 그런듯;
    result2 = textExample2.get("1.0", 'end-1c')
    result3 = textExample3.get("1.0", 'end-1c')
    re = result1 + " " + result2 + " " + result3
    print(result1)
    print(result2)
    print(result3)
    print(re)
    create_folder(path + re)
    create_folder(path + re + '/폴더1')
    create_folder(path + re + '/폴더2')
    create_folder(path + re + '/폴더3')
    messagebox.showinfo(" ", "폴더가 생성되었습니다.")


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

# 스타일링 작업

label = Label(window, text="폴더이름", height=5)
label.pack()

label1 = Label(window, text="날짜")
label1.pack()

textExample1 = Text(window, height= 1, width= 40)
textExample1.pack()

label2 = Label(window, text="품명")
label2.pack()
textExample2 = Text(window, height= 1, width= 40)
textExample2.pack()

label3 = Label(window, text="수주처")
label3.pack()
textExample3 = Text(window, height= 1, width= 40)
textExample3.pack()

btnRead = Button(window, height = 1, width = 10, text = "폴더 생성", command = create_folder2)
btnRead.pack()

window.mainloop()

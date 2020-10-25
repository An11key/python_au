import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from generate_dm1 import Ui_Form

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()


def beat_name1(name):
    name = "# {}".format(name.split('.')[0].capitalize())
    return name


def beat_name2(name):
    name = name.lower()
    s = ''
    ar = name.split(' ')
    for i, item in enumerate(ar):
        if i != len(ar) - 1:
            s += item + '-'
        else:
            s += item
    name = "+ [{}](#{})".format(name.capitalize(), s)
    return name


def beat_name3(name):
    name = "## {}".format(name)
    return name


def beat_link(link):
    link = "{}".format(link)
    return link


def beat_code(code):
    code = "```python\n{}\n```".format(code)
    return code


def w_in_file(file, massn1, massn2, massel):
    file.write(massn1.strip())
    file.write("\n\n")
    for item in massn2:
        file.write(item.strip())
        file.write("\n")
    file.write("\n")
    for i in range(len(massn2)):
        file.write(massel[i].strip())
        file.write("\n\n")


def add_item(mass, item):
    mass.append(item)


def bp():
    name = ui.lineEdit.text()
    link = ui.lineEdit_2.text()
    code = ui.lineEdit_3.text()
    file = ui.lineEdit_4.text()
    if not os.path.exists(file):
        f = open(file, 'w')
        f.close()
    f = open(file, 'r')
    if os.stat(file).st_size == 0:
        f.close()
        f = open(file, 'w')
        f.write(beat_name1(file))
        f.write('\n\n')
        f.write(beat_name2(name))
        f.write('\n\n')
        f.write(beat_name3(name))
        f.write('\n\n')
        f.write(beat_link(link))
        f.write('\n\n')
        f.write(beat_code(code))
        f.close()
    else:
        all_elem = f.read().split("##")
        f.close()
        all_names = all_elem[0].split('\n\n')[0]
        all_names2 = all_elem[0].split('\n\n')[1].split('\n')

        for i in range (1,len(all_elem)):
            all_elem[i] = '##{}'.format(all_elem[i])

        new_elem = beat_name3(name) + '\n\n' + beat_link(link) + '\n\n' + beat_code(code)
        all_elem.append(new_elem)
        if beat_name2(name) in all_names2:
            return
        add_item(all_names2, beat_name2(name))
        print(all_elem[1:])
        f = open(file, 'w')
        w_in_file(f, all_names, all_names2, all_elem[1:])
        f.close()
        f = open(file, 'r')
        str = f.read().strip()
        f.close()
        f = open(file, 'w')
        f.write(str)
        f.close()


ui.pushButton.clicked.connect(bp)

sys.exit(app.exec_())

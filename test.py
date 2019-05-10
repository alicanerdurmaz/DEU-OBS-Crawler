import re
import passwords
from robobrowser import RoboBrowser
import time

br = RoboBrowser()


for i in range(0, 52):

    # time.sleep(3)
    br.open("http://www.vproce.net/OgrenciBilgiSistemi/default.aspx")

    form = br.get_form(action='./default.aspx')
    form['txtusername'] = passwords.OGR_PASS[i]
    # time.sleep(3)
    br.submit_form(form)

    br.open("http://www.vproce.net/OgrenciBilgiSistemi/dersbilgileri.aspx?dersno=1")
    # time.sleep(3)

    src = str(br.parsed())

    match = re.search(r'<div class="not">(.*?)</div>', src)
    if match:
        print(passwords.OGR_PASS[i] + " = " + match.group(1))
        file1 = open("puanlar.txt", "a")
        file1.write(str(match.group(1)))
        file1.write('\n')
        file1.close()

    # time.sleep(3)

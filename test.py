import re
import passwords
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import requests
import time

br = RoboBrowser()

# if pasworlds.len < 2. program not running.
# i dont know why.
for x in range(0, passwords.len):

    # time.sleep(3)
    br.open("http://www.vproce.net/OgrenciBilgiSistemi/default.aspx")

    form = br.get_form(action='./default.aspx')
    form['txtusername'] = passwords.OGR_PASS[x]
    # time.sleep(3)
    br.submit_form(form)

    temp = str(br.parsed())
    firstPage = BeautifulSoup(temp, 'lxml')
    for i in firstPage.findAll("div", {"id": "DersKodu"}):
        if(i.text == "MAT1010"):
            tempLink = i.parent
            linka = str(tempLink)
            break

    finalLink = "http://www.vproce.net/OgrenciBilgiSistemi/" + linka[9:36]

    br.open(finalLink)
    # time.sleep(3)

    src = str(br.parsed())

    match = re.search(r'<div class="not">(.*?)</div>', src)
    if match:
        print(passwords.OGR_PASS[x] + " = " + match.group(1))
        # print(match.group(1))
        file1 = open("puanlar.txt", "a")
        file1.write(str(match.group(1)))
        file1.write('\n')
        file1.close()

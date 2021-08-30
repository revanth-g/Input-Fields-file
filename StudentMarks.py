import base64
import requests
import json

def studentMarks(url):
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json() 
        content = base64.b64decode(req['content'])
        str = content.decode('UTF-8')
        data=str.split()
        marks={}
        count={}

        for i in data:
            temp=json.loads(i)
            for j in temp :
                if j in marks.keys():
                    marks[j] = temp[j]+marks[j]
                    count[j]=count[j]+1
                else :
                    marks[j]=temp[j]
                    count[j]=1

        for i in sorted(marks.keys()):
            if i == "Subject":
                continue
            print(i,count[i],marks[i])
        print(" ")
        print("Completed")
    else:
        print('Content was not found.')

# url = "https://raw.githubusercontent.com/repos/revanth-g/Input-Fields-file/contents/Inputs.txt"
# studentMarks(url)
url1 = "https://api.github.com/repos/revanth-g/Input-Fields-file/contents/input4.txt"
studentMarks(url1)
url2 = "https://api.github.com/repos/revanth-g/Input-Fields-file/contents/input5.txt"
studentMarks(url2)
url3 = "https://api.github.com/repos/revanth-g/Input-Fields-file/contents/input6.txt"
studentMarks(url3)
url4 = "https://api.github.com/repos/revanth-g/Input-Fields-file/contents/input7.txt"
studentMarks(url4)

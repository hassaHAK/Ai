student=[]
student_1={"name":"Hassan","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":67,"quiz2":50,"mid":70,"final":90}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":77,"quiz2":75,"mid":60,"final":80}}}

student_2={"name":"Arif","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":45,"quiz2":70,"mid":70,"final":95}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":79,"quiz2":65,"mid":80,"final":70}}}

student_3={"name":"Hamza","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":47,"quiz2":76,"mid":71,"final":71}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":45,"quiz2":93,"mid":75,"final":46}}}

student_4={"name":"Arif","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":51,"quiz2":73,"mid":69,"final":59}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":15,"quiz2":74,"mid":30,"final":70}}}

student_5={"name":"Ghufran","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":45,"quiz2":70,"mid":70,"final":95}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":79,"quiz2":65,"mid":80,"final":70}}}

student_6={"name":"Ashar","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":67,"quiz2":50,"mid":70,"final":90}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":77,"quiz2":75,"mid":60,"final":80}}}


student_7={"name":"Wasif","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":51,"quiz2":73,"mid":69,"final":59}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":15,"quiz2":74,"mid":30,"final":70}}}

student_8={"name":"Fakhir","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":47,"quiz2":76,"mid":71,"final":71}},
                            "class2":{"name":"cnn","marks":
                                                              {"quiz1":45,"quiz2":93,"mid":75,"final":46}}}
                                              
                                    
        
student_9={"name":"Huzaifa","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":10,"quiz2":70,"mid":90,"final":95}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":97,"quiz2":56,"mid":79,"final":40}}}

student_10={"name":"Shahzar","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":67,"quiz2":50,"mid":70,"final":90}},
                            "class2":{"name":"cnn","marks":
                                                              {"quiz1":77,"quiz2":75,"mid":60,"final":80}}}


student.append(student_1)
student.append(student_2)
student.append(student_3)
student.append(student_4)
student.append(student_5)
student.append(student_6)
student.append(student_7)
student.append(student_8)
student.append(student_9)
student.append(student_10)
id_no=int(input("Enter id:\n"))-1
class_name=input("Enter Class:\n").lower()
exam=input("Enter Exam:\n").lower()
if (class_name=="ai"):
    print(student[id_no].get("class1").get("marks").get(exam))
if (class_name=="cnn"):
    print(student[id_no].get("class2").get("marks").get(exam))


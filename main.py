import student

# main functions section
def addNewStudent():
    def setStudentNo():
        studentNo_ = input("3 reqemden ibaret telebe nomresini daxil edin: ").strip()
        if studentNo_.isdigit() and len(studentNo_) == 3:
            for s in student.userList:
                if s.studentNo == studentNo_:
                    print("Bu koda sahib telebe artiq sistemde var!")
                    break
            return studentNo_

        else:
            print("Telebe nomresi dogru daxil edilmeyib!")
    studentNo = setStudentNo()

    def setName():
        name_ = input("Adi daxil edin: ").strip()
        if len(name_) != 0:
            return name_
        else:
            print("Ad bosh ola bilmez! Daxil edin.")
    name = ""
    if bool(studentNo):
        name = setName()

    def setSurname():
        surname_ = input("Soyadi daxil edin: ").strip()
        if len(surname_) != 0:
            return surname_
        else:
            print("Soyad bosh ola bilmez! Daxil edin.")
    surname = ""
    if bool(name):
        surname = setSurname()

    def setEmail():
        email_ = input("Emaili daxil edin: ").strip()
        if email_.find("@") != -1 and len(email_) != 0:
            return email_
        else:
            print("Email melumatlari dogru daxil edilmeyib! Tekarar daxil edin.")
    email = ""
    if bool(surname):
        email = setEmail()

    def setPhone():
        phone_ = input("Telefon nomresini daxil edin (+994_________): ").strip()
        if phone_.startswith("+994") and len(phone_) == 13 and len(phone_) != 0:
            return phone_
        else:
            print("Telefon nomresi dogru daxil edilmeyib! Tekrar daxil edin.")
    phone = ""
    if bool(email):
        phone = setPhone()

    if bool(studentNo) and bool(name) and bool(surname) and bool(email) and bool(phone):
        obj = student.Student(studentNo, name, surname, email, phone)
        student.userList.append(obj)

def printStudents():
    if len(student.userList) == 0:
        print("Sistemde telebe yoxdur!")
    else:
        for s in student.userList:
            s.printInfo()

def deleteStudent():
    studentNo_ = input("Silinecek telebenin kodunu daxil edin:").strip()
    if studentNo_.isdigit() and len(studentNo_) == 3:
        check = False

        def checkStudents():
            for x in student.userList:
                if x.studentNo == studentNo_:
                    return True

        check = checkStudents()
        if check:
            for s in student.userList:
                if studentNo_ == s.studentNo:
                    student.userList.remove(s)
        else:
            print("Sistemde bu koda sahib telebe tapilmadi!")

    else:
        print("Telebe nomresi dogru daxil edilmeyib!")

def editStudent():
    studentNo = input("Melumatlarina duzelish edilecek telebenin kodunu daxil edin:").strip()

    if studentNo.isdigit() and len(studentNo) == 3:
        check = False

        def checkStudents():
            for x in student.userList:
                if x.studentNo == studentNo:
                    return True

        check = checkStudents()
        if check:
            for s in student.userList:
                if s.studentNo == studentNo:
                    name = input("Adi daxil edin: ").strip()

                    surname = input("Soyadi daxil edin: ").strip()

                    def setEmail():
                        email_ = input("Emaili daxil edin: ").strip()
                        if email_.find("@") != -1:
                            return email_
                        else:
                            print("Email melumatlari dogru daxil edilmeyib! Tekarar daxil edin.")
                            setEmail()

                    email = setEmail()

                    def setPhone():
                        phone_ = input("Telefon nomresini daxil edin (+994_________): ").strip()
                        if phone_.startswith("+994") and len(phone_) == 13:
                            return phone_
                        else:
                            print("Telefon nomresi dogru daxil edilmeyib! Tekrar daxil edin.")
                            setPhone()

                    phone = setPhone()

                    s.name = name
                    s.surname = surname
                    s.email = email
                    s.phone = phone

        else:
            print("Sistemde bu koda sahib telebe tapilmadi!")
    else:
        print("Telebe nomresi dogru daxil edilmeyib! Tekrar daxil edin.")

def printByName():
    name = input("Telebe adini daxil edin: ").strip()
    check = False

    def checkStudents():
        for x in student.userList:
            if name == x.name:
                return True

    check = checkStudents()

    if check:
        for s in student.userList:
            if name == s.name:
                s.printInfo()
    else:
        print("Sistemde bu ada sahib telebe tapilmadi!")


# menu section
def menu():
    i = input("""
            1. Telebe daxil et
            2. Telebe koduna gore telebe melumatlarini sil
            3. Telebe koduna gore telebe melumatlarini deyishdir
            4. Telebe adina gore telebe melumatlarini goster
            5. Butun telebelerin melumatlarini goster
            6. Sistemden chix

            Menyudaki emrleri icra etmek uhun muvafiq reqemi daxil edin:
        """).strip()

    if bool(i):
        return int(i)

def showMenu():
    command = menu()

    if command == 1:
        if len(student.userList) < 10:
            print(len(student.userList))
            addNewStudent()
        else:
            print("Sistemde yeni telebe uchun yer yoxdur! Maksimum 10 telebe daxil ede bilersiz.")
    elif command == 2:
        deleteStudent()
    elif command == 3:
        editStudent()
    elif command == 4:
        printByName()
    elif command == 5:
        printStudents()
    elif command == 6:
        exit()
    else:
        print("Daxil etdiyiniz emr dogru deyil!")

# App start section
while True:
    showMenu()

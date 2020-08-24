class Student:
    studentNo = None
    name = None
    surname = None
    email = None
    phone = None



    def __init__(self, _studentNo, _name, _surname, _email, _phone):
        self.studentNo = _studentNo
        self.name = _name
        self.surname = _surname
        self.email = _email
        self.phone = _phone


    def printInfo(self):
        print(
            f"""
            Telebe kodu: {self.studentNo}
            Ad: {self.name}
            Soyad: {self.surname}
            Email: {self.email}
            Telefon: {self.phone}
            """
        )

userList = []


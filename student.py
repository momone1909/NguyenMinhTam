class Student:
    count = 0
    def __init__(self , msv , name, namsinh, quequan, chuyennganh):
        self.msv= msv
        self.name = namsinh
        self.quequan = quequan
        self.namsinh =  namsinh
        self.chuyennganh = chuyennganh
        Student.count += 1
    def layid(self):
        return self.msv
    def laychuyennganh(self):
        return self.chuyennganh  
    def taoten(self, name):
        self.name = name
    def layten(self):
        return self.name
    def show_info(self):
        print(f"\nThông tin Sinh Viên :  \n")
        print(f"Id :  { self.layid() }")
        print(f"Tên Sinh Viên :  { self.name }")
        print(f"năm sinh : {self.namsinh}")
        print(f"Quên quán : {self.quequan}")
        print(f"Chuyên ngành : {self.chuyennganh}")
        

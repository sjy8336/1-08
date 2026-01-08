class Student:
    student_id = None
    name = None
    cname = None

class Tops:
    def __init__(self, id, name, cn):
        self.__student_id = id
        self.__name = name
        self.__cname = cn
    
    def input_info():
        self.__student_id = input('학번을 입력하세요 >>')
        self.__name = input('이름을 입력하세요 >>')
        self.__cname = input('학급명을 입력하세요 >>')

    def show_info(self):
        info = f"""  
        *******학생 정보*******
        학  번: {self.__student_id}
        이  름: {self.__name}
        학급명: {self.__cname}
        """
        return info
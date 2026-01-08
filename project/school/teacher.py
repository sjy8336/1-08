class Teacher:
    t_id = None
    name = None
    subject = None

class Topt:
    def __init__(self, id, name, sub):
        self.__t_id = id
        self.__name = name
        self.__subject = sub
    
    def input_info():
        self.__t_id = input('교번을 입력하세요 >>')
        self.__name = input('이름을 입력하세요 >>')
        self.__subject = input('담당과목을 입력하세요 >>')

    def show_info(self):
        info = f"""  
        *******교사 정보*******
        학  번: {self.__t_id}
        이  름: {self.__name}
        학급명: {self.__subject}
        """
        return info
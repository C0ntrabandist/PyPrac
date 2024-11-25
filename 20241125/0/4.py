class Sender:
    bl = True

    @classmethod
    def reprot(cls):
        if cls.bl:
            print("Greetings!")
        else:
            print("Get away!")
        cls.bl = False


class Asker:
    @staticmethod
    def askall(lst):
        for elem in lst:
            elem.reprot()


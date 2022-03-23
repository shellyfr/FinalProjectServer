import script


class DBManager:
    def _init_(self):
        pass

    def getgroupnum(self, id):
        script.cur.execute("Select * From codes Where id=%s;",(id,))
        num = script.cur.fetchall()
        if not num:
            return ""
        number=num[0][0]
        return number

    def getfinish(self, id):
        script.cur.execute("Select * From codes Where id=%s;",(id,))
        num = script.cur.fetchall()
        if num[0][2] == 1:
            return False
        return True

    def user_finish(self,id):
        print(4)
        script.cur.execute('''UPDATE codes SET isfin = 1 WHERE id=%s;''', (id,))
        script.cur.execute("Select isfin From codes Where id=%s;", (id,))
        print(script.cur.fetchall())

        # here we have a problemmm!!!
        # here we have a problemmm!!!



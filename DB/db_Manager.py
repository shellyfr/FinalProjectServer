import script


class DBManager:
    def _init_(self):
        pass

    def getFromCodes(self, id):
        sql_query = "Select * From codes Where id=" + id + ";"
        num=script.get_data_from_db(sql_query)
        print( num)
        if num == [] :
            return False
        return num

    def updateCodes(self, id, time1, x):
        if x=='1':
            script.update_db("UPDATE codes SET isfin = 1 WHERE id=" + id + ";")
            script.update_db("UPDATE codes SET end_time ='"+time1+"'  WHERE id= " + id + ";")
        else:
            script.update_db("UPDATE codes SET start_time ='" + time1 + "'  WHERE id= " + id + ";")


    def insertPosition(self, id, snew1, snew2, snew3, snew4, snew5, snew6):
        script.insertDB("INSERT INTO positions(entry_code, s1, s2, s3, s4, s5, s6 ) "
                        "VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')" %
                        (id, snew1, snew2, snew3, snew4, snew5, snew6))

    def insertOpinion(self, id, onew1, onew2 ):
        script.insertDB("INSERT INTO opinion(entry_code, o1, o4) VALUES('%s', '%s' , '%s')" % (id, onew1, onew2 ))

    def insertDemo1(self, id, age1, gender1,education1, income1,employment1,computer1, phone1 ):
        script.insertDB("INSERT INTO demografic1(entry_code, age, gender,education, income,employment,computer, phone) "
                        "VALUES('%s', '%s' , '%s','%s', '%s', '%s', '%s', '%s')" %
                        (id, age1, gender1,education1, income1,employment1,computer1, phone1))

    def insertDemo2(self, id, myspace1, space_scale1, space_private1, space_size1,noise1,dark1, density1):
        script.insertDB("INSERT INTO demografic2(entry_code, myspace, space_scale,space_private, space_size,noise,dark, density ) "
                        "VALUES('%s', '%s' , '%s','%s', '%s', '%s', '%s', '%s')" %
                        (id, myspace1, space_scale1,space_private1, space_size1,noise1,dark1, density1))

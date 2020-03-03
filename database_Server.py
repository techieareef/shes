import mysql.connector
import json
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Text
from datetime import datetime
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from shutil import copyfile
import random
import commonFunction as CF

with open('Const/config.json') as i:

    json_const = json.load(i)
doctorEmail = json_const["Doctor_email"]

#engine = create_engine('sqlite:///C:\\path\\to\\foo.db')
engine = create_engine('sqlite:///Databases\\Shes_V1.db')
connection = engine.connect()

session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

#The business case here is that a company can be a stakeholder in another company.
class QuesCat(Base):
    __tablename__ = 'ques_category'
    q_cat_id = Column(Integer, primary_key=True)
    cat_name = Column(String)
    description = Column(String)
    sym_type = Column(Integer)
    questionaries = relationship("Questions", backref="ques_category")
class Questions(Base):
    __tablename__ = 'questions'
    q_id = Column(Integer, primary_key=True)
    name = Column(String)
    qus_type = Column(Integer)
    q_cat_id = Column(Integer, ForeignKey('ques_category.q_cat_id'))
    #QuesCat = relationship("QuesCat", back_populates="questions")
    ques_answers = relationship("Answers", backref="questions")
class Answers(Base):
    __tablename__ = 'ques_answers'
    ans_id = Column(Integer, primary_key=True)
    q_id = Column(Integer, ForeignKey('questions.q_id'))
    #Questions = relationship("Questions", foreign_keys=[q_id])
    name = Column(String)


Base.metadata.create_all(engine)
q1 = session.query(QuesCat).all()
def getQuestions():
# simple query test
    q1 = session.query(QuesCat).all()
    return q1

conn = sqlite3.connect(json_const['DB_NAME'])
c = conn.cursor()

try:
    # Create the connection object
    myconn = mysql.connector.connect(host=json_const['Server'], user=json_const['db_Username'], passwd=json_const['DB_Password'], \
                                     database=json_const['Database_name'])

    # printing the connection object
    # creating the cursor object
    mycursor = myconn.cursor()
except Exception as e:
    print(e)


def questionSync():
    myconn = mysql.connector.connect(host=json_const['Server'], user=json_const['db_Username'],
                                     passwd=json_const['DB_Password'], \
                                     database=json_const['Database_name'])

    mycursor = myconn.cursor()
    mycursor.execute("SELECT * FROM ques_category")
    cat_result = mycursor.fetchall()
    if len(cat_result) > 0:
        c.execute('delete from ques_category')
        conn.commit()
        c.execute('delete from questions')
        conn.commit()
        c.execute('delete from ques_answers')
        conn.commit()
        c.executemany('INSERT INTO ques_category(q_cat_id, cat_name, description, status, created_by, sym_type) \
         VALUES (?,?,?,?,?,?)', cat_result)
        conn.commit()
    mycursor.execute("SELECT * FROM questions")
    ques_result = mycursor.fetchall()
    if len(ques_result) > 0:
        #print(ques_result)
        c.executemany('INSERT INTO questions(q_id, q_cat_id, name, qus_type, status, created_by) \
        VALUES (?,?,?,?,?,?)', ques_result)
        conn.commit()
    mycursor.execute("SELECT * FROM ques_answers")
    answer_result = mycursor.fetchall()
    if len(answer_result) > 0:
        #print(answer_result)
        c.executemany('INSERT INTO ques_answers(ans_id, name, q_id, status) VALUES (?,?,?,?)', answer_result)
        conn.commit()

def _userregi(data):
    c.execute(
            "INSERT INTO ship_registration(id,ship_name, ship_email, ship_email_pwd, sys_pwd,call_sign,\
            imo_number,country,created_at,username) VALUES (?,?,?,?,?,?,?,?,?,?)",
            (data['id'],data['ship_name'],\
             data['ship_email'], data['ship_email_pwd'], \
             data['sys_pwd'],data['call_sign'],data['imo_number'],data['country'],data['created_at'], data['ship_username']))
    conn.commit()
    return True

def _logincheck(data):
    c.execute("SELECT * FROM ship_registration WHERE username='"+ data['ship_username'] +"' and sys_pwd='"+ data['sys_pwd'] +"'")
    login_records = c.fetchall()
    c.execute("SELECT * FROM ship_registration")
    all_records = c.fetchall()
    if len(login_records) < 1 and len(all_records) < 1:
        mycursor.execute("SELECT * FROM ship_registration WHERE username='"+ data['ship_username'] +"' and sys_pwd='"+ data['sys_pwd'] +"'")
        result = mycursor.fetchall()
        if len(result) == 1:
            result = result[0]
            data_info = {
                "id" : result[0],
                "ship_name" : result[1],
                "ship_email" : result[2],
                "ship_email_pwd" : result[3],
                "sys_pwd" : result[4],
                "call_sign": result[6],
                "imo_number":result[7],
                "country" : result[5],
                "created_at" : str(datetime.now()),
                "ship_username": result[9],

            }
            _userregi(data_info)
            return True
        else:
            return False
    else:
        if len(all_records) == 1 and len(login_records) < 1:
            return False
        return True

def _getuserDetail(ship_username):
    data_info = {}
    c.execute(
        "SELECT * FROM ship_registration WHERE username='"+ship_username+"'")
    result = c.fetchall()
    if len(result) == 1:
        result = result[0]
        data_info = {
            "id": result[0],
            "ship_name": result[1],
            "ship_email": result[2],
            "ship_email_pwd": result[3],
            "sys_pwd": result[4],
            "call_sign": result[6],
            "imo_number": result[7],
            "country": result[8],
            "ship_username": result[9],
        }
    return data_info

def saveSeafearsDetails(seafearsInfo):
    try:
        c.execute('select seafer_id from seafer_info where id=(select max(id) from seafer_info)')
        seaf_res = c.fetchall()
        seafer_id = seafearsInfo['seafer_id'] + "-101"
        if seaf_res:
            seaf_no = seaf_res[0][0].split("-", 1)
            seafer_id = str(seaf_no[0]) + "-"+ str(int(seaf_no[1])+1)
        seafearsInfo['seafer_id'] = seafer_id
        seafearsInfo['created_by'] = 27
        seafearsInfo['created_at'] = str(datetime.now())
        seafearsInfo_list = list(seafearsInfo.values())
        c.execute('INSERT INTO seafer_info(seafer_id, name, surname, nationality, dob, age,sex, rank,created_by,created_at) \
                 VALUES (?,?,?,?,?,?,?,?,?,?)', seafearsInfo_list)
        conn.commit()
        return True
    except Exception:
        return False
def readSeaferDetails():
    c.execute('select * from seafer_info')
    return c.fetchall()

def SaveMedicalDetials(resultList,imageList):
    try:
        resultList1=[]
        c.execute('select medical_req_id from medical_request_info where id=(select max(id) from medical_request_info)')
        medical_res = c.fetchall()
        medical_req_id = resultList[1]
        seaferId = resultList[0]
        subject = ''

        if medical_res:
            med_no = medical_res[0][0].split("-", 1)
            medical_req_id = str(med_no[0]) + "-"+ str(int(med_no[1])+1)
        resultList[1] = medical_req_id
        MedicalQuestion = []
        emailMedicalQuestion = {}
        for ele,values in resultList[-1]:
            value = values.split("-")
            ans_id = comments = ''
            q_id = ele.split("-")
            ans_name = ''
            if q_id[-1] == '1':
                comments = value[0]
                ans_id = int(q_id[2])
                ans_name = value[0]
                emailMedicalQuestion[q_id[1]] = value[0]
            else:
                comments = ''
                ans_id = value[0]
                ans_name = value[1]
                emailMedicalQuestion[q_id[1]] =value[1]
            MedicalQuestion.append([medical_req_id, q_id[1], ans_name, comments])
        MedicalImages = []
        FnalImages = []
        if len(imageList) > 0:
            for ls in imageList:
                destination = 'Pictures/'+str(medical_req_id) + str(random.random()) + '.jpg'
                copyfile(ls, destination)
                FnalImages.append(destination)
                MedicalImages.append([medical_req_id,destination])
            c.executemany('INSERT INTO medical_req_images(medical_req_id, image) VALUES (?,?)',MedicalImages)
            conn.commit()
        resultList1=resultList[0:len(resultList)-1]
        resultList1.insert(len(resultList1),27)
        resultList1.insert(len(resultList1),str(datetime.now()))
        subject = str(seaferId) + "_" + str(medical_req_id) + "_" + " Medical Request "
        resultList1.insert(len(resultList1),str(subject))
        resultList1.insert(len(resultList1), str(doctorEmail))
        #c.execute('select q_cat_id from ques_category where cat_name = "'+resultList1[12]+'"')
        #dataa=c.fetchone()

        emailData = {
            'basicInfo': resultList1,
            "Question": emailMedicalQuestion,
            "images": FnalImages,
            'subject': subject,

        }
        resultList1.insert(len(resultList1), str(emailData))
        #print(resultList1)
        #resultList1[12]=dataa[0]

        #seafearsInfo_list = list(seafearsInfo.values())

        c.execute('INSERT INTO medical_request_info(seafer_id, medical_req_id, departure_port, arrival_port, exp_arrival_time, '
                  'present_position,latitude, longitude,temp,blood_pressure,pulse_rate,weight,symp_cat_id,other_information,'
                  'created_by,created_at,subject,doctor_email,summary) \
                 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', resultList1)
        conn.commit()
        c.executemany('INSERT INTO medical_req_ques(medical_req_id, q_id, ans_id, comments) VALUES (?,?,?,?)', MedicalQuestion)
        conn.commit()
        SuccessMessage = CF.sendMedicalRequest(emailData)
        return SuccessMessage
    except Exception:
        return False
def MedicalRecordDetails():
    c.execute('select * from medical_request_info')
    return c.fetchall()
def updateMedicalRecord(arrFinalreplayData):
    #print(arrFinalreplayData)

    try:
        text = arrFinalreplayData['text']
        subj = arrFinalreplayData['Subject']
        #print('update medical_request_info SET replay_text="'+arrFinalreplayData['text']+'" where subject="'+arrFinalreplayData['Subject']+'"')
        c.execute('update medical_request_info SET replay_text="'+arrFinalreplayData['text']+'" where subject="'+arrFinalreplayData['Subject']+'"')
        conn.commit()

        return True
    except Exception as e:
        print("Failed to update sqlite table", e)
        return False


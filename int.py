# import sqlite3
# import json
# with open('Const/config.json') as i:
#     json_const = json.load(i)
#
# device = json_const['DEVICE_FLAG']
# db = json_const['DB_NAME']
# print(db)
# conn = sqlite3.connect(json_const['DB_NAME'])
#
# c = conn.cursor()
# print(c)
#
# if device == "S":
# #     # c.execute("SELECT starttime,patientid FROM Exercisesession WHERE ID= 'D1'")
#     x=c.execute("SELECT * FROM ExerciseSession WHERE ID='D1'")
#     print(c.fetchall())
# for row in c.fetchall():
#     print("row data"+row)
#     # return row
db_patient_name="hello"
id=1
start_conv=120
end_conv=20
print("SELECT * FROM ExerciseSession WHERE PatientID='" + db_patient_name + "' and ExerciseID='" + str(id) + "'StartTime>='"+str(start_conv)+"'and StartTime<='"+str(end_conv)+'"and reps is not NULL' )
print("SELECT * FROM ExerciseSession WHERE PatientID='" + db_patient_name + "' and ExerciseID='" + str(id) + "'StartTime>='"+str(start_conv)+"'and StartTime<='"+str(end_conv)+"'"+'and reps is not NULL')
print("SELECT perfectHits, reps, StartTime, duration, minAngle, maxAngle FROM ExerciseSession WHERE PatientID='" + db_patient_name + "' and ExerciseID='" + str(id) + "'and StartTime>='"+str(start_conv)+"'and StartTime<='"+str(end_conv)+"'"+'and reps is not NULL')

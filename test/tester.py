import imaplib
import email
import sys
# from fpdf import FPDF,HTMLMixin
# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

# class HTML2PDF(FPDF, HTMLMixin):
#     pass

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "suneethactel" + ORG_EMAIL
FROM_PWD    = "cteladmin"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993


def get_first_text_block(msg):
    type = msg.get_content_maintype()

    if type == 'multipart':
        for part in msg.get_payload():
            if part.get_content_maintype() == 'text':
                return bytes.decode(part.get_payload(decode=1))
    elif type == 'text':

        return bytes.decode(msg.get_payload(decode=1))


def read_email_from_gmail():
    arrFinalReplay = {}
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')
        #type, data = mail.search(None, 'ALL')
        type, data = mail.search(None, '(FROM "suneetha.ankala@gmail.com" SUBJECT "vkishore02-101_MDR-10001_ Medical Request")')
        mail_ids = data[0]
        #print(mail_ids)
        id_list = mail_ids.split()
        #first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        #print(latest_email_id)
        #print(first_email_id)

        #for i in range(latest_email_id,first_email_id, -1):
        result,data = mail.fetch(str(latest_email_id), '(RFC822)' )
        #print(data)
        for response_part in data:
            #print(response_part)
            #print(data[1])
            #type(response_part)
            if isinstance(response_part, tuple):
                #print(str(response_part[1]))
        #print(data[0])
        #raw_Email = data[0][1]
        #print(raw_Email['subject'])
                #msg = email.message_from_string(str(response_part[1]))
                msg = email.message_from_string(response_part[1].decode("utf-8"))


                #print(msg.get_payload)
                text = get_first_text_block(msg)

                email_subject = msg['subject']
                email_from = msg['from']
                #print(text, "is of type", str(text))


                # print('From : ' + str(email_from) + '\n')
                # print('Subject : ' + str(email_subject) + '\n')
                # print('Date : ' + str(msg['Date']) + '\n')
                # print(text)
                arrFinalReplay = {
                    'From' :str(email_from),
                    'Subject': str(email_subject),
                    'Replay_Date': str(msg['Date']),
                    'text' : text
                }
                return arrFinalReplay
                # # stringlist = [x.decode('utf-8') for x in text]
                # # print(stringlist)
                # #print(text.encode())
                # FinalText = text.encode()
                # #pdf = FPDF()
                # pdf = HTML2PDF()
                #
                # table = """<table border="0" align="center" width="50%">
                #     <thead><tr><th width="30%">Header 1</th><th width="70%">header 2</th></tr></thead>
                #     <tbody>
                #     <tr><td>cell 1</td><td>cell 2</td></tr>
                #     <tr><td>cell 2</td><td>cell 3</td></tr>
                #     <tr><td>cell 2</td><td>"""+str(FinalText)+ """</td></tr>
                #     </tbody>
                #     </table>"""
                #
                # pdf.add_page()
                # pdf.write_html(table)
                # pdf.output('simple_table_html2.pdf')

                # pdf.add_page()
                # pdf.set_font("Arial", size=12)
                # pdf.write_html(200, 10, txt=text, ln=1, align="C")
                # pdf.output("simple_demo3.pdf")

    except:
        print("Unexpected error:", sys.exc_info()[0])

read_email_from_gmail()





# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# # l = [('1-What is the temparature?-1-1', 'good'), ('2-Is having headache?-yes-2', '2'), \
# #      ('2-Is having headache?-No-2', '2'), ('3-Having any other problems?-Cough-2', '4'), \
# #      ('3-Having any other problems?-Cold-2', '4'), ('3-Having any other problems?-Headache-2', '4'), \
# #      ('3-Having any other problems?-Body pains-2', '4')]
# # medical_req_id = 'MDR-10001'
# # MedicalQuestion = []
# # emailMedicalQuestion = {}
# # for ele,value in l:
# #     ans_id = comments = ''
# #     q_id = ele.split("-")
# #
# #     if q_id[-1] == '1':
# #         comments = value
# #         ans_id = int(q_id[2])
# #         emailMedicalQuestion[q_id[1]] =value
# #     else:
# #         comments = ''
# #         ans_id = value
# #         emailMedicalQuestion[q_id[1]] = q_id[2]
# #     MedicalQuestion.append([medical_req_id, q_id[0], ans_id,comments])
# # print(MedicalQuestion)
# # print(emailMedicalQuestion)
# email = {'basicInfo':
# ['member2-102', 'MDR-10008', '6', '6', '6', '6', '6', '67', '6', '66', '6', '66', 1, 'hehhe', 27, '2020-01-06 09:04:19.484679',
# 'member2-102_MDR-10008_ Medical Request '],
#  'Question': {'What is the temparature?': '88', 'Is having headache?': 'No', 'Having any other problems?': 'Body pains'},
#  'images': ['Pictures/MDR-100080.5652241314687829.jpg', 'Pictures/MDR-100080.8775213654451804.jpg'],
#  'resultList': ['member2-102', 'MDR-10008', '6', '6', '6', '6', '6', '67', '6', '66', '6', '66', 1, 'hehhe',
#                 27, '2020-01-06 09:04:19.484679', 'member2-102_MDR-10008_ Medical Request '],'subject':'suneethaaaaa'}
#
# def sendMedicalRequest(emailMedicalRequest):
#     print(emailMedicalRequest)
#     sender_email = "suneethactel@gmail.com"
#     receiver_email = "suneetha.ankala@gmail.com"
#     password = 'cteladmin'
#
#     # Create the plain-text and HTML version of your message
#     # text
#     html = """\
#     <html>
# <head></head>
# <body>
# Basic Info:<br><br>
# """
#
#     html = html + " Temperature: -  " + str(emailMedicalRequest['basicInfo'][8]) + """<br>"""
#     html = html + " Blood Pressure: -  " + str(emailMedicalRequest['basicInfo'][9]) + """<br>"""
#     html = html + " Pulse rate: -  " + str(emailMedicalRequest['basicInfo'][10]) + """<br>"""
#     html = html + " Weight: -  " + str(emailMedicalRequest['basicInfo'][11]) + """<br>"""
#     html = html + " System: -  " + str(emailMedicalRequest['basicInfo'][12]) + """<br>"""
#     html = html + " Other Info: -  " + str(emailMedicalRequest['basicInfo'][13]) + """<br>"""
#
#
#     html = html + """</p><br>
# Informarion:<br><br>
# """
#     for f,value in emailMedicalRequest['Question'].items():
#         html = html + f + "  -  " + value + """<br>"""
#     html = html + """</p>
# <p>Regards,<br>
#  SHES Team</p>
#  </body>
#  </html>
# """
#
#
#
#     # message = MIMEMultipart("alternative", None, [MIMEText(text), MIMEText(html, 'html')])
#     message = MIMEMultipart("alternative", None, [MIMEText(html, 'html')])
#     message["Subject"] = emailMedicalRequest['subject']
#     message["From"] = sender_email
#     message["To"] = receiver_email
#
#     # Create secure connection with server and send email
#     if True:
#         try:
#             context = ssl.create_default_context()
#             with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#                 server.login(sender_email, password)
#                 server.sendmail(sender_email, receiver_email.lower(), message.as_string())
#                 server.close()
#         except smtplib.SMTPRecipientsRefused as e:
#             return "Invali Email ID"
#         # except Exception as e:
#         #     return "Something Went Wrong"
#     else:
#         return "Network Issues, Please check your Internet"
#     msgTxt = 'COoolll'
#     print(msgTxt)
#     return msgTxt
#
# sendMedicalRequest(email)
# #
# #
# # justin = "Justin"
# #
# # p = {u'Contracts that need signed by: Justin': [[u'/contracts/26203', u'/contracts/26194', u'/contracts/26199', u'/contracts/26173']]}
# #
# #
# # for a in p.keys():
# #     b = p['Contracts that need signed by: Justin']
# #     for c, d in enumerate(b):
# #         e = d
# #         html = """\
# # <html>
# # <head></head>
# # <body>
# # <p>Contracts that need signed by """ + justin  + """<br>
# # Informarion:<br>
# # """
# #         for f,value in email['Question'].items():
# #             html = html + f + "  -  " + value + """\n"""
# #         html = html + """</p>
# # </body>
# # </html>
# # """
# #
# #
# # part2 = MIMEText(html, 'html')
# #
# # print(part2)
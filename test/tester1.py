# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email import encoders
# from email.mime.base import MIMEBase
#
#
# email = {'basicInfo':
# ['member2-102', 'MDR-10008', '6', '6', '6', '6', '6', '67', '6', '66', '6', '66', 1, 'hehhe', 27, '2020-01-06 09:04:19.484679',
# 'member2-102_MDR-10008_ Medical Request '],
#  'Question': {'What is the temparature?': '88', 'Is having headache?': 'No', 'Having any other problems?': 'Body pains'},
#  'images': ['Pictures/MDR-1001.jpg', 'Pictures/company_logo.jpg'],
#  'resultList': ['member2-102', 'MDR-10008', '6', '6', '6', '6', '6', '67', '6', '66', '6', '66', 1, 'hehhe',
#                 27, '2020-01-06 09:04:19.484679', 'member2-102_MDR-10008_ Medical Request '],'subject':'mail with images'}
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
#     for filename in emailMedicalRequest['images']:
#
#         filename = "../"+filename  # In same directory as script
#
#         # Open PDF file in binary mode
#         with open(filename, "rb") as attachment:
#             # Add file as application/octet-stream
#             # Email client can usually download this automatically as attachment
#             part = MIMEBase("application", "octet-stream")
#             part.set_payload(attachment.read())
#
#         # Encode file in ASCII characters to send by email
#         encoders.encode_base64(part)
#
#         # Add header as key/value pair to attachment part
#         part.add_header(
#             "Content-Disposition",
#             f"attachment; filename= {filename}",
#         )
#
#         # Add attachment to message and convert message to string
#         message.attach(part)
#         #text = message.as_string()
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
#
#
#
# # from itertools import chain
# # import email
# # import imaplib
# # import smtplib,ssl
# # import sys
# # from datetime import datetime
# #
# # params = {
# #     'imap_ssl_host':    'imap.gmail.com',
# #     'imap_ssl_port':    993,
# #     'username':         'suneethactel@gmail.com',
# #     'password':         'cteladmin',
# #     'criteria':         {
# #                             'FROM': 'suneetha.ankala@gmail.com',
# #                             'SUBJECT': 'Email'
# #                         },
# #     'uid_max':          0,
# #     'folder':           'inbox',
# #     'start_date':       'SINCE 07-Dec-2020',
# #     'end_date':         'BEFORE 08-Jan-2020'
# # }
# #
# # def search_string(uid_max, criteria):
# #     c = list(map(lambda t: (t[0], '"' + str(t[1]) + '"'), criteria.items())) + [('UID', '%d:*' % (uid_max + 1))]
# #     return '(%s)' % ' '.join(chain(*c))
# #
# # def get_first_text_block(msg):
# #     type = msg.get_content_maintype()
# #
# #     if type == 'multipart':
# #         for part in msg.get_payload():
# #             if part.get_content_maintype() == 'text':
# #                 return bytes.decode(part.get_payload(decode=1))
# #     elif type == 'text':
# #         return bytes.decode(msg.get_payload(decode=1))
# #
# # def get_email_address(msg):
# #     # need to be updated for other email search criteria
# #     index_start = msg.index('<')
# #     index_end = msg.index('>')
# #     str = msg[index_start+1:index_end]
# #     return str
# #
# # def main(params):
# #     try:
# #         server = imaplib.IMAP4_SSL(params['imap_ssl_host'], params['imap_ssl_port'])
# #         server.login(params['username'], params['password'])
# #         server.select(params['folder'])
# #         if params['end_date'] == '':
# #             search_dates = '(' + params['start_date'] + ')'
# #         elif params['start_date'] == '':
# #             search_dates = '(' + params['end_date'] + ')'
# #         else:
# #             search_dates = '(' + params['start_date'] + ' ' + params['end_date'] + ')'
# #
# #         result, data = server.uid('search', search_dates, search_string(params['uid_max'], params['criteria']))
# #     except:
# #         print("Unexpected error:", sys.exc_info()[0])
# #         return 1
# #     else:
# #         uids = [int(s) for s in data[0].split()]
# #         if not uids:
# #             print("Emails found by search criteria: 0")
# #             return 3
# #         print("Emails found by search criteria: ", len(uids))
# #
# #         undelivered_email_list = list()
# #         for uid in uids:
# #             params['uid_max'] = max(uids)   # in case for while loop to search for new messages with sleep
# #             try:
# #                 result, emailData = server.uid('fetch', str(uid), '(RFC822)')
# #                 #result, emailData = server.fetch(str(uid), '(RFC822)')
# #             except:
# #                 print("Unexpected error:", sys.exc_info()[0])
# #                 return 2
# #             msg = email.message_from_string(emailData[0][1].decode("utf-8"))
# #             text = get_first_text_block(msg)
# #             undelivered_email_list.append(get_email_address(text))
# #
# #         undelivered_email_set = set(undelivered_email_list)
# #         dlist = {}
# #         print('\nUndelivered emails:')
# #         for x in undelivered_email_set:
# #             dlist.update({x: undelivered_email_list.count(x)})
# #         sorted_dict = {r: dlist[r] for r in sorted(dlist, key=dlist.get, reverse=True)}
# #         for k, v in sorted_dict.items():
# #             print(k, ' : ', v)
# #     finally:
# #         if 'server' in locals():
# #             server.logout()
# #     return
# #
# # if __name__ == '__main__':
# #     start_time = datetime.now()
# #     exitcode = main(params)
# #     end_time = datetime.now()
# #     print('\nDuration: {}'.format(end_time - start_time))
# #     exit(exitcode)

#
# import csv
#
# with open('../Const/ports.csv') as f:
#     reader = csv.reader(f)
#     your_list = list(reader)
#
# print(your_list)

import csv
content=[]
with open('../Const/ports.csv', encoding="utf8") as f:
    reader = csv.reader(f, skipinitialspace=True)
    # print((reader))

    rows = list(reader)
    for row in rows:
        # print(row[1])
        content.append(row[1]) #list(row[0] for i in row)

print(content)


# print(rows)
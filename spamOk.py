import random
import time
import requests
import string

class spamOk:
    def randomChar(self, length):
        return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(length))

    def getEmail(self):
        email = self.randomChar(15) + '@spamok.com'
        print(f'Your email is: {email}')
        return email

    def getInbox(self, mail):
        mail = mail.replace('@spamok.com', '')
        for i in range(30): #Refresh limit
            r = requests.get('https://api.spamok.com/v2/EmailBox/' + mail)
            if len(r.json()['mails']) > 0:
                for i in range(len(r.json()['mails'])):
                    print('Inbox: ', r.json()['mails'][i]['subject']) #Get mails subjects (Other parameters: id, fromDisplay, fromDomain, fromLocal, toDomain, toLocal, date, dateSystem, messagePreview, secondsAgo)
            print('Refreshing...')
            time.sleep(5) #Refresh per loop

obj = spamOk()
obj.getInbox(obj.getEmail())

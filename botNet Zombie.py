import pxssh
class Client:

def _init_(self,host,user,password):
self.host = host
    self.user = user
    self.password = password
    self.session = self.connect()

def connect(self):
try:
s = pxssh.pxssh()
    s.login(self.host,self.user,self.password)

    return s

except Exception, e

print(e)

    print("[*] Bağlantı Hatası")

def send_command(self,cmd):

self.session.sendline(cmd)
    self.session.prompt()
return self.session.before

def botnerCommand(command):

for client in botNet:

output = client.sen_command(command)

print ("Output from" , client.host)
print("[+]" , output)

def addClient(host, user , password):

client = Client(host , user , password)

    botNet.appent(client)

botNet = []

addClient('127.0.0.1' , 'ubuntu' , 'pass')

botnetCommand('ls -la')

:wq
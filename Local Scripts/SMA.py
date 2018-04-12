import sqlite3
from sqlite3 import Error
import paho.mqtt.publish as publish
import time
host=""
port= 
username=""
password=""
topicP1="Topic name for Power"
topicE="Topic Name for Energy"
def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
	return None
def select_Pac(conn,Pac):
	cur = conn.cursor()
	cur.execute("select {P} from SpotData order by TimeStamp desc limit 1".format(P=Pac))
	rows = cur.fetchall()
	for row in rows:
		#print(row)
		ans=row
	ans=str(ans)
	ans=ans.replace("(","")
	ans=ans.replace(")","")
	ans=ans.replace(",","")
	return ans
def send_to_cloud(Pac1,E):
	publish.single(topicP1,payload=Pac1,hostname=host,port=port,auth={'username':username,'password':password})
	publish.single(topicE,payload=E,hostname=host,port=port,auth={'username':username,'password':password})
	print("Done "+topicP1+"="+Pac1)
	print("Done"+topicE+"="+E)
def main():
	database ="/home/pi/smadata/SBFspot.db"
	conn= create_connection(database)
	while 1:
		with conn:
			Pac1=select_Pac(conn,'Pac1')
			#Pac2=select_Pac(conn,'Pac2')
			#Pac3=select_Pac(conn,'Pac3')
			E=select_Pac(conn,'ETotal')
			print(Pac1)
			print(E)
			send_to_cloud(Pac1,E)
			time.sleep(900)
if __name__=='__main__':
	main()


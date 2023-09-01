# SENDER - client

import time as t
import socket
import os


# CREATE OUR CLIENT (TCP SOCKET OBJ)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print()
print('_'*15, 'SENDING', '_'*15)
target_ip = input("\n[*] Enter Targets IP Address: ")

# TRY TO CONNECT OUR CLIENT TO THE SOCKET OF TARGET
client.connect((target_ip, 9999)) 


local_file = input("\n[*] Enter File to Send: ")


# OPEN FILE TO GRAB CONTENTS
file = open(local_file, 'rb') #where rb is reading-bytes mode

# GET DESIRED FILES ACTUAL SIZE
file_size = os.path.getsize(local_file)



# SENDING OVER NAME OF RESULTING RECEIVED FILE
sent_file = "RECEIVED_" + local_file
t.sleep(0.5)
client.send( sent_file.encode() )
t.sleep(0.5)

# TELLING FILE SIZE BEFORE SENDING FILES DATA
t.sleep(0.5)
client.send( str(file_size).encode() )
t.sleep(0.5)


# TELLING USER WHAT EXACTLY WAS SENT
print("\n[*] File Sent:", sent_file)
print('_'*40)
print()


# SENDING ALL DATA FOUND IN FILE & FINISHES WITH ENDING TAG
data = file.read()
client.sendall( data )
client.send(b"<END>")



# CLOSE FILE WHEN DONE READING/SENDING DATA
file.close()

# CLOSE CLIENT AT END ONCE SENDING COMPLETE
client.close()


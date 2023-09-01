# RECEIVER - server

import socket


# CREATE OUR SERVER (TCP SOCKET OBJ)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SERVER BINDED TO THIS SOCKET
server.bind( ("0.0.0.0", 9999) )

# SERVER LISTENS
server.listen()



# SERVER ACCEPTS CONNECTION & GRABS CLIENTS INFO
client, addr = server.accept()



# RECEIVE INFO DIRECTLY FROM CLIENT & DECODE
file_name = client.recv(1024).decode()

# PRINT FILE NAME
print()
print('_'*15, 'RECEIVING', '_'*15)
print( '\n[*] Incoming File With Name:', file_name )



# RECEIVE INFO DIRECTLY FROM CLIENT & DECODE
file_size = client.recv(1024).decode()

# PRINT FILE_SIZE
print( '\n[*] File Size:', file_size,'Bytes' )



# OPEN THE FINAL RECEIVING FILE & PREP TO WRITE TO IT
file = open(file_name, "wb")


# DATA IS STORED HERE 
file_bytes = b""


more_data = True

while( more_data == True ):

    data = client.recv(1024)

    if( file_bytes[-5:] == b"<END>" ):
        more_data = False
    else:
        file_bytes = file_bytes + data


file.write(file_bytes)

# CLOSE FILE SINCE DONE WITH IT
file.close()

# CLOSE CONNECTION SINCE FINISHED SENDING
client.close()
server.close()


print('_'*40)
print()

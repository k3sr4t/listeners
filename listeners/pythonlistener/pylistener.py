#pylistener
#
#python script for listening port
#
#

import socket
import os

version = ("v1.2")

def banner():
    banner = (f"//pylistener {version}//")
    print(banner)

#ui functions start
def select_menu():
    select="""
    1 start listener
    2 credits
    3 exit
    4/h help page
    5 close port
    """
    print(select)

def inputfunction():
    global selected
    selected = int(input("selected: "))

def ui():
    banner()
    select_menu()
    inputfunction()
    mainplace()
#ui functions end


#programs functions start
def mainplace():
    if selected == 1:
        print("starting...")
        main_starter()
    elif selected == 2:
        credits()
        os._exit(1)
    elif selected == 3:
        print("quiting...")
        os._exit(1)
    elif selected == 4 or selected == "h":
        print("help page")
        print("""
        port for the port that you want to open
        write the ip adress/ipv6 adress working with all interfaces
        enter the protocol for listening
            """)
        os._exit(1)
    elif selected == 5:
        port = int(input("enter the opened port for closing: "))
        closed_port_protocol = input("select protocol(tcp or udp) ")
        if closed_port_protocol == "tcp":
            tcp_close_port(port)
        elif closed_port_protocol == "udp":
            udp_close_port(port)
        else:
            print("an error occured")
            os._exit(1)
    else:
        print("fatal error")
        os._exit(1)

def credits():
    credits = """
    by k3sR4T
    github : https://github.com/k3sr4t/k3sr4t/blob/main/README.md
    """
    print(credits)

def main_starter():
    problem = False
    port = int(input("port: "))
    interface = input("your ip address for listening(careful with interfaces) ")

    protocoloriginal = str(input("protocol (tcp or udp): "))
    protocol = protocoloriginal.lower()
    
    if port == (""):
        print("please select port for listener")
        problem = True

    else:
        port = port
    
    
    if protocol != ("tcp") and protocol != ("udp"):
        print("invalid option for sellecting protocol")
        problem = True
    else:
        protocol = protocol


    if problem == False:
        print(f"started listener {interface} on port {port}...")
    else:
        print("an error occured")



    if protocol == "tcp":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sock.bind((interface, port))
        sock.listen(1)
        while True:
             # Accept an incoming connection
            conn, addr = sock.accept()
            print(f"Connected by {addr}")

            # Handle the connection
            while True:
                # Receive data from the client
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode()}")

                # Send a response back to the client
                conn.sendall(data)
                
    elif protocol == "udp":
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind the socket to the port
        sock.bind(("", port))

        print(f"Listening on port {port}...")

        while True:
            # Receive a UDP packet
            data, addr = sock.recvfrom(1024)
            print(f"Received from {addr}: {data.decode()}")

            # Send a response back to the client
            sock.sendto(data, addr)
            
    else:
        print("an error occured")


def udp_close_port(port):
    # Create a new socket for UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Try to bind to the port
        s.bind(('', port))
        print(f"UDP Port {port} is free, binding and closing.")
    except socket.error as e:
        print(f"UDP Port {port} is already in use: {e}")
    
    # Close the socket
    s.close()
    print(f"UDP Port {port} closed.")


def tcp_close_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.bind(('', port))
        print(f"Port {port} is free, binding and closing.")
    except socket.error as e:
        print(f"Port {port} is already in use: {e}")
    
    # Close the socket
    s.close()
    print(f"Port {port} closed.")


#programs functions end

ui()




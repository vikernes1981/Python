import socket

def internet(host="8.8.8.8", port = 53, timeout = 3):
    """
    Host : 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort : 53/tcp
    Service : domain (DNS/TCP)
    """
    print ("Checking Internet Connection")
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return "Internet is connected"
    except Exception as ex:
        print ex.message
        return False
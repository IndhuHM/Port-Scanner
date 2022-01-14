import socket
import common_ports



def get_open_ports(target, port_range, Verbose=None):
    open_ports = []
    start, end = port_range[0], port_range[-1]

    if target[0].isdigit():
      IP = True

    else: 
      IP = False

    try:
        for i in range(start, (end + 1)):
            port = i
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            s.close()
        
        if Verbose:
            if IP:
                url = socket.gethostbyaddr(target)[0]
                string = f"Open ports for {url} ({target})\nPORT     SERVICE\n"
            else:
                ip_address = str(socket.gethostbyname(target))
                string = f"Open ports for {target} ({ip_address})\nPORT     SERVICE\n"
            port_arr = []
            
            for port in open_ports:
                space_length = 9 - len(str(port))
                common_port = common_ports.ports_and_services
                port_arr.append(f"{port}{space_length * ' '}{common_port[port]}")
        
            return string + '\n'.join(port_arr)
        else: 
            return open_ports
        
    except socket.gaierror:
            return "Error: Invalid IP address"
    except socket.herror:
            return "Error: Invalid hostname"
  
    
  
    return(open_ports)
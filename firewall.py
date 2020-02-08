import csv 
import sys

class Firewall:
    #Constructor
    def __init__(self, path):
        with open(path, 'r') as f:
            reader = csv.reader(f)
            self.rules = list(reader) 

    #input: port number 
    #output: list of rules that satisfy the port condition
    def process_port(self, given_port):
        indices = []
        for i in range(0,len(self.rules)):
            currentPort = self.rules[i][2]
            #print(currentPort)
            if '-' in currentPort:
                p_range = currentPort.split('-')
                if(given_port >= int(p_range[0]) and given_port <= int(p_range[1])):
                    indices.append(i)
            else:
                if int(currentPort) == given_port:
                    indices.append(i)
        return indices
    
    #input: direction value(string), list of rules
    #output: index where direction matches, or -1 if it doesn't find a match
    def process_dir(self, given_dir, ip_list):
        #print(self.rules[index][0])
        #print(given_dir)
        dir_list = []
        for i in ip_list:
            if(self.rules[i][0].index(given_dir) != -1 ):
                return i
        return -1

    #input: protocol value(string), index
    #output: index if matches, -1 if it doesn't match
    def process_protocol(self, given_protocol, index):
        if(self.rules[index][1] == given_protocol):
            return index
        return -1

    #input: ip value (single address or a range), list of rules
    #output: list of rules that match the IP 
    def process_IP(self, given_ip, port_list):
        given_ip_val = given_ip.replace('.','')
        ip_list = []
        for i in port_list:
            currentIP = self.rules[i][3]
            #ip is a single value
            if '-' not in currentIP:
                ip_val = currentIP.replace('.','')
                if int(ip_val) == int(given_ip_val):
                    ip_list.append(i)
            #ip rule is a range
            else:
                ip_range = currentIP.split('-')
                lower = ip_range[0].replace('.','')
                upper = ip_range[1].replace('.','')
                if int(given_ip_val) >= int(lower) and int(given_ip_val) <= int(upper):
                    ip_list.append(i)             
            
        return ip_list
              
    #input: a packet 
    #output: true or false
    def accept_packet(self, direction, protocol, port, ip):
        '''
        1. find index of port
        2. find indicies of valid ip
        3. check if direction matches
        4. check if protocol matches
        '''
        port_list = self.process_port(port) #will return list of ports
        #print(port, port_list)
        ip_index = self.process_IP(ip, port_list) #will return a list of ip
        #print(ip, ip_index)
        validDir = self.process_dir(direction, port_list)
        #print('Dir: ',validDir)
        validProto = self.process_protocol(protocol, validDir) 
        #print('proto: ',validProto)
        return validDir == validProto and validDir != -1
        

if __name__ == '__main__':
    firewall = Firewall(sys.argv[1])
    #print(firewall.process_port(80))
    #print(firewall.process_IP('192.168.2.1'))
    print(firewall.accept_packet("inbound", "tcp", 80, "192.168.2.1")) 
    print(firewall.accept_packet("inbound", "udp", 53, "192.168.2.1")) 
    print(firewall.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))
    print(firewall.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
    print(firewall.accept_packet("inbound", "udp", 24, "52.12.48.92"))
    
    '''
    expected:
    true
    true
    true
    false
    false
    '''

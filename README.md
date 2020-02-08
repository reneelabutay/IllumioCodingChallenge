# IllumioCodingChallenge

For this programming challenge, I decided to implement the solution using Python. I utilized the csv package to be able to import the Firewall rules. Since time was limited, I focused on obtaining the correct solution for the basic cases, and optimize it if I had more time to spare. 

## Code Explanation
firewall.py contains the Firewall class definition, the accept_packet() function, and a few helper functions. I stored all the rules in a 2D list, where each row contains a rule and each column specifies the rule's direction, protocol, port, and IP address respectively. To implement the accept_packet() function, I needed to check if the packet matches any of the rules, so I decided to split the problem up by creating 4 helper functions to process each of the rule conditions. 

Each helper function returns a list of rule indices that the packet satisfies, then passes that list as a parameter for the next function. For example, I called the process_port() function, which takes the packet's port number, and returns a port_list, which is a list of the rules where the port number is valid. I then pass port_list into process_IP(), which takes that list and returns a narrowed-down list of rules that satisfy both the port and IP address values. It repeats this with direction and protocol, which will ultimately result in a single rule that matches this packet. 


## Testing
Although I did not have time to thoroughly test my program, I am confident that it works for the sample input and output values provided in the assignment. If more time was given, I would test more edge cases. I was also unsure if this IP address range is valid: 198.62.101.1-198.63.1.3 because it was not clear to me if each octet was compared in the range, or the overall IP address. If this range was valid, I would consider that case. 

## Optimization Opportunities
Currently, my program runs in linear time because it has to iterate through all the rules to find a match. If I had more time to think about complexity of this program, I would try to utilize a different data structure that ensure better performance and reduce the time complexity. 

Team Preferences
1. Data Team
2. Platform Team
3. Policy Team


# IllumioCodingChallenge

For this programming challenge, I decided to implement the solution using Python. I utilized the csv package to be able to import the Firewall rules. Since time was limited, I focused on obtaining the correct solution for the basic cases, and optimize it if I had more time to spare. 

## Code Explanation
firewall.py contains the Firewall class definition, the accept_packet() function, and a few helper functions. I stored all the rules in a 2D list, where each row contains a rule and each column specifies the rule's direction, protocol, port, and IP address respectively. To implement the accept_packet() function, I needed to check if the packet matches any of the rules, so I decided to split the problem up by creating 4 helper functions to process each of the rule conditions. 

Each helper function returns a list of rule indices that the packet satisfies, then passes that list as a parameter for the next function. For example, I called the process_port() function, which takes the packet's port number, and returns a port_list, which is a list of the rules where the port number is valid. I then pass port_list into process_IP(), which takes that list and returns a narrowed-down list of rules that satisfy both the port and IP address values. It repeats this and 

created 4 helper functions for 

## Testing


Optimization Opportunities

Team Preferences
1. Data Team
2. Platform Team
3. Policy Team



. Include a README file, which includes anything you’d like to communicate to the person that is reviewing your code. This may include items such as:
a. how you tested your solution
b. any interesting coding, design, or algorithmic choices you’d like to point out c. any refinements or optimizations that you would’ve implemented if you had
more time
d. anything else you’d like the reviewer to know
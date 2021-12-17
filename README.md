M/M/1 and M/M/2 Queuing simulation system:
This system is designed for customers such as banks with multiple tellers or packet switching routers to analyze the queuing system with M/M/1 and M/M/2 queuing model.

Architecture:
The system consists with 2 parts, (a) Banks with multiple tellers, and (b) Packet switching router. For each part the system will simulate both M/M/1 and M/M/2 queuing model and print the result and plot. When the user launches the system, it will require user to select which service user would like to use. After that, system will ask user to input three parameters: arrival rate(min), service rate(min), and client numbers (bank’s customer or packets).

Use case diagram:
![image](https://user-images.githubusercontent.com/93003662/146613297-ec15d690-3098-4ed8-885a-de084250b134.png)


Implementation:
Functional requirement:
•	The system should output both M/M/1 and M/M/2 simulation results
•	The system will plot customers wait time in plot

Non-functional requirement:
•	The system cannot hang with large input (e.g. 1000 customers)

Software Testing:

Test case 1:
With following input condition
Please Select the service: 1.Banks 2.Packet switching router:1
Please enter the average customers per minute：1
Please enter the average number of people served per minute：1.5
Please enter the number of customers：1000

 ![image](https://user-images.githubusercontent.com/93003662/146613014-af1f75a7-3c1b-4582-bf02-2bcd9404b944.png)
 
 Output:
 Servers : 1
 Time Between Arrivals :  1.003540208760709 
 Service Time: (1/µ) 0.7107006852820134
 Utilization (c):  0.7075900086805407
 Expected wait time in line (minute): 1.9202734000000001
 Expected time spent on the system (minute): 2.6309737999999996 
 Expected number of customers in line (Lq): 1.913119671611941
 Expected number of clients in the system (Ls): 2.6207096802924816 
 Expected number of occupied servers : 0.7075900086805407
 
 ![image](https://user-images.githubusercontent.com/93003662/146612996-ca93b228-42e4-4e84-a248-cf13e48803b8.png)
 
 Output:  
 Servers : 2 
 Time Between Arrivals :  1.003540208760709 
 Service Time: (1/µ) 0.7107006852820134 
 Utilization (c):  0.3159774355924707 
 Expected wait time in line (minute): 0.1290735 
 Expected time spent on the system (minute): 0.8397739000000001 
 Expected number of customers in line (Lq): 0.2043748532727596 
 Expected number of clients in the system (Ls): 0.836329724457701 
 Expected number of occupied servers : 0.6319548711849414


Test case 2:

With following input condition:
Please Select the service: 1.Banks 2.Packet switching router2
Please enter the average packet per minute：2
Please enter the average number of packet departed per minute：4
Please enter the number of packets：1500
![image](https://user-images.githubusercontent.com/93003662/146614108-0b9e0cbd-eab4-44e5-9658-7d601d76c6b6.png)

Output: 
 Servers : 1 
 Time Between Arrivals :  0.5158490058490683 
 Service Time: (1/µ) 0.258171044418318 
 Utilization (c):  0.49925293261216064 
 Expected wait time in line (minute): 0.30189906666666666 
 Expected time spent on the system (minute): 0.5600696666666667 
 Expected number of customers in line (Lq): 0.5842929097839182 
 Expected number of clients in the system (Ls): 1.0835458423960789 
 Expected number of occupied servers : 0.49925293261216064

![image](https://user-images.githubusercontent.com/93003662/146614275-64738659-fe14-4a1d-aae2-5f91d57029e7.png)
Output: 
 Servers : 2
 Time Between Arrivals :  0.5158490058490683 
 Service Time: (1/µ) 0.258171044418318 
 Utilization (c):  0.23545164555896225 
 Expected wait time in line (minute): 0.020599866666666668 
 Expected time spent on the system (minute): 0.27877046666666666 
 Expected number of customers in line (Lq): 0.0690538266805398 
 Expected number of clients in the system (Ls): 0.5399571177984643 
 Expected number of occupied servers : 0.4709032911179245



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
 
 

 ![image](https://user-images.githubusercontent.com/93003662/146612996-ca93b228-42e4-4e84-a248-cf13e48803b8.png)

 ![image](https://user-images.githubusercontent.com/93003662/146612965-e669808c-3282-4253-b4d6-95be14ea06c8.png)

 

![image](https://user-images.githubusercontent.com/93003662/146612900-4427091c-b4f7-4847-9b9f-53be002f9a6d.png)


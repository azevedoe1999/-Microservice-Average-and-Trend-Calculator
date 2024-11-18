Communication Contract: 

Discord: eazevedo1999 (Perfered Method of Contract) 

Email: azevedoe@oregonstate.edu

_______________________________________________________________________________________________________________________________________________________________________________________
  
I included a test.py with all the examples of how to request and retreive data.

_______________________________________________________________________________________________________________________________________________________________________________________

How to programmatically REQUEST data:

  In your main project, you would want to have the 'requests' module if your programming language does not have it installed already. 
	
  The first function 'add_workout_to_list()' requires you to send it the data information in this format:
	
    data = [
    {'name' : 'Name of Excersise', 'sets' : [{'rep' : # of reps for set i, 'weight' : weight number used in set i}, {}, ....]
    },
    {'name' : 'Name of Excersise', 'sets' : [{'rep' : # of reps for set i, 'weight' : weight number used in set i}, {}, ....]
    },
    {}...
    ] 
			
  The second and third functions 'calculate_average_weight()' and 'calculate_average_reps()' requires you to send in the name of the excersise that you want to get the results for. 
	
  For all the functions, you are required to use the requests.get() with the address/name of the function, along with any paramerters and data you want to send over. 
  
  Example:
  
    response = requests.post('http://local.host/add_workout_to_list', json=data)
    response = requests.get('http://local.host/calculate_average_weight', params={'name': name}) *same for 'calculate_average_reps()'
    response = requests.get('http://local.host/calculate_average_sets') *for last 2 functions that does not require any parameters

_______________________________________________________________________________________________________________________________________________________________________________________

How to programmatically RECEIVE data:

  Once you request data, the microservice will do its thing, and it will return the results in the response variable or whichever variable you assigned the requests.get() to. 
  
  From there, you can print out the response.json(), which will grab the contents. 

  Example:
  
     print(response.json())

_______________________________________________________________________________________________________________________________________________________________________________________

UML sequence diagram: 


![UML Sequence Diagram](https://github.com/user-attachments/assets/199e20d4-ec49-4208-a37f-96f06f056eb2)


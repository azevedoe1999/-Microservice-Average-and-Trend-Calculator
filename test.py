# test program that demonstrates that the microservice can be called and respond with data

import requests

# function that will track the workout by getting name and sets
def add_workout_to_list(data):    
    response = requests.post('http://127.0.0.1:5000/add_workout_to_list', json=data)
    print(response.json())

# will print out the average weight per set and per rep
def calculate_average_weight(name):
    response = requests.get('http://127.0.0.1:5000/calculate_average_weight', params={'name': name})
    print(response.json())

# will print out the average rep per set
def calculate_average_reps(name):
    response = requests.get('http://127.0.0.1:5000/calculate_average_reps', params={'name': name})
    print(response.json())

# will print out the average set per workout
def calculate_average_sets():
    response = requests.get('http://127.0.0.1:5000/calculate_average_sets')
    print(response.json())

# will post the user_id and will print out the trends
def identify_trends():
    response = requests.get('http://127.0.0.1:5000/identify_trends')
    print(response.json())


if __name__ == '__main__':
    data_1 = [
    {'name': 'Excersise 1',
        'sets': [{'rep': 15, 'weight': 200}]
        },
    {'name': 'Excersise 2',
        'sets': [{'rep': 4, 'weight': 150}, {'rep': 10, 'weight': 200}]
        }
]
    data_2 = [
    {'name': 'Excersise 3',
        'sets': [{'rep': 13, 'weight': 150}, {'rep': 10, 'weight': 180}]
        },
    {'name': 'Excersise 4',
        'sets': [{'rep': 7, 'weight': 100}, {'rep': 8, 'weight': 120}]
        }
]
    add_workout_to_list(data_1)
    calculate_average_weight('Excersise 1')
    calculate_average_weight('Excersise 2')
    calculate_average_reps('Excersise 1')
    calculate_average_reps('Excersise 2')
    calculate_average_sets()
    identify_trends()

    add_workout_to_list(data_2)
    calculate_average_weight('Excersise 3')
    calculate_average_weight('Excersise 4')
    calculate_average_reps('Excersise 3')
    calculate_average_reps('Excersise 4')
    calculate_average_sets()
    identify_trends()

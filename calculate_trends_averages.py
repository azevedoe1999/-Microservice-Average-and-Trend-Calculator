from flask import Flask, request, jsonify
import json
import datetime

app = Flask(__name__)

workout_log_data = []

file_path = "workout_log.txt"

# NEED TO RUN FIRST, SO THAT WHICH EVERY IS THE CURRENT DATA, WILL BE STORE ON THE TEXT FILE SO THAT THE TREND FUNCTION WILL WORK PROPERLY 
@app.route('/add_workout_to_list', methods=['POST'])
def add_workout_to_list():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%m-%d-%y %I:%M %p")
    data = request.json
    workout_log_data.append(data)
    with open(file_path, 'a') as file:
        file.write('\n')
        file.write(f"Log {formatted_datetime}:")
        file.write('\n')
        for workout in workout_log_data:
            for wo in workout:
                json.dump(wo, file)
                file.write('\n')
    return jsonify({'message': 'Workouts were added to the file'})

# CALCULATE THE AVERAGE WEIGHT PER SET AND PER REP, AND RETURN THAT INFO, AS WELL AS ADD IT TO THE FILE
@app.route('/calculate_average_weight', methods=['GET'])
def calculate_average_weight():
    name = request.args.get('name')
    total_weight = 0
    total_sets = 0
    total_reps = 0
    for workout in workout_log_data:
        for wo in workout:
            if wo['name'] == name:
                name_found = True
                for s in wo['sets']:
                    total_weight += s['weight']
                    total_sets += 1
                    total_reps += s['rep']
    if name_found:
        average_set_weight = total_weight / total_sets
        average_rep_weight = total_weight / total_reps
        with open(file_path, 'a') as file:
            file.write(f"Average set weight for {name} = {average_set_weight}")
            file.write("\n")
            file.write(f"Average rep weight for {name} = {average_rep_weight}")
            file.write('\n')
        return jsonify(message=f'The average weight per set for {name} is {average_set_weight}. The average weight per rep for {name} is {average_rep_weight}')
    else:
        return jsonify(message=f'{name} was not found in the current workout log')

# CALCULATE THE AVERAGE REPS PER SET AND RETURN THAT INFO, AS WELL AS ADD IT TO THE FILE
@app.route('/calculate_average_reps', methods=['GET'])
def calculate_average_reps():
    name = request.args.get('name')
    total_sets = 0
    total_reps = 0
    for workout in workout_log_data:
        for wo in workout:
            if wo['name'] == name:
                name_found = True
                for s in wo['sets']:
                    total_sets += 1                
                    total_reps += s['rep']
    if name_found:
        average_reps = total_reps / total_sets
        with open(file_path, 'a') as file:
            file.write(f"Average reps for {name} = {average_reps}")
            file.write('\n')
        return jsonify(message=f'The average reps per set for {name} is {average_reps}')
    else:
        return jsonify(message=f'{name} was not found in the current workout log')

# CALCULATE THE AVERAGE SETS PER WORKOUT AND RETURN THAT INFO, AS WELL AS ADD IT TO THE FILE
@app.route('/calculate_average_sets', methods=['GET'])
def calculate_average_sets():
    total_sets = 0
    total_workouts = len(workout_log_data)
    for workout in workout_log_data:
        for wo in workout:
            total_sets += len(wo['sets'])
    average_sets = total_sets / total_workouts
    with open(file_path, 'a') as file:
        file.write(f"Average sets = {average_sets}")
        file.write('\n')
    return jsonify(message=f'The average sets per workout is {average_sets}')

# COMPARE ADVERAGES IN THE TEXT FILE AND RETURN THOSE TRENDS
@app.route('/identify_trends', methods=['GET'])
def identify_trends():
    average_set_weight_data = []
    average_rep_weight_data = []
    average_reps_data = []
    average_sets_data = []

    with open(file_path, 'r') as file:
        # Gather the averages for each section and add it to a set
        for line_number, line in enumerate(file, start=1):
            if 'Average set weight for' in line and '=' in line:
                key, value = line.split('=')
                value = value.strip()
                average_set_weight_data.append((float(value)))
            elif 'Average rep weight for' in line and '=' in line:
                key, value = line.split('=')
                value = value.strip()
                average_rep_weight_data.append((float(value)))
            elif 'Average reps for' in line and '=' in line:
                key, value = line.split('=')
                value = value.strip()
                average_reps_data.append((float(value)))
            elif 'Average sets' in line and '=' in line: 
                key, value = line.split('=')
                value = value.strip()
                average_sets_data.append((float(value)))

    # get trends for average weight per set
    if len(average_set_weight_data) < 2:
        average_set_weight_trend = "Not enough data to determine a trend for the average weight per set"
    else:
        average_set_weight_change = average_set_weight_data[-1] - average_set_weight_data[0]
        if average_set_weight_change > 0:
            average_set_weight_trend = "Increased average weight per set"
        if average_set_weight_change < 0:
            average_set_weight_trend = "Decreased average weight per set"
        else:
            average_set_weight_trend = "Stable average weight per set"
    
    # get trends for average weight per rep
    if len(average_rep_weight_data) < 2:
        average_rep_weight_trend = "Not enough data to determine a trend for the average weight per rep"
    else:
        average_rep_weight_change = average_rep_weight_data[-1] - average_rep_weight_data[0]
        if average_rep_weight_change > 0:
            average_rep_weight_trend = "Increased average weight per rep"
        if average_rep_weight_change < 0:
            average_rep_weight_trend = "Decreased average weight per rep"
        else:
            average_rep_weight_trend = "Stable average weight per rep"

    # get trends for average reps per set
    if len(average_reps_data) < 2:
        average_reps_trend = "Not enough data to determine a trend for the average reps per set"
    else:
        average_reps_change = average_reps_data[-1] - average_reps_data[0]
        if average_reps_change > 0:
            average_reps_trend = "Increased average reps per set"
        if average_reps_change < 0:
            average_reps_trend = "Decreased average reps per set"
        else:
            average_reps_trend = "Stable average reps per set"

     # get trends for average sets per workout
    if len(average_sets_data) < 2:
        average_sets_trend = "Not enough data to determine a trend for the average sets per workout"
    else:
        average_sets_change = average_sets_data[-1] - average_sets_data[0]
        if average_sets_change > 0:
            average_sets_trend = "Increased average sets per workout"
        if average_sets_change < 0:
            average_sets_trend = "Decreased average sets per workout"
        else:
            average_sets_trend = "Stable average sets per workout"
        
    return jsonify(f'The trend for the average weight per set: {average_set_weight_trend}\n'
                f'The trend for the average weight per rep: {average_rep_weight_trend}\n'
                f'The trend for the average reps per set: {average_reps_trend}\n'
                f'The trend for the average sets per workout: {average_sets_trend}')      

if __name__ == '__main__':
    app.run(debug=True)

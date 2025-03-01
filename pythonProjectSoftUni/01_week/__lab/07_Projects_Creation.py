architect_name = input()
project_numbers = int(input())

project_time = project_numbers * 3

data = 'The architect ' + architect_name + ' will need ' + str(project_time) + ' hours to complete ' + str(project_numbers) + ' project/s.'
print(data)
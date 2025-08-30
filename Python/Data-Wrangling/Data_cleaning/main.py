from datetime import datetime

zipped_data = [[None,None,['Month','12'],['Day','12'],['Year','2024'],None,None,None,['Hour','15'],['Minute','30']]]

starting_string = '{}/{}/{} {}:{}'.format(
      zipped_data[0][2][1],  #Month
            zipped_data[0][3][1],  #Day
            zipped_data[0][4][1],  #Year
            zipped_data[0][8][1],  #Hour
            zipped_data[0][9][1],  #Minute
)
print(f'Given time {starting_string}')
start_time = datetime.strptime(starting_string,'%m/%d/%Y %H:%M')
print(f'Converted Time :{start_time}')
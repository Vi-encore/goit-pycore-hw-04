def total_salary(path):
  try: 
    with open(path, 'r', encoding='utf-8') as fh:
      salaries = []

      for line in fh:
        try:
          _, salary = line.strip().split(',')
          salaries.append(int(salary))
        except ValueError as error:
          print(f'Невірний формат рядка: {line.strip()}')
          # salaries.append(0) #result will be incorrect in the end (more employees than money)
          # pass #again incorrect results

          return(error) #will break def
        
      total = sum(salaries) 
      average = total//len(salaries) if salaries else 0

      return total, average
    
    
      # return(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {total//num_of_employees}")
    
  except FileNotFoundError as error:
    print('Такого файлу не існує!')
    return(error)
  except IOError as error:
    print('Помилка читання файлу!')
    return(error)





# path = 'task_1\\salary.txt' #relative
total, average = total_salary("task_1\\salary.txt")

# print(total_salary(path))
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

#you can swap all uncommented lines for commented => will still work 

#because uncommented lines cause 2 errors - one from try...except block

#Other one will be TypeError - because of return error inside for cycle 
#If I swap that return with pass or append => result will be incorrect, so I decided to break function instead
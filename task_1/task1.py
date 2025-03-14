def total_salary(path):
  try: 
    with open(path, 'r', encoding='utf-8') as fh:
      total = 0
      num_of_employees = 0;

      for line in fh:
        total += int(line.strip().split(',')[1])
        num_of_employees += 1
    
      average = total//num_of_employees
      return(total, average)
      # return(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {total//num_of_employees}")
    
  except ZeroDivisionError as error :
    print('Переданий файл пустий!')
    return(error)
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
#Other one will be TypeError  
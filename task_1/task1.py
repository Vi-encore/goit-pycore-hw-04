def total_salary(path):
  try: 
    with open(path, 'r', encoding='utf-8') as fh:
      total_sum = 0
      num_of_employees = 0;

      for line in fh:
        total_sum += int(line.strip().split(',')[1])
        num_of_employees += 1
    
      return(f"Загальна сума заробітної плати: {total_sum}, Середня заробітна плата: {total_sum//num_of_employees}")
    
  except ZeroDivisionError as error :
    print('Переданий файл пустий!')
    return(error)
  except FileNotFoundError as error:
    print('Такого файлу не існує!')
    return(error)
  except IOError as error:
    print('Помилка читання файлу!')
    return(error)



# path = 'D:\PROJECTS\NEOVERSITY\goit-pycore-hw-04\task_1\salary.txt' #absolute
path = 'task_1\\salary.txt' #relative

print(total_salary(path))

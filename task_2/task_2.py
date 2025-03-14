def get_cats_info(path):
  try:
    with open(path, 'r', encoding='utf-8') as fh:
      result = []
      for line in fh:
        try:
          cat_id, name, age = line.strip().split(',')
          result.append({'id': cat_id, 'name': name, 'age': age})

        except ValueError:
          return(f'Невірний формат рядку {line.strip()}')
      return result
    
  except FileNotFoundError as error:
    print('Такого файлу не існує!')
    return(error)
  except IOError as error:
    print('Помилка читання файлу!')
    return(error)

path = 'task_2\\cat_info.txt' #relative

cats_info = get_cats_info(path)
print(cats_info)
from colorama import Fore, Style, init
import sys
from pathlib import Path

init()

def create_mock(directory_path, indent_lvl = 0):
  try:
    for path in directory_path.iterdir():
      indent = ' ' * 4 * indent_lvl
      if Path(path).is_dir():
        print(f'{Fore.BLUE}{indent}{Path(path).name}/{Style.RESET_ALL}')
        create_mock(Path(path), indent_lvl + 1)
      else:
        print(f'{indent}{Fore.GREEN}{Style.BRIGHT}{Path(path).name}{Style.RESET_ALL}')
  except PermissionError:
    print(f'{Fore.RED}{Style.BRIGHT}Доступ до директорії {directory_path} заборнено!{Style.RESET_ALL}')


def main():
  if len(sys.argv) != 2:
    print(f'{Fore.LIGHTRED_EX}{Style.BRIGHT}Використання: python task3.py /шлях/до/директорії{Style.RESET_ALL}')
    sys.exit(1)

  directory_path = Path(f'/{sys.argv[1]}') if not sys.argv[1].startswith('\\') else Path(sys.argv[1]).resolve() #will work correctly if input is "dir\dir"

  if not directory_path.exists():
    print(f'{Fore.RED}{Style.BRIGHT}Даний шлях не існує!{Style.RESET_ALL}')
    sys.exit(1)

  if directory_path.is_file():
    print(f'{Fore.YELLOW}{Style.BRIGHT}Даний шлях веде до файлу {directory_path.name}{Style.RESET_ALL}')
    sys.exit(1)
  
  # if not directory_path.is_dir():  #if do not want to display filename if path was for it
  #   print(f'{Fore.RED}{Style.BRIGHT}Даний шлях не є директорією!{Style.RESET_ALL}')
  #   sys.exit(1)

  create_mock(directory_path)


if __name__ == '__main__':
  main()
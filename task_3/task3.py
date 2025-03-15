from colorama import Fore, Back, Style
import sys
from pathlib import Path


def create_mock(directory_path, indent_lvl = 0):
  indent = ' ' * 4 * indent_lvl
  for path in directory_path.iterdir():
    if Path(path).is_dir():
      print(f'{Fore.BLUE}{indent}{Path(path).name}/{Style.RESET_ALL}')
      create_mock(Path(path), indent_lvl + 1)
    else:
      print(f'{indent}{Fore.GREEN}{Style.BRIGHT}{Path(path).name}{Style.RESET_ALL}')


def main():
  if len(sys.argv) != 2:
    print(f'{Fore.RED}Використання: python task3.py /шлях/до/директорії{Style.RESET_ALL}')
    sys.exit(1)

  directory_path = Path(f'/{sys.argv[1]}') if not sys.argv[1].startswith('\\') and not Path(sys.argv[1]).is_absolute() else Path(sys.argv[1])

  if not directory_path.exists():
    print(f'{Fore.RED}{Style.BRIGHT}Даний шлях не існує!{Style.RESET_ALL}')
    sys.exit(1)
  
  if not directory_path.is_dir():
    print(f'{Fore.RED}{Style.BRIGHT}Даний шлях не є директорією!{Style.RESET_ALL}')
    sys.exit(1)

  create_mock(directory_path)


if __name__ == '__main__':
  main()
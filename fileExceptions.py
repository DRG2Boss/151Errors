def load_data(file_name):
    try:
        file = open(file_name, 'a')
    except FileNotFoundError:
        print(f"{file_name} was not found, giving up")
        return
    except PermissionError:
        print(f"We couldn't read {file_name}")
        return
    else:
        file_lines = file.readlines()
        file.close()
        return file_lines
    finally:
        print("We do this no matter what")

def main():
    data = load_data("WordFile.txt")
    if not data:
        exit(0)
    for country in data:
        print(country)

main()
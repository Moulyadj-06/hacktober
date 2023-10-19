import os

def check_file_permissions(file_path):
    if not os.path.exists(file_path):
        print(f" The file: '{file_path}' Does not exists.")
        return
    
    try:
        mode = os.stat(file_path).st_mode
        permissions = {
            'readable': bool(mode & 0o400),
            'writable': bool(mode & 0o200),
            'executable': bool(mode & 0o100)
            }
        print(f" Permissions for: '{file_path}':")
        print(f" Readable: {permissions['readable']}")
        print(f" writable: {permissions['writable']}")
        print(f" Executable: {permissions['executable']}")
    except OSError as e:
        print(f"Error: {e}")
        
if __name__==" __main__":
    file_path = input("enter the file path")
    check_file_permissions(file_path)
      

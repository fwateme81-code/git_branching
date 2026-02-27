from auth.login import login
from auth.logout import logout
from ui.header import header

def main():
    print("=== Application Started ===")
    header()
    login()
    logout()

if __name__ == "__main__":
    main()
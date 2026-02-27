from auth.login import login
from auth.logout import logout

def main():
    print("=== Application Started ===")
    login()
    logout()

if __name__ == "__main__":
    main()
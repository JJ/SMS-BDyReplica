
from gestorhtml import *





def main():
    from paste import httpserver
    app = Server()
    ap=httpserver.serve(app, host='127.0.0.1', port='8000')

if __name__ == '__main__':
    main()
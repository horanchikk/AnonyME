import multiprocessing
from time import sleep
from sys import platform
from subprocess import PIPE, call
from psutil import process_iter


if platform == 'win32':
    python = 'python'
    pip = 'pip'
else:
    python = 'python3.10'
    pip = 'pip3.10'

def initThread(typeserver):
    match typeserver:
        case "uvicorn":
            call(f'cd backend && {pip} install -r requirements.txt && uvicorn main:app --reload', stdout=PIPE, shell=True)
            while True:
                pass

        case "npm":
            call("cd frontend && yarn && yarn dev", shell=True)
            while True:
                pass

g = multiprocessing.Process(target=initThread, args=("npm", ))
j = multiprocessing.Process(target=initThread, args=("uvicorn", ))
g.daemon = True
j.daemon = True


def server(args):
    match args:
        case 'kill':
            g.kill()
            j.kill()
            
            for proc in process_iter():
                if proc.name() == 'node.exe':
                    proc.kill()
                elif proc.name == 'node':
                    proc.kill()
        case 'run':
            g.start()
            j.start()
            while True:
                sleep(10000)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    try:
        server('run')
    except KeyboardInterrupt or SystemExit:
        server('kill')
        print('\nserver has been stopped')
    except Exception as e:
        server('kill')
        print("\n" + str(e))
        print('\nserver has been stopped')
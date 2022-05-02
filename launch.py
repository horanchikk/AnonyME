from multiprocessing import Process
from sys import platform
from os import system as call
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--front', help='launch command for npm (run or yarn)', default='yarn')
parser.add_argument('--b-host', help='backend launch host, 127.0.0.1 for example', default='127.0.0.1')
parser.add_argument('--b-port', help='backend launch port, 8000 for example', default=8000)
args = parser.parse_args()


if platform == 'win32':
    python = 'python'
    pip = 'pip'
else:
    python = 'python3'
    pip = 'pip3'


def backend():
    call(
        f'cd backend && '
        f'{pip} install -r requirements.txt && '
        f'uvicorn main:app --reload --host {args.b_host} --port {args.b_port}',
    )


def frontend():
    command = 'npm run dev' if args.front == 'run' else 'yarn && yarn dev'
    call(f'cd frontend && {command}')


if __name__ == '__main__':
    back = Process(target=backend, daemon=True)
    front = Process(target=frontend, daemon=True)
    back.start()
    front.start()
    back.join()
    front.join()

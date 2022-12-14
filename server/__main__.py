import argparse
import configparser
import os
import socket
from multiprocessing import Process
import typing

import server.object as obj
import server.http as csehttp


def main():
    """Main function for running the whole program, reads the port
       commandline argument, then runs the server until given Ctrl + c"""

    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'config.ini')
    config = configparser.ConfigParser()
    config.read(config_path)

    parser = argparse.ArgumentParser(description=config.get('cli',
                                                            'description'))
    parser.add_argument('port', type=int, help="""Port server to receive \
                        http requests on.""")
    args = parser.parse_args()

    port = args.port
    processes = []
    try:
        run_server(port, processes)
    except KeyboardInterrupt:
        for p in processes:
            p.kill()
        exit(0)


def run_server(port: int, processes: typing.List[Process]):
    """Create the listening socket, and passes any requests to an
       independent process to handle it, allowing requests to be
       quickly handled and concurrently processed."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen()
        s.settimeout(2)
        while True:
            try:
                connection, addr = s.accept()
                proc = Process(target=request_handler, args=(connection,))
                proc.start()
                processes.append(proc)
            except TimeoutError:
                # Periodically during timeouts, no request made yet, clean out
                # dead processes.
                dead_processes = [p for p in processes if not p.is_alive()]
                for p in dead_processes:
                    p.kill()
                    processes.remove(p)
                pass


def request_handler(conn):
    """Target function used for creating process to handle request."""
    csehttp.HttpController(obj.ObjectRepo()).process_request(conn)


if __name__ == '__main__':
    main()

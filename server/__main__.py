import argparse
import configparser
import os


def main():
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
    print(port)


if __name__ == '__main__':
    main()

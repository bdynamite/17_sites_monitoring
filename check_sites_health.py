import subprocess
import requests
import argparse


def load_urls4check(site_name):
    http_status = is_server_respond_with_200(site_name)
    expiration_date = get_domain_expiration_date(site_name)
    return {'http_status': http_status, 'exp_date': expiration_date}


def is_server_respond_with_200(site_name):
    url = 'http://{}'.format(site_name)
    return requests.get(url).status_code


def get_domain_expiration_date(site_name):
    data_string = subprocess.check_output('whois {}'.format(site_name)).decode()
    registry_date_pos = data_string.find('Registry Expiry Date: ') + 22
    return data_string[registry_date_pos:registry_date_pos + 10]


def get_file_path():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to file', type=str)
    return parser.parse_args().path


def get_urls(path):
    with open(path, 'r') as file_urls:
        return [x.split() for x in file_urls.readlines()]


def print_status(site, status_data):
    print('{} monitoring:'.format(site))
    print(' '*4 + 'http status: {}'.format(status_data['http_status']))
    print(' '*4 + 'expiry date: {}'.format(status_data['exp_date']))


def main():
    file_path = get_file_path()
    names_list = get_urls(file_path)
    for site_name in names_list:
        response = load_urls4check(site_name[0])
        print_status(site_name[0], response)

if __name__ == '__main__':
    main()

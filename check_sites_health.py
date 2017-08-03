import subprocess
import requests


def load_urls4check(site_name):
    http_status = is_server_respond_with_200(site_name)
    expiration_date = get_domain_expiration_date(site_name)
    return http_status, expiration_date


def is_server_respond_with_200(site_name):
    url = 'http://{}'.format(site_name)
    return requests.get(url).status_code


def get_domain_expiration_date(site_name):
    data_string = subprocess.check_output('whois {}'.format(site_name)).decode()
    registry_date_pos = data_string.find('Registry Expiry Date: ') + 22
    return data_string[registry_date_pos:registry_date_pos + 10]


def get_file_path():
    return input('input urls file path: ')


def get_urls(path):
    with open(path, 'r') as file_urls:
        return [x[:-1] for x in file_urls.readlines()]


def print_status(site, status_data):
    print('{} monitoring:'.format(site))
    print(' '*4 + 'http status: {}'.format(status_data[0]))
    print(' '*4 + 'expiry date: {}'.format(status_data[1]))


def main():
    file_path = get_file_path()
    names_list = get_urls(file_path)
    for site_name in names_list:
        response = load_urls4check(site_name)
        print_status(site_name, response)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Gets the latitude and longitude from ipstack for an IP address passed in as an argument.
"""
import argparse
import configparser
import ipaddress
import sys
import requests


def is_ip_valid(ip_adr):
    """
    ip_adr: ip address
    Checks whether an ip address is valid
    """
    try:
        ipaddress.ip_address(ip_adr)
    except ValueError:
        return False
    return True


def is_key_present(conf):
    """
    conf: configuration object
    Checks whether an API key is present in the configuration
    """
    try:
        conf["ipstack"]["api_key"]
    except KeyError:
        return False
    return True


parser = argparse.ArgumentParser(
    description="Gets the lat and long of the ip provided from IPstack"
)
parser.add_argument(
    "--ip",
    dest="ip",
    default="8.8.8.8",
    required=False,
    help="The IP address that will be looked up",
)
parser.add_argument(
    "--key_file",
    dest="key_file",
    default="ipstack.py",
    required=False,
    help="The filename where the API key is stored",
)
args = parser.parse_args()
if not is_ip_valid(args.ip):
    print(f"Invalid IP address:{args.ip}")
    sys.exit()
config = configparser.ConfigParser()
config.read(args.key_file)
if not is_key_present(config):
    print("API key not found.")
    sys.exit()
url = f"http://api.ipstack.com/{args.ip}?access_key={config['ipstack']['api_key']}"
res = requests.post(url)
res_dict = res.json()
if res_dict.get("latitude"):
    print(f"lat:{res_dict['latitude']},long:{res_dict['longitude']}")
elif res_dict.get("error"):
    print(
        f"error code:{res_dict['error']['code']}\nerror type:{res_dict['error']['type']}"
    )
else:
    print("Something went wrong. No data found for the IP address.")

""" Copyright (c) 2024 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at https://developer.cisco.com/docs/licenses.
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

class Meraki:
    def __init__(self):
        self.meraki_api_key = os.getenv('MERAKI_API_KEY')
        self.base_url = "https://api.meraki.com/api/v1"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Cisco-Meraki-API-Key": self.meraki_api_key
        }

    def get_organizations(self):
        url = f"{self.base_url}/organizations"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_organization_id(self, organization_name):
        url = f"{self.base_url}/organizations"
        organizations = requests.get(url, headers=self.headers).json()
        for organization in organizations:
            if organization['name'] == organization_name:
                organization_id = organization['id']
        return organization_id
    
    def get_networks(self, organization_id):
        url = f"{self.base_url}/organizations/{organization_id}/networks"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_network_id(self, organization_id, network_name):
        url = f"{self.base_url}/organizations/{organization_id}/networks"
        networks = requests.get(url, headers=self.headers).json()
        for network in networks:
            if network['name'] == network_name:
                network_id = network['id']
        return network_id
    
    def get_inventory_devices(self, organization_id, query=None):
        url = f"{self.base_url}/{organization_id}/inventory/devices"
        response = requests.get(url, headers=self.headers).json()
        return response

    def get_network_devices(self, network_id):
        url = f"{self.base_url}/networks/{network_id}/devices"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_device_serial(self, network_id, device_name):
        url = f"{self.base_url}/networks/{network_id}/devices"
        devices = requests.get(url, headers=self.headers).json()
        for device in devices:
            if device['name'] == device_name:
                serial_number = device['serial']
        return serial_number
    
    def remove_network_devices(self, network_id, serial_number):
        url = f"{self.base_url}/networks/{network_id}/devices/remove"
        payload = { "serial": serial_number }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 204:
            print(f"Successfully removed network device with serial number {serial_number}")
        else:
            print(f" Error removing device. HTTP response {response.status_code}: {response.reason}")
    
    def release_from_organization_inventory(self, organization_id, serial_number):
        url = f"{self.base_url}/organizations/{organization_id}/inventory/release"
        payload = { "serials": [serial_number] }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            print(f"Successfully released device with serial number {serial_number} from organization")
        else:
            print(f"Error releasing device from organization. HTTP response {response.status_code}: {response.reason}")
    
    def claim_network_devices(self, network_id, serial_number):
        url = f"{self.base_url}/networks/{network_id}/devices/claim"
        payload = { "serials": [serial_number] }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            print(f"Successfully claimed device with serial number {serial_number}")
        else:
            print(f"Error claiming device. HTTP response {response.status_code}: {response.reason}")
    
    def update_device(self, serial_number, payload):
        url = f"{self.base_url}/devices/{serial_number}"
        response = requests.put(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            print(f"Successfully updated device with serial number {serial_number}")
        else:
            print(f"Error updating device. HTTP response {response.status_code}: {response.reason}")
    
    def get_network_appliance_ports(self, network_id):
        url = f"{self.base_url}/networks/{network_id}/appliance/ports"
        response = requests.get(url, headers=self.headers).json()   
        return response
    
    def update_network_appliance_port(self, network_id, port_id, payload):
        url = f"{self.base_url}/networks/{network_id}/appliance/ports/{port_id}"
        response = requests.put(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            print(f"Successfully updated network appliance port {port_id}")
        else:
            print(f"Error updating network appliance port. HTTP response {response.status_code}: {response.reason}")
    
    def get_network_appliance_ssids(self, network_id):
        url = f"{self.base_url}/networks/{network_id}/appliance/ssids"
        response = requests.get(url, headers=self.headers).json()
        return response
    
    def update_network_appliance_ssid(self, network_id, ssid_number, payload):
        url = f"{self.base_url}/networks/{network_id}/appliance/ssids/{ssid_number}"
        response = requests.put(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            print(f"Successfully updated network appliance SSID {ssid_number}")
        else:
            print(f"Error updating network appliance SSID. HTTP response {response.status_code}: {response.reason}")

    def get_device_management_interface(self, serial_number):
        url = f"{self.base_url}/devices/{serial_number}/managementInterface"
        response = requests.get(url, headers=self.headers).json()
        return response
    
    def update_device_management_interface(self, serial_number, payload):
        url = f"{self.base_url}/devices/{serial_number}/managementInterface"
        response = requests.put(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            print(f"Successfully updated management interface from device with serial number {serial_number}")
        else:
            print(f"Error updating device management interface. HTTP response {response.status_code}: {response.reason}")
    
    def get_device_switch_ports(self, serial_number):
        url = f"{self.base_url}/devices/{serial_number}/switch/ports"
        response = requests.get(url, headers=self.headers).json()
        return response
    
    def update_device_switch_ports(self, serial_number, port_id, payload):
        url = f"{self.base_url}/devices/{serial_number}/switch/ports/{port_id}"
        response = requests.put(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            print(f"Successfully updated device switch port {port_id}")
        else:
            print(f"Error updating switch ports. HTTP response {response.status_code}: {response.reason}")
    
    def get_network_wireless_ssids(self, network_id):
        url = f"{self.base_url}/networks/{network_id}/wireless/ssids"
        response = requests.get(url, headers=self.headers).json()
        return response
        
    def update_network_wireless_ssids(self, network_id, ssid_number, payload):
        url = f"{self.base_url}/networks/{network_id}/wireless/ssids/{ssid_number}"
        response = requests.put(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            print(f"Successfully updated wireless network SSID {ssid_number}")
        else:
            print(f"Error updating wireless network SSIDs. HTTP response {response.status_code}: {response.reason}")

    def export_device_configurations(self, source_organization_id, source_network_name, source_network_id):
        source_devices = self.get_network_devices(source_network_id)
        network_record = {
        'name': source_network_name,
        'network_id': source_network_id,
        'organization_id': source_organization_id,
        'devices': []
        }
        for device in source_devices:
            device_record = {
                'serial': device['serial'],
                'model': device['model']
            }
            if 'lat' in device:
                device_record['lat'] = device['lat']
            if 'lng' in device:
                device_record['lng'] = device['lng']
            if 'address' in device:
                device_record['address'] = device['address']
            if 'name' in device:
                device_record['name'] = device['name']
            if 'notes' in device:
                device_record['notes'] = device['notes']

            device_management_interface = self.get_device_management_interface(device['serial'])
            if not device_management_interface is None:
                device_record['managementInterface'] = device_management_interface

            if device['model'].startswith('MX'):
                network_appliance_ports = self.get_network_appliance_ports(source_network_id)
                if not network_appliance_ports is None:
                    device_record['appliancePorts'] = network_appliance_ports
                network_appliance_ssids = self.get_network_appliance_ssids(source_network_id)
                if not network_appliance_ssids is None:
                    device_record['applianceSsids'] = network_appliance_ssids
            elif device['model'].startswith('MS'):
                device_switch_ports = self.get_device_switch_ports(device['serial'])
                if not device_switch_ports is None:
                    allCleanPorts = []
                    for port in device_switch_ports:
                        singleCleanPort = {}
                        for attr in port:
                            if attr != 'linkNegotiationCapabilities':
                                singleCleanPort[attr] = port[attr]
                        allCleanPorts.append(singleCleanPort)
                    device_record['switchPorts'] = allCleanPorts
            elif device['model'].startswith('MR'):
                network_wireless_ssids = self.get_network_wireless_ssids(source_network_id)
                if not network_wireless_ssids is None:
                    device_record['wirelessSsids'] = network_wireless_ssids

            network_record['devices'].append(device_record)
        return network_record
    
    def create_configuration_file(self, file_name, network_record):
        try:
            f = open(file_name, 'w')
            json.dump(network_record, f, indent=4)
            f.close()
            print(f"Successfully saved {file_name}")
        except:
            print(f"Unable to write to file {file_name}")

    def open_configuration_file(self, file_name):
        try:
            f = open(file_name, 'r')
            network_configuration = json.load(f)
            f.close()
        except:
            print(f"Unable to read file {file_name}")
        return network_configuration
    
    def import_device_configurations(self, network_configuration, destination_network_id):
        for device in network_configuration['devices']:
            payload = {}
            if 'name' in device:
                payload['name'] = device['name']
            if 'address' in device:
                payload['address'] = device['address']
            if 'lat' in device:
                payload['lat'] = device['lat']
                payload['moveMapMarker'] = True
            if 'lng' in device:
                payload['lng'] = device['lng']
                payload['moveMapMarker'] = True
            if 'notes' in device:
                payload['notes'] = device['notes']
            if payload != {}:
                update = self.update_device(device['serial'], payload)

            if 'managementInterface' in device:
                update_management_interface = self.update_device_management_interface(device['serial'], device['managementInterface'])

            if 'appliancePorts' in device:
                for port in device['appliancePorts']:
                    appliance_port_payload = {}
                    for attr in port:
                        if attr != 'number':
                            appliance_port_payload[attr] = port[attr]
                    update_appliance_port =  self.update_network_appliance_port(destination_network_id, port['number'], appliance_port_payload)

            if 'applianceSsids' in device:
                for ssid in device['applianceSsids']:
                    appliance_ssid_payload = {}
                    for attr in ssid:
                        if attr != 'number':
                            appliance_ssid_payload[attr] = ssid[attr]
                    update_appliance_ssid = self.update_network_appliance_ssid(destination_network_id, ssid['number'], appliance_ssid_payload)

            if 'switchPorts' in device:
                for port in device['switchPorts']:
                    switch_port_payload = {}
                    for attr in port:
                        if attr != 'portId':
                            switch_port_payload[attr] = port[attr]
                    update_switch_port = self.update_device_switch_ports(device['serial'], port['portId'], switch_port_payload)

            if 'wirelessSsids' in device:
                for ssid in device['wirelessSsids']:
                    wireless_ssid_payload = {}
                    for attr in ssid:
                        if attr != 'number':
                            wireless_ssid_payload[attr] = ssid[attr]
                    update_wireless_ssids = self.update_network_wireless_ssids(destination_network_id, ssid['number'], wireless_ssid_payload)
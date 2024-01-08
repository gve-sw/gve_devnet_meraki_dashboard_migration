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

from meraki import Meraki
from dotenv import load_dotenv
import os

source_organization_name = os.getenv('SOURCE_ORGANIZATION_NAME')

source_network_name = os.getenv('SOURCE_NETWORK_NAME')

# Instantiate Meraki class from meraki.py
meraki = Meraki()

source_organization_id = meraki.get_organization_id(source_organization_name)

source_network_id = meraki.get_network_id(source_organization_id, source_network_name)

source_devices = meraki.get_network_devices(source_network_id)

# Export Device Configurations
network_configuration = meraki.export_device_configurations(source_organization_id, source_network_name, source_network_id)

# Save export to file name "configuration"
file_name = "configuration"
meraki.create_configuration_file(file_name, network_configuration)

# Remove and unclaim devices
for device in source_devices:
    remove = meraki.remove_network_devices(source_network_id, device['serial'])
    unclaim = meraki.release_from_organization_inventory(source_organization_id, device['serial'])

print("Released devices may take several minutes to be available for claiming in a different organization. This is normal")
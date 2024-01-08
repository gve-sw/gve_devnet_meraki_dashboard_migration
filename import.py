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

destination_organization_name = os.getenv('DESTINATION_ORGANIZATION_NAME')

destination_network_name = os.getenv('DESTINATION_NETWORK_NAME')

# Instantiate Meraki class from meraki.py
meraki = Meraki()

destination_organization_id = meraki.get_organization_id(destination_organization_name)

destination_network_id = meraki.get_network_id(destination_organization_id, destination_network_name)

# Open configuration file
file_name = "configuration"
network_configuration = meraki.open_configuration_file(file_name)

# Import device configurations
meraki.import_device_configurations(network_configuration, destination_network_id)
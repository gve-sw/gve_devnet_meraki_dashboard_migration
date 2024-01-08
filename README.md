# gve_devnet_meraki_dashboard_migration
The purpose of this sample code is to allow customers to migrate one Meraki dashboard to another. The scripts pull the current devices and their configurations and import the devices configurations to the destination Meraki dashboard. The Python script export.py pulls the current devices and their configurations and saves the device configurations as a JSON object. Then the Python scripts claim.py and import.py claim the devices and import them, which moves the devices from one dashboard to another. The prupose of splitting the code up into multiple files is because the time required for devices to be unclaimed and reclaimed in Meraki dashboard can take many minutes.


## Contacts
* Vanessa Rottke

## Solution Components
* Meraki

## Workflow
![/IMAGES/workflow.png](/IMAGES/workflow.png)

## Prerequisites
#### Meraki API Keys
In order to use the Meraki API, you need to enable the API for your organization first. After enabling API access, you can generate an API key. Follow these instructions to enable API access and generate an API key:
1. Login to the Meraki dashboard
2. In the left-hand menu, navigate to `Organization > Settings > Dashboard API access`
3. Click on `Enable access to the Cisco Meraki Dashboard API`
4. Go to `My Profile > API access`
5. Under API access, click on `Generate API key`
6. Save the API key in a safe place. The API key will only be shown once for security purposes, so it is very important to take note of the key then. In case you lose the key, then you have to revoke the key and a generate a new key. Moreover, there is a limit of only two API keys per profile.

> For more information on how to generate an API key, please click [here](https://developer.cisco.com/meraki/api-v1/#!authorization/authorization). 

> Note: You can add your account as Full Organization Admin to your organizations by following the instructions [here](https://documentation.meraki.com/General_Administration/Managing_Dashboard_Access/Managing_Dashboard_Administrators_and_Permissions).


## Installation/Configuration
1. Clone this repository with `git clone [repository name]`. To find the repository name, click the green `Code` button above the repository files. Then, the dropdown menu will show the https domain name. Click the copy button to the right of the domain name to get the value to replace [repository name] placeholder.

2. Access the downloaded folder:
  ```cd gve_devnet_meraki_dashboard_migration```

3. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).

4. Install the requirements with `pip3 install -r requirements.txt`

5. Fill in your variables in the **.env** file:
  ```  
    MERAKI_API_KEY="[Add Meraki API Key]"
    SOURCE_ORGANIZATION_NAME="[Add source organization name]"
    DESTINATION_ORGANIZATION_NAME="[Add destination organization name]"
    SOURCE_NETWORK_NAME="[Add source network name]"
    DESTINATION_NETWORK_NAME="[Add destination network name]"
  ```

## Usage
Run the file export.py:
  ```
  $ python3 export.py
  ```

Wait at least 5-10 minutes so that the devices are reasy to be claimed again. Then run the script claim.py.
  ```
  $ python3 claim.py
  ```

Wait at least another 5-10 minutes so that the devices have been claimed to the network. Then run the script import.py.
  ```
  $ python3 import.py
  ```

# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
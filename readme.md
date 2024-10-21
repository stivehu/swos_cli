### SWOS CLI - README

#### Overview of MikroTik SwOS and Its Limitations

MikroTik's SwOS is a lightweight and straightforward operating system designed for managing switches. It provides a web-based interface for tasks like configuring VLANs, managing ports, and monitoring the switch's performance. However, using the SwOS web interface presents several challenges, especially in environments that require frequent, automated, or scriptable management actions:

1. **Manual Interaction**: The web interface is purely manual, requiring point-and-click operations, which can be slow for power users and admins managing multiple devices.
2. **No CLI Support**: Unlike other switch operating systems, such as Cisco's IOS, SwOS lacks a Command Line Interface (CLI), limiting automation, customization, and integration with network management scripts.
3. **HTTP Authentication**: The system relies on basic or digest HTTP authentication, which must be managed manually through the browser.
4. **No Easy Bulk Operations**: Tasks like retrieving MAC address tables or checking interface statuses have to be done one at a time through the web interface, making bulk operations cumbersome.

This project aims to solve these issues by introducing a CLI for MikroTik SwOS, which brings the efficiency and flexibility of command-line management to SwOS users.

---

#### Project Description

The **SWOS CLI** is a command-line tool that allows users to interact with MikroTik SwOS via HTTP requests, mimicking the functionality of a CLI that many network engineers are accustomed to, particularly from Cisco devices. This CLI enables users to run commands to gather information, like MAC address tables, and perform various management tasks through a familiar command structure.

---

#### Features

- **Cisco-like Commands**: The CLI adopts a Cisco-style syntax, making it easier for network admins to use without needing to learn a new interface.
- **`show mac address-table` Command**: You can retrieve MAC address table data in various modes (all, count, VLAN, MAC, interface) and filter the output.
- **HTTP Digest Authentication**: Securely connect to SwOS devices with digest-based authentication.
- **Auto-Completion**: Integrated autocompletion for commands using the Tab key to make the CLI more user-friendly.
- **Scriptability**: Unlike the web interface, this CLI allows for automation, making it a valuable tool in larger or more complex network environments.

---

#### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/stivehu/swos-cli.git
   cd swos-cli
   ```

2. **Create a Virtual Environment (Optional but Recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Required Dependencies**:
   Install the necessary Python libraries from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

---

#### Usage

1. **Running the CLI**:
   Start the CLI tool by running:
   ```bash
   python swos_cli.py
   ```

   This will display the prompt where you can issue commands like:
   ```bash
   Welcome to MikroTik SwOS CLI
   admin@192.168.88.1> 
   ```

2. **Supported Commands**:
   - `show mac address-table all`: Display all entries in the MAC address table.
   - `show mac address-table count`: Display the number of MAC addresses in the table.
   - `show mac address-table vlan <vlan_id>`: Display MAC addresses associated with a specific VLAN.
   - `show mac address-table mac <mac_address>`: Display entries matching a specific MAC address. Supports both colon and dash-separated formats.
   - `show mac address-table interface <interface_name>`: Display MAC addresses associated with a specific interface.

   To exit the CLI, simply type:
   ```bash
   exit
   ```

3. **Examples**:
   - **Show all MAC addresses**:
     ```bash
     show mac address-table all
     ```
   - **Show MAC addresses filtered by VLAN 43**:
     ```bash
     show mac address-table vlan 43
     ```
   - **Show MAC addresses filtered by interface `1`**:
     ```bash
     show mac address-table interface 1
     ```

4. **Autocompletion**:
   The CLI supports autocompletion using the Tab key. For example, if you start typing:
   ```bash
   show mac add...
   ```
   Pressing the Tab key will complete the command as `show mac address-table`.

---

#### Roadmap and Future Improvements

- **Additional Commands**: Expand the CLI to support more commands from the SwOS web interface, such as port configuration and VLAN management.
- **Bulk Operations**: Add features to allow batch configuration changes across multiple devices.
- **Improved Parsing**: Enhance the data parsing logic to handle more complex responses and errors from SwOS.

---

#### Contributions

We welcome contributions! If you encounter any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request on GitHub.

---

#### License

This project is licensed under the MIT License.
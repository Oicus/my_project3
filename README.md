# Port Scanner Script

## Overview

This project implements a simple port scanner using Python. The script scans a range of ports on a specified target IP address to determine which ports are open.

## Features

- Scans a range of ports on a target IP address
- Uses multithreading for faster scanning
- Prints the list of open ports

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Oicus/my_project3.git
    cd my_project3
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the port scanner, use the following command:
```sh
python portscan.py <target_ip> <start_port> <end_port>
```

Example:
```sh
python portscan.py 192.168.1.1 1 1024
```

## Legal Disclaimer

This project is intended for educational purposes only. The use of this tool for scanning targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

## Development and Contributions

This project is open to contributions and further development. Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)

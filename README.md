# Web Page Refresh Project

## Description

This project allows you to continuously refresh a web page using a Python script with Selenium.

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/web-page-refresh.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Update the configuration file:

- Open the `config.ini` file.
- Set the `url` variable to the desired web page URL.
- Adjust the `refresh_interval` to specify the time (in seconds) between each refresh.

2. Run the script:

```
python web_refresh.py
```

3. To stop the script, press `Ctrl+C`.

## Configuration

The `config.ini` file contains the following settings:

- `url`: The URL of the web page to refresh.
- `refresh_interval`: The time interval (in seconds) between each refresh.

## Dependencies

The project uses the following dependencies:

- Selenium: Version X.X.X
- Other dependencies...

## Contributing

Contributions to the project are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
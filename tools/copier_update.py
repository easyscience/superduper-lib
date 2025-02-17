from copier import run_update
import requests
import tomllib  # Available in Python 3.11 and above

# URL of the raw TOML file
url = "https://raw.githubusercontent.com/easyscience/superduper/master/project.toml"

# Send a GET request to fetch the raw file content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    try:
        # Parse the TOML content
        config = tomllib.loads(response.text)
        # Access data from the TOML
        print(config)
    except tomllib.TOMLDecodeError as exc:
        print(f"Error parsing TOML: {exc}")
else:
    print(f"Failed to fetch file: {response.status_code}")

# Define the template source and destination path
destination_path = "./"

# Optional: Define data to pre-answer template questions
data = config

# Run the copier copy function
run_update(
    dst_path=destination_path,
    data=data,  # Remove this line if you prefer interactive prompts
    defaults=True,  # Set to True to use default answers without prompting
    overwrite=True,  # Set to True to overwrite existing files if any
    conflict="inline",  # How to handle conflicts: "inline" or "rej"
    # Additional parameters can be set as needed
)

from copier import run_copy
import requests
import tomllib  # Available in Python 3.11 and above
import toml
import yaml

def dict_to_yaml(data):
    """
    Convert a dictionary to a YAML string.

    Args:
        data (dict): Dictionary to convert.

    Returns:
        str: YAML-formatted string.
    """
    return yaml.dump(data, default_flow_style=False, sort_keys=False)

def fetch_and_convert_toml(url):
    """
    Fetch a TOML file from a given URL and convert it into a dictionary
    with section names as key prefixes.

    Args:
        url (str): URL of the TOML file.

    Returns:
        dict: Transformed dictionary with prefixed keys.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if the request fails

    parsed_toml = toml.loads(response.text)

    result_dict = {}
    for section, values in parsed_toml.items():
        for key, value in values.items():
            new_key = f"{section}_{key}"
            result_dict[new_key] = value

    return result_dict

# Optional: Define data to pre-answer template questions
url = "https://raw.githubusercontent.com/easyscience/superduper/master/project.toml"
data = fetch_and_convert_toml(url)

print(dict_to_yaml(data))

# Define the template source and destination path
template_src = "https://github.com/easyscience/templates-python-lib.git"
destination_path = "./"

# Run the copier copy function
run_copy(
    src_path=template_src,
    dst_path=destination_path,
    data=data,  # Remove this line if you prefer interactive prompts
    defaults=True,  # Set to True to use default answers without prompting
    overwrite=True,  # Set to True to overwrite existing files if any
    vcs_ref="master",  # Specify the branch, tag, or commit to use
    # Additional parameters can be set as needed
)

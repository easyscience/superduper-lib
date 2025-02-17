import argparse
import requests
import toml
import yaml
from typing import Dict, Any
from copier import run_copy, run_update

# Dictionary mapping template types to their respective URLs
TEMPLATE_URLS: Dict[str, str] = {
    "python-lib": "https://github.com/easyscience/templates-python-lib.git",
    "desktop-app": "https://github.com/easyscience/templates-desktop-app.git",
    "project-hub": "https://github.com/easyscience/templates-project-hub.git",
    "common": "https://github.com/easyscience/templates-common.git",
}

PROJECT_CONFIG_BASE_URL: str = "https://raw.githubusercontent.com/easyscience"


def dict_to_yaml(data: Dict[str, Any]) -> str:
    """Convert a dictionary to a YAML string."""
    return yaml.dump(data, default_flow_style=False, sort_keys=False)


def fetch_toml_to_dict(url: str) -> Dict[str, Any]:
    """Fetch a TOML file from a given URL and return python dict."""
    response = requests.get(url)
    response.raise_for_status()
    return toml.loads(response.text)


def copier_action(action: str, template_type: str, destination_path: str, repository: str = None) -> None:
    """
    Runs the copier function (copy or update) based on user input.

    Args:
        action (str): Either "copy" or "update".
        template_type (str): Template type (python-lib, desktop-app, project-hub, common).
        destination_path (str): Path where the template should be applied.
        repository (str, optional): Repository name under 'easyscience' containing project.toml (only needed for copy).
    """
    if template_type not in TEMPLATE_URLS:
        print(f"Error: Unsupported template type '{template_type}'. Choose from {list(TEMPLATE_URLS.keys())}.")
        return

    template_src: str = TEMPLATE_URLS[template_type]

    if action == "copy":
        if not repository:
            print("Error: The 'copy' action requires a repository name under 'easyscience'.")
            return

        project_config_url = f"{PROJECT_CONFIG_BASE_URL}/{repository}/master/project.toml"

        # Fetch and convert TOML data
        try:
            data: Dict[str, Any] = fetch_toml_to_dict(parsed_toml)
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch project configuration from '{project_config_url}'.\nError: {e}")
            return

        print("Using the following configuration:")
        print(dict_to_yaml(data))

        print(f"Running copier copy for template '{template_type}'...")
        run_copy(
            src_path=template_src,
            dst_path=destination_path,
            data=data,
            defaults=True,
            overwrite=True,
            vcs_ref="master",
        )

    elif action == "update":
        print(f"Running copier update for template '{template_type}'...")
        answers_file = f".copier-answers.{template_type}.yml"
        run_update(
            dst_path=destination_path,
            answers_file=answers_file,
            defaults=True,
            overwrite=True,
            conflict="inline",
        )

    else:
        print("Invalid action. Use 'copy' or 'update'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copier script for managing project templates.")

    # Required argument: action (copy or update)
    parser.add_argument("action", choices=["copy", "update"], help="Action to perform: 'copy' or 'update'.")

    # Required argument: template type
    parser.add_argument("template-type", choices=TEMPLATE_URLS.keys(), help="Type of template to use.")

    # Required argument: destination path
    parser.add_argument("--dest", default="./", help="Destination path for the template.")

    # Repository name (ONLY required for 'copy' action)
    parser.add_argument("--config-repo", help="Repository under 'easyscience' where project.toml is located (only for 'copy').")

    args = parser.parse_args()

    # Ensure repository is only required for 'copy'
    if args.action == "copy" and not args.config_repo:
        parser.error("The 'copy' action requires --config-repo to be specified.")

    copier_action(args.action, args.template_type, args.dest, args.config_repo)

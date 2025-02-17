from copier import run_update

# Define the template source and destination path
destination_path = "./"

# Optional: Define data to pre-answer template questions
data = {
    "app_docs_url": "https://docs.easydiffraction.org/lib",
    "app_repo": "diffraction-app",
    "description": "efewfw",
    "has_app": "true",
    "has_lib": "true",
    'hub_repo': "diffraction",
    "hub_url": "https://easydiffraction.org",
    "lib_docs_url": "https://docs.easydiffraction.org/lib",
    'lib_repo': "diffraction-lib",
    "package_name": "easydiffraction",
    'project_name': 'EasyDiffraction',
    'year': "2025",
    "template_dir": 'desktop-app'
}

# Run the copier copy function
run_update(
    dst_path=destination_path,
    data=data,  # Remove this line if you prefer interactive prompts
    defaults=True,  # Set to True to use default answers without prompting
    overwrite=True,  # Set to True to overwrite existing files if any
    conflict="inline",  # How to handle conflicts: "inline" or "rej"
    # Additional parameters can be set as needed
)

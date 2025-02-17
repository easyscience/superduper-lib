from copier import run_copy

# Define the template source and destination path
template_src = "https://github.com/easyscience/templates-copier.git"
destination_path = "./"

# Optional: Define data to pre-answer template questions
data = {
    "app_docs_url": "https://docs.easydiffraction.org/lib"
    "app_repo": "diffraction-app"
    "description": "efewfw"
    "has_app": "true"
    "has_lib": "true"
    'hub_repo': "diffraction"
    "hub_url": "https://easydiffraction.org"
    "lib_docs_url": "https://docs.easydiffraction.org/lib"
    'lib_repo': "diffraction-lib"
    "package_name": "easydiffraction"
    'project_name': 'EasyDiffraction'
    'year': "2025"
}

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

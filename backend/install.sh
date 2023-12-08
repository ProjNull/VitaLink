#!/bin/bash
#
# Step 0: Check if .conda/ or .venv/ directories are present and instruct the user to activate an environment
if [ -d ".conda" ] || [ -d ".venv" ]; then
    echo "You have existing environments in this directory."
    echo "To activate a Conda environment, run: conda activate ./.conda"
    echo "To activate a VirtualEnv environment, run: source .venv/bin/activate"
    exit 0
fi

# Step 1: Check if conda is installed
if command -v conda &> /dev/null; then
    CONDA_INSTALLED=true
else
    CONDA_INSTALLED=false
fi

# Step 2: Check if python is installed
if command -v python &> /dev/null; then
    PYTHON_INSTALLED=true
else
    PYTHON_INSTALLED=false
fi

# Step 3: If python is installed, check if virtualenv is installed
if [ "$PYTHON_INSTALLED" = true ]; then
    if pip show virtualenv &> /dev/null; then
        VENV_INSTALLED=true
    else
        VENV_INSTALLED=false
    fi
fi

# Step 4: Check if conda and python are not installed
if [ "$CONDA_INSTALLED" = false ] && [ "$PYTHON_INSTALLED" = false ]; then
    echo "Neither Conda nor Python is installed. Please install either Conda or Python and run the script again."
    exit 1
fi

# Step 5: If conda is not installed but Python is, check if virtualenv is installed
if [ "$CONDA_INSTALLED" = false ] && [ "$PYTHON_INSTALLED" = true ] && [ "$VENV_INSTALLED" = false ]; then
    read -p "Python is installed, but VirtualEnv is not. Do you want to install VirtualEnv? (y/n): " INSTALL_VENV
    if [ "$INSTALL_VENV" = "y" ]; then
        pip install virtualenv
    else
        echo "You can manually install VirtualEnv and run the script again."
        exit 1
    fi
fi

# Step 6: If both Conda and VirtualEnv are installed, ask the user which one to use
if [ "$CONDA_INSTALLED" = true ] && [ "$VENV_INSTALLED" = true ]; then
    read -p "Both Conda and VirtualEnv are installed. Which one do you want to use? (conda/venv): " ENV_CHOICE
    if [ "$ENV_CHOICE" = "conda" ]; then
        ENV_NAME=".conda"
    elif [ "$ENV_CHOICE" = "venv" ]; then
        ENV_NAME=".venv"
    else
        echo "Invalid choice. Please select 'conda' or 'venv'."
        exit 1
    fi
elif [ "$CONDA_INSTALLED" = true ]; then
    ENV_NAME=".conda"
elif [ "$VENV_INSTALLED" = true ]; then
    ENV_NAME=".venv"
fi

# Step 7: Create a new environment with Python 3.11.X
if [ "$ENV_NAME" = ".conda" ]; then
    conda create -p ./.conda python=3.11
else
    virtualenv -p python3.11 $ENV_NAME
    source $ENV_NAME/bin/activate
fi

ENV_PATH=$(pwd)/$ENV_NAME
echo "Environment created at: $ENV_PATH"

# Step 8: Install requirements.txt using pip
if [ -f "requirements.txt" ]; then
    if [ "$ENV_NAME" = ".conda" ]; then
        echo Requirements auto install is not supported with conda. Install pip packages manually.
    else
        read -p "Do you want to install requirements.txt now? (y/n): " INSTALL_REQUIREMENTS
        if [ "$INSTALL_REQUIREMENTS" = "y" ]; then
            source ./.venv/bin/activate
            PIP_PATH=$(which pip)
            echo Installing packages using $PIP_PATH
            $PIP_PATH install -r requirements.txt
        fi
    fi
else
    echo "No requirements.txt file found. Install pip packages manually."
fi

echo "To activate a Conda environment, run: conda activate ./.conda"
echo "To activate a VirtualEnv environment, run: source ./.venv/bin/activate"
exit 0

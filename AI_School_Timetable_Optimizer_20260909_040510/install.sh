#!/bin/bash

# Update pip to the latest version
pip install --upgrade pip

# Install dependencies from requirements.txt
pip install -r /mount/src/c-users-sc-desktop-local-ai-software-factory-workspace-projects-ai_school_timetable_optimizer/requirements.txt

# Install rich for improved exception logging
pip install rich>=10.14.0

# Update pip again after installing rich
pip install --upgrade pip
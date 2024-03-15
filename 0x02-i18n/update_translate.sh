#!/usr/bin/bash
# This script is used to update the translation files for the project.

echo "Updating translation files..."
pybabel extract -F babel.cfg -o messages.pot .

# Array of Supported Languages
declare -a LANGUAGES=("en" "fr")

echo "\n\n"

# check if the translations directory exists and if not, create it
if [ ! -d "translations" ]; then
    mkdir translations
    for lang in "${LANGUAGES[@]}"
    do
        pybabel init -i messages.pot -d translations -l $lang
    done  
else
    for lang in "${LANGUAGES[@]}"
    do
        pybabel update -i messages.pot -d translations -l $lang
    done
fi

echo "\n\n"

# if the translations are updated, compile them
pybabel compile -d translations

echo "\n\n"

echo "Translation files updated successfully."

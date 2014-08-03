#!/usr/bin/env bash
# execute by typing ./download_nces.sh into shell prompt

# Download and extract 2011 NCES data
#
# Resulting file structure:
#    data/state    -- state level
#    data/district -- district level
#    data/school   -- school level

read -r -p "Download 2011 NCES district finance data? [y/N] " response
case $response in
    [yY][eE][sS]|[yY]) 
        echo
        if [ ! -d "$data/district" ]; then
            mkdir -p data/district
        fi
        wget http://nces.ed.gov/ccd/data/zip/sdf11_1a_txt.zip -P data/district
        tar -xvf data/district/sdf11_1a_txt.zip -C data/district/
        rm data/district/sdf11_1a_txt.zip
        echo
        ;;
esac

read -r -p "Download 2011 NCES state finance data? [y/N] " response
case $response in
    [yY][eE][sS]|[yY]) 
        echo
        if [ ! -d "$data/state" ]; then
            mkdir -p data/state
        fi
        wget http://nces.ed.gov/ccd/data/zip/stfis111a_txt.zip -P data/state
        tar -xvf data/state/stfis111a_txt.zip -C data/state/
        rm data/district/stfis111a_txt.zip
        echo
        ;;
esac

read -r -p "Download 2011 NCES district survery data? [y/N] " response
case $response in
    [yY][eE][sS]|[yY]) 
        echo
        if [ ! -d "$data/district" ]; then
            mkdir -p data/district
        fi
        wget http://nces.ed.gov/ccd/Data/zip/ag111a_txt.zip -P data/district
        tar -xvf data/district/ag111a_txt.zip -C data/district/
        rm data/district/ag111a_txt.zip
        echo
        ;;
esac

read -r -p "Download 2011 NCES school survery data? [y/N] " response
case $response in
    [yY][eE][sS]|[yY]) 
        echo
        if [ ! -d "$data/school" ]; then
            mkdir -p data/school
        fi
        wget http://nces.ed.gov/ccd/Data/zip/sc111a_supp_txt.zip -P data/school
        tar -xvf data/school/sc111a_supp_txt.zip -C data/school/
        rm data/school/sc111a_supp_txt.zip
        echo
        ;;
esac

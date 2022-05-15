import os, sys
from pathlib import Path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import path_definitions

flag_using_sample_data = True # when you have the full data, turn if off

url_dictionary = {
    "data_raw_sample": "https://drive.google.com/uc?export=download&id=1CmXO7H1SJNQv06WxJvHOW8Q1jl4aQk2y"
}

def get_raw_feature_folderpath(phase = 1, institute = "INS"):
    path = os.path.join(path_definitions.RAWDATA_PATH , institute + "_" + str(phase) , "FeatureData/")
    return path

def get_survey_filepath(phase = 1, institute = "INS"):
    path = os.path.join(path_definitions.RAWDATA_PATH , institute + "_" + str(phase) , "SurveyData/")
    return path

def get_deviceinfo_filepath(phase = 1, institute = "INS"):
    path = os.path.join(path_definitions.RAWDATA_PATH , institute + "_" + str(phase) , "DeviceInfoData/")
    return path

feature_folder = {
    "INS1": {1:get_raw_feature_folderpath(1, "INS1"),
        2:get_raw_feature_folderpath(2, "INS1"),
        3:get_raw_feature_folderpath(3, "INS1"),
        4:get_raw_feature_folderpath(4, "INS1")},
    "INS2": {1:get_raw_feature_folderpath(1, "INS2"),
        2: get_raw_feature_folderpath(2, "INS2")},
}

survey_folder = {
    "INS1": {1:get_survey_filepath(1, "INS1"),
        2:get_survey_filepath(2, "INS1"),
        3:get_survey_filepath(3, "INS1"),
        4:get_survey_filepath(4, "INS1"),},
    "INS2": {1:get_survey_filepath(1, "INS2"), 
        2: get_survey_filepath(2, "INS2")},
}

device_info_folder = {
    "INS1": {1:get_deviceinfo_filepath(1, "INS1"),
        2:get_deviceinfo_filepath(2, "INS1"),
        3:get_deviceinfo_filepath(3, "INS1"),
        4:get_deviceinfo_filepath(4, "INS1")},
    "INS2": {1:get_deviceinfo_filepath(1, "INS2"),
        2:get_deviceinfo_filepath(2, "INS2")},
}

def get_raw_feature_folderpath_sample(phase = 1, institute = "INS"):
    path = os.path.join(path_definitions.RAWDATA_PATH , institute + "_" + str(phase) + "_sample" , "FeatureData/")
    return path

def get_survey_filepath_sample(phase = 1, institute = "INS"):
    path = os.path.join(path_definitions.RAWDATA_PATH , institute + "_" + str(phase) + "_sample" , "SurveyData/")
    return path

def get_deviceinfo_filepath_sample(phase = 1, institute = "INS"):
    path = os.path.join(path_definitions.RAWDATA_PATH , institute + "_" + str(phase) + "_sample" , "DeviceInfoData/")
    return path

feature_folder_sample = {
    "INS1": {1:get_raw_feature_folderpath_sample(1, "INS1"),
        2:get_raw_feature_folderpath_sample(2, "INS1"),
        3:get_raw_feature_folderpath_sample(3, "INS1"),
        4:get_raw_feature_folderpath_sample(4, "INS1")},
    "INS2": {1:get_raw_feature_folderpath_sample(1, "INS2"),
        2: get_raw_feature_folderpath_sample(2, "INS2")},
}

survey_folder_sample = {
    "INS1": {1:get_survey_filepath_sample(1, "INS1"),
        2:get_survey_filepath_sample(2, "INS1"),
        3:get_survey_filepath_sample(3, "INS1"),
        4:get_survey_filepath_sample(4, "INS1"),},
    "INS2": {1:get_survey_filepath_sample(1, "INS2"), 
        2: get_survey_filepath_sample(2, "INS2")},
}

device_info_folder_sample = {
    "INS1": {1:get_deviceinfo_filepath_sample(1, "INS1"),
        2:get_deviceinfo_filepath_sample(2, "INS1"),
        3:get_deviceinfo_filepath_sample(3, "INS1"),
        4:get_deviceinfo_filepath_sample(4, "INS1")},
    "INS2": {1:get_deviceinfo_filepath_sample(1, "INS2"),
        2:get_deviceinfo_filepath_sample(2, "INS2")},
}

if (flag_using_sample_data):
    feature_folder = feature_folder_sample
    survey_folder = survey_folder_sample
    device_info_folder = device_info_folder_sample
import os, yaml, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pathlib import Path
from data_loader import data_loader_ml, data_loader_dl
from utils import path_definitions
from data import data_factory
import wget
import zipfile

def download_rawdata(key:str = "data_raw_sample") -> None:
    """ Download and unzip the data """

    target_path = os.path.join(path_definitions.RAWDATA_PATH, key + ".zip")
    if (os.path.exists(target_path)):
        return
        
    url = data_factory.url_dictionary[key]
    print("Downloading sample data...")
    wget.download(url, out = target_path)
    print("Unzipping data...")
    with zipfile.ZipFile(target_path,"r") as zip_ref:
        zip_ref.extractall(path_definitions.RAWDATA_PATH)
    print("Unzipping done!")


def convert_rawdata_to_pkldata() -> None:
    """ Convert raw data from 'data_raw' folder to pkl data in 'data' folder """

    with open(os.path.join(os.path.dirname(os.path.abspath(Path(__file__).parent)),
        "config", f"global_config.yaml"), "r") as f:
        global_config = yaml.safe_load(f)

    ds_keys = global_config["all"]["ds_keys"]
    pred_targets = global_config["all"]["prediction_tasks"]

    # prepare pkl file with sliced data format
    data_loader_ml.data_loader(
        ds_keys_dict={pt: ds_keys for pt in pred_targets}, flag_max_feature_types=False)
    
    # prepare pkl file with raw time-series format
    data_loader_ml.data_loader_raw(ds_keys_list=ds_keys)

    # prepare pkl file with all sensor types (currently support INS1)
    ins_list = [i.split("_")[0] for i in ds_keys]
    ins_all = list(set(ins_list))
    if (len(ins_all) == 0 and ins_all[0] == "INS1"):
        data_loader_ml.data_loader(
            ds_keys_dict={pt: ds_keys for pt in pred_targets}, flag_max_feature_types=True)

    # prepare np pkl file with sliced data format for deep models
    data_loader_dl.prep_repo_np_dict(flag_normalize=True)
    data_loader_dl.prep_repo_np_dict(flag_normalize=False)

    # prepare placeholder to make sure the pipeline will go smoothly for deep models
    data_loader_dl.data_loader_dl_placeholder(pred_targets, ds_keys)

if __name__ == "__main__":
    
    download_rawdata()

    convert_rawdata_to_pkldata()
import os

from hansel import Crumb
from neuro_pypes.run import run_debug, run_wf
from neuro_pypes.config import update_config
from neuro_pypes.io import build_crumb_workflow
from neuro_pypes.anat import attach_spm_anat_preprocessing

print("\033[1;34m")
print("ALL MODUELS IMPORTED")
print("\033[0m")

# root path to my data
base_dir = os.getcwd() + "/data"

# the configuration file path
config_file_path = "pypes_config.yml"

# define the Crumb filetree of my image database
data_path = os.path.join(
    base_dir, "{subject_id}", "session_1", "{modality}", "{image}")

# create the filetree Crumb object
data_crumb = Crumb(data_path, ignore_list=[".*"])
print(data_crumb)
print(data_crumb['subject_id'])
print(data_crumb['image'])

# the different worflows that I will use with any given name
attach_functions = {"spm_anat_preproc": attach_spm_anat_preprocessing}

# the specific parts of the `data_crumb` that define a given modality.
# **Note**: the key values of this `crumb_arguments` must be the same as expected
# in the functions in `attach_functions`.
crumb_arguments = {'anat': [('modality', 'anat_1'),
                            ('image', 'mr_img.nii.gz')]
                   }

# the pypes configuration file with workflow parameter values
update_config(config_file_path)

# output and working directory paths
output_dir = os.path.join(os.path.dirname(base_dir), "out")
cache_dir = os.path.join(os.path.dirname(base_dir), "wd")

# build the workflow
wf = build_crumb_workflow(attach_functions,
                          data_crumb=data_crumb,
                          in_out_kwargs=crumb_arguments,
                          output_dir=output_dir,
                          cache_dir=cache_dir,)


print("\033[1;34m")
print("WORKFLOW BUILT")
print("\033[0m")

run_wf(wf, plugin="MultiProc", n_cpus=8)

print("\033[1;34m")
print("WORKFLOW RAN WITHOUT ERRORS")
print("\033[0m")

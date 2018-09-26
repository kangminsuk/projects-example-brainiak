import numpy as np 
import scipy.io
import nibabel as nib
from nilearn.input_data import NiftiMasker
from sklearn import preprocessing

# data path VDC dataset (instructor should set this properly)
# princeton adroit
vdc_data_dir = '/home/NEU480/datasets/vdc/'
# yale 
# vdc_data_dir = '/gpfs/milgram/data/cmhn-s18/datasets/vdc/'

# constants for the VDC dataset
vdc_label_dict = {1: "Faces", 2: "Scenes", 3: "Objects"}
vdc_all_ROIs = ['FFA', 'PPA']
vdc_n_runs = 3

def get_MNI152_template(dim_x, dim_y, dim_z):
    """get MNI152 template used in fmrisim
    Parameters
    ----------
    dim_x: int
    dim_y: int
    dim_z: int
        - dims set the size of the volume we want to create
    
    Returns
    -------
    MNI_152_template: 3d array (dim_x, dim_y, dim_z)
    """
    # Import the fmrisim from BrainIAK
    import brainiak.utils.fmrisim as sim 
    # Make a grey matter mask into a 3d volume of a given size
    dimensions = np.asarray([dim_x, dim_y, dim_z])
    _, MNI_152_template = sim.mask_brain(dimensions)
    return MNI_152_template


def load_vdc_stim_labels(sub):
    stim_label = [];
    stim_label_allruns = [];
    for run in range(1, vdc_n_runs + 1):
        in_file = (vdc_data_dir + sub + '/ses-day2/design_matrix/' + '%s_localizer_0%d.mat' % (sub, run))
        # Load in data from matlab
        stim_label = scipy.io.loadmat(in_file);
        stim_label = np.array(stim_label['data']);
        # Store the data
        if run == 1:
            stim_label_allruns = stim_label;
        else:       
            stim_label_allruns = np.hstack((stim_label_allruns, stim_label))
    return stim_label_allruns


def load_vdc_mask(ROI_name, sub):
    maskdir = (vdc_data_dir + sub + "/preprocessed/masks/")
    # load the mask
    maskfile = (maskdir + "sub-01_ventral_%s_locColl_to_epi1.nii.gz" % (ROI_name))
    mask = nib.load(maskfile)
    return mask


def load_vdc_epi_data(sub, run):
    # Load MRI file (in Nifti format) of one localizer run
    epi_in = (vdc_data_dir + sub + 
              "/preprocessed/loc/%s_filtered2_d1_firstExampleFunc_r%d.nii" % (sub, run))
    epi_data = nib.load(epi_in)
    return epi_data


def mask_data(epi_data, mask): 
    nifti_masker = NiftiMasker(mask_img=mask)
    epi_masked_data = nifti_masker.fit_transform(epi_data);
    return epi_masked_data


def scale_data(data): 
    data_scaled = preprocessing.StandardScaler().fit_transform(data)
    return data_scaled


# Make a function to load the mask data
def load_vdc_masked_data(directory, subject_name, mask_list):    
    masked_data_all = [0] * len(mask_list)
    maskdir = (directory + subject_name + "/preprocessed/masks/")

    # Cycle through the masks
    for mask_counter in range(len(mask_list)):
        # load the mask for the corresponding ROI
        mask = load_vdc_mask(mask_list[mask_counter], subject_name)

        # Cycle through the runs
        for run in range(1, vdc_n_runs + 1):
            # load fMRI data 
            epi_data = load_vdc_epi_data(subject_name, run)
            # mask the data 
            epi_masked_data = mask_data(epi_data, mask)
            epi_masked_data = np.transpose(epi_masked_data)
            # z-scoring here is removed to avoid double dipping
#             # Z-score (Standardize) the data  
#             epi_masked_data_zscored = scale_data(epi_masked_data)
            
            # concatenate data 
            if run == 1:
                masked_data_all[mask_counter] = epi_masked_data
            else:
                masked_data_all[mask_counter] = np.hstack(
                    (masked_data_all[mask_counter], epi_masked_data)
                )
    return masked_data_all


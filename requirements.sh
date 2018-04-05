# Python dependencies -----------------
apt-get update \
    && apt-get install -y build-essential libgomp1 libmpich-dev mpich python3-tk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

pip3 install sklearn scipy brainiak nilearn

# Data --------------------------------
DATADIR=/home/repl/datasets
DATA_URL=https://s3.amazonaws.com/assets.datacamp.com/projects/machow-pni-demo/BE_roi_data.mat

mkdir -p $DATADIR

wget -O $DATADIR/BE_roi_data.mat $DATA_URL

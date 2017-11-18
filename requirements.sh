# Python dependencies -----------------
pip3 install sklearn

# Data --------------------------------
DATADIR=/home/repl/datasets
DATA_URL=https://s3.amazonaws.com/assets.datacamp.com/projects/machow-pni-demo/BE_roi_data.mat

mkdir -p $DATADIR

wget -O $DATADIR/BE_roi_data.mat $DATA_URL

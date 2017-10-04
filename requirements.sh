pip3 install numpy==1.11.0
pip3 install pandas==0.19.1
pip3 install scipy==0.18.1
pip3 install seaborn==0.7.1

DATADIR=/usr/local/share/datasets
mkdir -p $DATADIR
wget -O $DATADIR/colors.csv https://s3.amazonaws.com/assets.datacamp.com/production/project_10/datasets/colors.csv
wget -O $DATADIR/sets.csv https://s3.amazonaws.com/assets.datacamp.com/production/project_10/datasets/sets.csv

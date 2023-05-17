# Create env to test query
#
set -e
TEST_PY=`realpath  python/test_query.py`
MOCK_CLIENT1=`realpath python/mock_client1.py`
PSEDO_DIR=pseudo_env
cd ~/Downloads
rm -Rf $PSEDO_DIR 
mkdir -p $PSEDO_DIR  
cd $PSEDO_DIR
cp $TEST_PY .
mkdir google
mkdir google/cloud
cp $MOCK_CLIENT1 google/cloud/bigquery.py
#pip install py-bigquery-mock


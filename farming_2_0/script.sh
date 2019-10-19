export MICRO_ENV=/Users/aviso/backend/famring_2.0_env

# activate the environments
if [ -f $MICRO_ENV/bin/activate ]; then
    source $MICRO_ENV/bin/activate
    else
    echo
    echo "################################################################################"
    echo "#              No python environment found at: $MICRO_ENV                      #"
    echo "#  Trying to run without activating env... assuming env is already activated . #"
    echo "################################################################################"
fi
# runserver basing on the inputs
if [ $# -gt 0 ]; then
    python manage.py $*
else
    python manage.py runserver 8005
fi
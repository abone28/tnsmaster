## Install into virtualenv

virtualenv --prompt '(tnsmaster) ' .venv
. .venv/bin/activate
pip install -e .

## If you like to participate on this project, install git hooks
cd .git/hooks/

ln -s ../../hooks/pre-commit.sh pre-commit

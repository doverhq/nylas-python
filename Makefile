SHELL := /bin/bash
################################
# Deploy
################################

clean-python-build:
	rm -rf dist *.egg-info

_publish-python-package: clean-python-build
	python setup.py sdist && \
		twine upload dist/* --repository-url https://api.packagr.app/88ncBXhza/ -u '' -p ${PACKAGR_TOKEN}

publish-package: _publish-python-package clean-python-build

sync-dev-deps:
	# install all deps locally
	pip install -e ".[release,test,docs]"

ifndef MK_RELEASE_PY
MK_RELEASE_PY=1

include make/env.Makefile
include make/ci.py.Makefile

PYPI_NAME = $(shell $(READ_PYPROJECT_KEY) pypi.name)
PYPI_URL = $(shell $(READ_PYPROJECT_KEY) pypi.url)

build: clean  ## Build the python package
	poetry build

publish: build ## Publish the python package to the repository
	poetry config repositories.$(PYPI_NAME) $(PYPI_URL)
	poetry publish -r $(PYPI_NAME)

endif

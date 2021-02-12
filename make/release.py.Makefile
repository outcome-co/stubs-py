ifndef MK_RELEASE_PY
MK_RELEASE_PY=1

include make/ci.py.Makefile

build: clean
	poetry build

publish: build
	poetry publish

endif

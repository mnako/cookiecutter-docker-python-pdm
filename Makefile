dev-env:
	@if [ ! -d "__pypackages__" ]; then pdm install; pdm install --group dev; fi;

test: dev-env
	pdm run pytest -vv tests

rm:
	rm -rf .mypy_cache/ || true
	rm -rf .pytest_cache/ || true
	rm -rf __pypackages__/ || true
	rm -rf tests/__pycache__/ || true

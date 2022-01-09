install:
	pdm install
	pdm install --group dev

test:
	pdm run pytest -vv tests

rm:
	rm -rf .mypy_cache/ || true
	rm -rf .pytest_cache/ || true
	rm -rf __pypackages__/ || true
	rm -rf tests/__pycache__/ || true

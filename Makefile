test:
	rm -rf /tmp/testproject || true
	pdm run cookiecutter . --output-dir /tmp --no-input project_name=testproject
	cd /tmp/testproject && \
	$(MAKE) run && \
	$(MAKE) test && \
	$(MAKE) build VERSION=0.0.0 && \
	$(MAKE) rm
	@echo "All tests passed"

.PHONY: test

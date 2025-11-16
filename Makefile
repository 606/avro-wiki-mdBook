.PHONY: help build serve clean test check-links generate-summary install

help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install mdBook
	@echo "Installing mdBook..."
	@command -v cargo >/dev/null 2>&1 && cargo install mdbook || \
		(echo "Error: cargo not found. Please install Rust first." && exit 1)

build: ## Build the wiki
	@echo "Building the wiki..."
	@mdbook build

serve: ## Serve the wiki locally with live reload
	@echo "Starting local server..."
	@mdbook serve --open

clean: ## Clean build artifacts
	@echo "Cleaning build artifacts..."
	@rm -rf book/

test: ## Run mdBook tests
	@echo "Running tests..."
	@mdbook test

check-links: ## Check for broken links
	@echo "Checking for broken links..."
	@python3 scripts/check_links.py

generate-summary: ## Auto-generate SUMMARY.md from file structure
	@echo "Generating SUMMARY.md..."
	@python3 scripts/generate_summary.py --dry-run

watch: ## Build and serve with live reload (alias for serve)
	@$(MAKE) serve

validate: check-links build ## Validate links and build
	@echo "Validation complete!"

all: clean build ## Clean and build

.DEFAULT_GOAL := help

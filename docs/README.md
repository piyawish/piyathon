# Piyathon Documentation

## Description

This directory contains the complete documentation for the Piyathon project, built using Sphinx documentation generator. The documentation includes tutorials, examples, and detailed guides for using and developing with Piyathon.

## Directory Structure

- `source/`: Contains the source files for documentation in Markdown/RST format
  - `tutorial/`: Step-by-step guides from basics to advanced usage
  - `examples/`: Code examples and cookbook
  - `getting_started/`: Installation and initial setup guides
- `build/`: Generated documentation output directory
- `media/`: Documentation assets (images, diagrams, etc.)
- `Makefile`: Build automation for documentation

## Development Guidelines

1. All documentation source files are in the `source/` directory
2. Use Markdown (.md) format for content files
3. Update `conf.py` in source/ for configuration changes
4. Test your changes locally by building the docs before committing
5. Keep the directory structure organized according to the existing pattern:
   - Put tutorials in `source/tutorial/`
   - Add examples in `source/examples/`
   - Place getting started guides in `source/getting_started/`

## Contributing

1. Review existing documentation structure before adding new content
2. Follow the established formatting and style guidelines
3. Update the table of contents when adding new pages
4. Include practical examples where appropriate
5. Test all code examples before committing

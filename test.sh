#!/bin/zsh

poetry run python build.py build_ext --inplace
rm -r src/**/*.c
poetry run python -c "import main; main.main()"
rm -r main.cpython*.so

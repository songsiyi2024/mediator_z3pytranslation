#!/usr/bin/env bash
# examples/build_and_run.sh - build and run ParseExample on Unix-like systems
set -e
ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/.."
cd "$ROOT_DIR"

javac -cp .:org examples/ParseExample.java -d examples_bin
java -cp .:org:examples_bin ParseExample

#!/usr/bin/env bash
# Delegator: forward to tools/gradle/gradlew
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
"$SCRIPT_DIR/tools/gradle/gradlew" "$@"

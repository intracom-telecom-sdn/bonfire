#!/bin/bash


FLAMEGRAPH_HOME=$BONFIRE_HOME/submodules/FlameGraph
echo "export FLAMEGRAPH_HOME=$FLAMEGRAPH_HOME" >> $BONFIRE_HOME/setup_env_vars.sh
echo 'export PATH=$PATH:$FLAMEGRAPH_HOME' >> $BONFIRE_HOME/setup_env_vars.sh


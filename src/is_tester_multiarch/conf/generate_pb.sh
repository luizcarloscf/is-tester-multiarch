#!/bin/bash
set -e 

echo "|>>| Generating protobuf..."
docker run --rm -v $(pwd):$(pwd) -w $(pwd) luizcarloscf/docker-protobuf:master \
                                                        --python_out=. \
                                                        -I./ options.proto
echo "|>>| Done!"

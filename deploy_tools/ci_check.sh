#!/bin/bash

echo "Waiting for containers to finish..."
while ! curl -sSf localhost:8000 > /dev/null; do
    sleep 2
done

echo "Containers are up"

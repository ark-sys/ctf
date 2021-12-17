#!/bin/sh

for dir in app-script/;do
    if [ -f "$dir/README.md" ]; then
        pandoc $dir/README.md -o $dir/segment.pdf
    fi
done

for dir in app-systeme/;do
    if [ -f "$dir/README.md" ]; then
        pandoc $dir/README.md -o $dir/segment.pdf
    fi
done

for dir in cracking/*;do
    if [ -f "$dir/README.md" ]; then
        pandoc $dir/README.md -o $dir/segment.pdf
    fi
done

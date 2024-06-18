#!/bin/bash

# Check if a commit message was provided
if [ -z "$1" ]; then
  echo "Usage: $0 <commit-message>"
  exit 1
fi

# Add all changes to staging
git add .
if [ $? -ne 0 ]; then
  echo "Error: Failed to add changes"
  exit 1
fi

# Commit changes with the provided message
git commit -m "$1"
if [ $? -ne 0 ]; then
  echo "Error: Failed to commit changes"
  exit 1
fi

# Push changes to the repository
git push
if [ $? -ne 0 ]; then
  echo "Error: Failed to push changes"
  exit 1
fi

echo "Successfully added, committed, and pushed changes"


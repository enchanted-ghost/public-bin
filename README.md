# public-bin

Welcome to a collection of useful (to me) scripts, utilities, hack-jobs etc.

`emulate_bitbucket_pipelines.py` - Hack-job #1. We often use various CICD platforms, BitBucket being one. Occasionally
something goes wrong, and we need to debug what the pipeline is going through. This is how I go about doing so. It
parses the yaml config file and spits out a command to start a docker container using the same image BitBucket uses.
Assuming you have access to pull this container.

"""emulate_bitbucket.py"""
import yaml

BB_PIPELINE_CONFIG = 'bitbucket-pipelines.yml'


with open(BB_PIPELINE_CONFIG, 'r') as file:
    bb_config = yaml.safe_load(file)

if bb_config == None:
    print("No {} found...", BB_PIPELINE_CONFIG)

# print(bb_config['image'])
print("########################################")
print("* Docker commnad to run...\n")
print("docker run --rm -it -v $(pwd):/bb " +bb_config['image'])
print("")
print("########################################")

print("* Commands to run\n")
print("cd /bb")
# THIS IS A VERY GROSS WAY OF LOOKING AT THE COMMANDS
#
for step in bb_config['pipelines']['branches']['master'][0]["step"]["script"]:
    print(step)


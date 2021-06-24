import os
#Pprerequisite: install trivy and docker as well before you execute the script
#input for the code image to pull. 
docker_image = input("Please enter the docker image that you wish to scan: ")
os.system(f'docker pull {docker_image}')
os.system(f"trivy image --severity HIGH {docker_image}")





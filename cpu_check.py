import psutil
import subprocess
import time

def configure_auto_scaling(auto_scale_commands):
    print("Configuring auto-scaling properties...")
    for current_command in auto_scale_commands:
        print(f"Running command: {current_command}")    
        try:
            # Execute each command
            subprocess.run(current_command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {e}")

def check_cpu_usage(commands, interval_sec=10, duration_sec=600):
    print(f"Current CPU usage check at {time.time()}...")
    
    check_final_time = time.time() + duration_sec
    while time.time() < check_final_time:
        cpu_load = psutil.cpu_percent(interval=1)
        print(f"CPU Usage Data: {cpu_load}%")
        
        if cpu_load >= 75:
            for current_command in commands:
                print(f"Running command: {current_command}")
                try:
                    # Execute each command
                    subprocess.run(current_command, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Command failed: {e}")
                
        time.sleep(interval_sec - 1)

if __name__ == "__main__":
    commands = [
        "gcloud config configurations create auto-scale-gcp-config --activate || gcloud config configurations activate auto-scale-gcp-config && gcloud auth activate-service-account --key-file=\"/home/vboxuser/Downloads/rugged-sentry-453807-s0-906843f2288d.json\" && gcloud config set project \"rugged-sentry-453807-s0\" --quiet && gcloud config set compute/zone \"us-central1-a\" --quiet && gcloud config set compute/region \"us-central1\" --quiet",
        "sleep 5",
        "gcloud compute instances create assignment-3-api-solution --machine-type=e2-small --image-project=ubuntu-os-cloud --image-family=ubuntu-2004-lts --zone=us-central1-a",
        "sleep 30",
        "gcloud compute scp --recurse /home/vboxuser/Assignment-3/Assignment-3-API/bin/Debug/net7.0 assignment-3-api-solution:/tmp/assignment-3-api-solution --zone=us-central1-a",
        "sleep 20",
        "gcloud compute ssh assignment-3-api-solution --zone=us-central1-a --command=\"sudo chown m22aie201:m22aie201 /home/m22aie201; sudo chmod 755 /home/m22aie201; sudo mv /tmp/assignment-3-api-solution /home/m22aie201; sudo apt-get update && sudo apt-get install -y wget gpg && wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb && sudo dpkg -i packages-microsoft-prod.deb && sudo apt-get update && sudo apt-get install -y dotnet-sdk-7.0; cd /home/m22aie201/assignment-3-api-solution; dotnet exec Assignment-3-API.dll;\"",
"sleep 30",
        "gcloud compute firewall-rules create allow-api --allow=tcp:5000 --source-ranges=0.0.0.0/0 --description=\"Allow external access to API\""
    ]
    check_cpu_usage(commands, interval_sec=5, duration_sec=60)
    
    auto_scaling_commands = [
    "sleep 10",
    "gcloud compute instance-templates create auto-scaling-template --machine-type=e2-small --image-family=ubuntu-2204-lts --image-project=ubuntu-os-cloud --tags=http-server,https-server",
"gcloud compute instance-groups managed create auto-scaling-group --base-instance-name=assignment-3-api-solution --size=1 --template=auto-scaling-template --zone=us-central1-a",
"gcloud compute instance-groups managed set-autoscaling auto-scaling-group --zone=us-central1-a --min-num-replicas=1 --max-num-replicas=2 --target-cpu-utilization=0.6 --cool-down-period=60"
    ]
    
    configure_auto_scaling(commands)

The goal of this project is to create a local virtual machine (VM) and implement a mechanism to monitor its resource usage. When the cpu usage exceeds 75%, the system scales the application to a Google Cloud.

Application used for testing is a dotnet(.NET 7.0) REST API with two endpoints. One endpoints provides weather information and another endpoint provides facts for cats. Below is a snapshot for application endpoints:
Pre-requisite:
.NET should be existing in the system to run the API solution.

![image](https://github.com/user-attachments/assets/e977f12c-20d9-4ce4-a047-2bbf62f31474)

Program Flow:
1. Local VM Creation: Local VM created using VirtualBox.
2. Resource Monitoring: Monitor CPU usage using Python script.
3. Auto-Scaling to Cloud: Deploy the application to cloud when CPU thresholds are exceeded.
4. Application Deployment: Transfer application artifacts to cloud environment and run application from cloud as well.

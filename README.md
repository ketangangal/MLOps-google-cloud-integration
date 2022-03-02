# mlops-google-cloud-integration
MLOps-google-cloud-integration.
Kubeflow is a tool that allows you to essentially integrate your machine learning lifecycles into Kubernetes. 
# Download Google CLoud SDK 
```commandline
https://cloud.google.com/sdk/docs/install
```

# Requirements 
```commandline
pip install mlflow 
pip install scikit-learn 
```
# Steps to setup Google 
1. This is perhaps the hardest step in this deployment process. 
First, you set up a bucket and push the contents of your mlruns folder to be stored on the cloud.
2. Next, you set up the virtual machine that will host your server when you deploy the model.
This involves installing Conda and MLFlow.
3. 
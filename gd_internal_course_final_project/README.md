This is the final project of course Kubernetes. \
I've migrated the project from docker-compose to Kubernetes.\
To run this project follow the next steps:\
To create new cluster by minikube, run the following command: 
```
minikube start
```
To enable the NGINX Ingress controller, run the following command:
```
minikube addons enable ingress
```
To clone repository, run the following command:
```
git clone git@github.com:atrofymchuk/kubernetes.git
```
To deploy all recourses to the cluster, run the following command:
```
kubectl apply -f ./kubernetes
```
You need to wait several minutes until all recourses will be created and run and then for creating an index "elastic", run the following command:
```
curl -X PUT "http://`minikube ip`/elastic" -H 'Content-Type: application/json' -d'{ "settings" : { "index" : { } }}'
```
To get IP address of the cluster, run the following command:
```
kubectl get ingress
```
You will see the IP address of the cluster for example:
```
NAME          CLASS   HOSTS   ADDRESS          PORTS   AGE
web-service   nginx   *       192.168.59.101   80      5h58m
```
To see the applications, open the IP address on the browser with the next paths http://IP/, http://IP/getTaskAnswer http://IP/elastic, http://IP/kibana

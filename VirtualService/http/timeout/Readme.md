docker build -t grs2docker2hub/istio-virtualserver-http-timeout .
docker image save -o image.tar grs2docker2hub/istio-virtualserver-http-timeout
minikube image load image.tar
rm -f image.tar

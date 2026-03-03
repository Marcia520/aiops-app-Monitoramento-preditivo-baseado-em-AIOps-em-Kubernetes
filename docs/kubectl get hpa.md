C:\>kubectl get hpa -n aiops-banco
NAME        REFERENCE                     TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
aiops-hpa   Deployment/aiops-deployment   cpu: <unknown>/70%   2         5         0          2d18h
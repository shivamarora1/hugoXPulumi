1. Make sure you have setup following environment variables:
```
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
export AWS_REGION=ap-south-1
```

2. 
```
cd pulumi-deployment
```

3. Make sure pulumi is installed in your system.
```
brew install pulumi/tap/pulumi
```

4. Apply the provisionings 
```
pulumi up
```

5. Open the url in your browser.
> This repository is a submission for the [Pulumi Deploy and Document Challenge](https://dev.to/devteam/announcing-the-pulumi-deploy-and-document-challenge-3000-in-prizes-887).<br>
> You can read the full submission article [here](https://dev.to/coder_dragon/deploy-hugo-website-to-amazon-s3-using-pulumi-43g2).


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

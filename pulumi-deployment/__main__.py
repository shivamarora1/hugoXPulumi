"""An AWS Python Pulumi program"""

import os
import pulumi
from pulumi_aws import s3
import mimetypes
import toml
import subprocess


####################
## Helpers functions...
####################
# def build_and_upload_website(endpoint: str):
#     print(endpoint)
#     build_website(endpoint)
#     local_folder = "../public"
#     uploadFolder(local_folder)


def build_website(website_addr):
    print(website_addr)
    with open("../hugo.toml", "r") as f:
        config = toml.load(f)
    config["baseURL"] = website_addr
    with open("../hugo.toml", "w") as f:
        toml.dump(config, f)

    os.chdir("../")
    result = subprocess.run(["hugo"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Failed to build hugo website: {result.stderr}")
        raise Exception(result.stderr)


# Upload files to AWS S3
def uploadFolder(folder_name: str):
    for root, dirs, files in os.walk(folder_name):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, folder_name)
            mime_type, _ = mimetypes.guess_type(file_path)
            s3.BucketObjectv2(
                relative_path,
                bucket=bucket.id,
                source=pulumi.FileAsset(file_path),
                key=relative_path,
                content_type=mime_type,
                acl="public-read",
                opts=pulumi.ResourceOptions(
                    depends_on=[public_access_block, ownership_controls, website]
                ),
            )


###################################
###################################
###################################
###################################


# Create an AWS resource (S3 Bucket)
bucket = s3.BucketV2("hugo-pulumi")

ownership_controls = s3.BucketOwnershipControls(
    "ownership-controls",
    bucket=bucket.id,
    rule={
        "object_ownership": "ObjectWriter",
    },
)

public_access_block = s3.BucketPublicAccessBlock(
    "public-access-block", bucket=bucket.id, block_public_acls=False
)

website = s3.BucketWebsiteConfigurationV2(
    "website",
    bucket=bucket.id,
    index_document={
        "suffix": "index.html",
    },
)

### * Need to wait before deployment...
website.website_endpoint.apply(lambda url: build_website("http://"+url))
uploadFolder("../public")

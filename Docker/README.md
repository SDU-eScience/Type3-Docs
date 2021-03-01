# Online Documentation

How to update and deploy the Type 3 user guide.

### Prerequisite

Log in to the eScience self-hosted registry:
```bash
docker login dreg.cloud.sdu.dk
```

### Procedure

Run the script `deploy_doc` to create the deployment pipeline:

1. Update the `master` branch.

2. Update metadata in the Dockerfile.

3. Build a new Docker image of the documentation website and tag it with the `<hash>` of the latest commit of `master`.

4. Push the new release `user-guide:<hash>` to the local Docker registry.

5. Commit local changes and push to the GitHub repository.

6. Create a tag `doc-<hash>` and push to the GitHub repository.

7. Push the changes to the `deployment` branch.

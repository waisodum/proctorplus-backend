import os
import pkg_resources

for dist in pkg_resources.working_set:
    location = dist.location
    size = sum(
        os.path.getsize(os.path.join(root, f)) for root, _, files in os.walk(location) for f in files
    )
    print(f"{dist.project_name}: {size / (1024 * 1024)} MB")

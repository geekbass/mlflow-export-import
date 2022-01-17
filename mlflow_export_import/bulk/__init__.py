import os
import json
from mlflow_export_import import utils
from mlflow_export_import.common import filesystem as _filesystem

def write_export_manifest_file(output_dir, duration, stages, notebook_formats, export_notebook_revision):
    manifest = utils.create_common_manifest(duration)
    manifest["stages"] = stages
    manifest["notebook_formats"] = notebook_formats
    manifest["export_notebook_revision"] = export_notebook_revision
    with open(os.path.join(output_dir, "manifest.json"), "w") as f:
        f.write(json.dumps(manifest, indent=2)+"\n")

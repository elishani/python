#!/usr/bin/env python

import tarfile
import os.path

def make_tarfile(output_filename, source_dir, app_version):
    app_tar = output_filename + app_version + ".tgz"
    print "\n*** Creating tar file '" + app_tar + "' from dirctory  '" + source_dir + "'\n"
    with tarfile.open(app_tar, "w:gz") as tar:
      tar.add(source_dir, arcname=os.path.basename(source_dir))
      
output_filename = "elishani"
source_dir = "/tmp/eli"
app_version = "10.2.3.4"

make_tarfile (output_filename, source_dir, app_version)

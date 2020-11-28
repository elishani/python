#!/usr/bin/env python

import tarfile
import os.path
import configparser
config = configparser.RawConfigParser()


def make_tarfile(tar_directory, output_filename, source_dir, app_version):
  app_tar = output_filename + "_" + app_version + ".tgz"
  app_dir = tar_directory + "/" + source_dir
  print "*** Creating tar file '" + app_tar + "' from dirctory  '" + app_dir + "'"
  with tarfile.open(app_tar, "w:gz") as tar:
    tar.add(app_dir, arcname=os.path.basename(app_dir))

def main():
  config_file = "/tmp/config.cfg"
  
  config.read(config_file)
  app_dict = dict(config.items("APP_VERSION"))
  dir_dict = dict(config.items("TAR_DIRECTORY")) 
  tar_dict = dict(config.items("TAR_FILES"))
    
  # Get application version
  for key in app_dict:
    app_version = app_dict[key]
  
  # Get tar directory
  for key in dir_dict:
    tar_directory = dir_dict[key]

  # Create tar files
  print "\n***** START creating tar files\n"
  for key in tar_dict:
    make_tarfile (tar_directory, tar_dict[key], key, app_version)
  print "\n***** END creating tar files"

if __name__ == '__main__':
  main()
    

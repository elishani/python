#!/usr/bin/env python

import tarfile
import os.path
import configparser
config = configparser.ConfigParser()
# config = configparser.RawConfigParser()

def make_tarfile(tar_directory, output_filename, source_dir, app_version):
  app_tar = output_filename + "_" + app_version + ".tgz"
  app_dir = tar_directory + "/" + source_dir
  print "*** Creating tar file '" + app_tar + "' from dirctory  '" + app_dir + "'"
  with tarfile.open(app_tar, "w:gz") as tar:
    tar.add(app_dir, arcname=os.path.basename(app_dir))

def main():
  config_file = "/tmp/config.cfg"
  config.read(config_file)
  app_ver = "application_version"
  dir_tar = "tar_directory"
  
  app_ver = config['APP_VERSION'][app_ver]
  dir_tar = config['TAR_DIRECTORY'][dir_tar]

  # Create tar files
  print "\n***** START creating tar files\n"
  for key in config['TAR_FILES']:
    make_tarfile (dir_tar, config['TAR_FILES'][key], key, app_ver)
  print "\n***** END creating tar files"

if __name__ == '__main__':
  main()

  print "\n***** START creating tar files\n"
  for key in tar_dict:
    make_tarfile (tar_directory, tar_dict[key], key, app_version)
  print "\n***** END creating tar files"

if __name__ == '__main__':
  main()

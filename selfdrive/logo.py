import os
import shutil

from openpilot.common.basedir import BASEDIR


def setup_bluepilot_logo(cls):
  bluepilot_boot_logo = f'{BASEDIR}/selfdrive/assets/images/black_bp.jpg'
  boot_logo_location = '/usr/comma/bg.jpg'
  boot_logo_save_location = f'{BASEDIR}/selfdrive/assets/images/backup_bg.jpg'
  
  remount_root = ['sudo', 'mount', '-o', 'remount,rw', '/']
  cls.run_cmd(remount_root, "File system remounted as read-write", "Failed to remount file system")

  if not os.path.exists(boot_logo_save_location):
    shutil.copy(boot_logo_location, boot_logo_save_location)
    print("Successfully backed up the original boot logo.")

  if not filecmp.cmp(bluepilot_boot_logo, boot_logo_location, shallow=False):
    copy_cmd = ['sudo', 'cp', bluepilot_boot_logo, boot_logo_location]
    cls.run_cmd(copy_cmd, "Successfully replaced bg.jpg with black_bp.jpg", "Failed to replace boot logo")

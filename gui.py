import os
import sys
import subprocess
from ffsubsync import ffsubsync
from gooey import Gooey

# CRITICAL: Tell ffsubsync to use the bundled FFmpeg inside the AppImage
if "APPDIR" in os.environ:
    ffmpeg_path = os.path.join(os.environ["APPDIR"], "usr", "bin")
    os.environ["PATH"] = ffmpeg_path + os.path.pathsep + os.environ["PATH"]

@Gooey(
    program_name="FFsubsync GUI",
    default_size=(600, 720),
    navigation="Tabbed"
)
def main():
    # We strip the first argument (the script name) so ffsubsync handles args correctly
    sys.argv[0] = 'ffsubsync'
    ffsubsync.main()

if __name__ == '__main__':
    main()

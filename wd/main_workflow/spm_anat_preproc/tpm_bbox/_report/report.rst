Node: spm_anat_preproc (tpm_bbox (utility)
==========================================


 Hierarchy : main_workflow.spm_anat_preproc.tpm_bbox
 Exec ID : tpm_bbox


Original Inputs
---------------


* function_str : def get_bounding_box(in_file):
    """ Retrieve the bounding box of a volume in millimetres."""

    # the imports must be inside if you want them to work in a nipype.Function node.
    from itertools import product

    import nibabel as nib
    import numpy as np

    img = nib.load(in_file)

    # eight corners of the 3-D unit cube [0, 0, 0] .. [1, 1, 1]
    corners = np.array(list(product([0, 1], repeat=3)))
    # scale to the index range of the volume
    corners = corners * (np.array(img.shape[:3]) - 1)
    # apply the affine transform
    corners = img.affine.dot(np.hstack([corners, np.ones((8, 1))]).T).T[:, :3]

    # get the extents
    low_corner = np.min(corners, axis=0)
    high_corner = np.max(corners, axis=0)

    return [low_corner.tolist(), high_corner.tolist()]

* in_file : /usr/local/MATLAB/R2014a/toolbox/matlab/spm12/tpm/TPM.nii


Execution Inputs
----------------


* function_str : def get_bounding_box(in_file):
    """ Retrieve the bounding box of a volume in millimetres."""

    # the imports must be inside if you want them to work in a nipype.Function node.
    from itertools import product

    import nibabel as nib
    import numpy as np

    img = nib.load(in_file)

    # eight corners of the 3-D unit cube [0, 0, 0] .. [1, 1, 1]
    corners = np.array(list(product([0, 1], repeat=3)))
    # scale to the index range of the volume
    corners = corners * (np.array(img.shape[:3]) - 1)
    # apply the affine transform
    corners = img.affine.dot(np.hstack([corners, np.ones((8, 1))]).T).T[:, :3]

    # get the extents
    low_corner = np.min(corners, axis=0)
    high_corner = np.max(corners, axis=0)

    return [low_corner.tolist(), high_corner.tolist()]

* in_file : /usr/local/MATLAB/R2014a/toolbox/matlab/spm12/tpm/TPM.nii


Execution Outputs
-----------------


* bbox : [[-90.0, -126.0, -72.0], [90.0, 90.0, 108.0]]


Runtime info
------------


* duration : 0.08442
* hostname : noobron08
* prev_wd : /home/noobron/rough/mri_pre_process
* working_dir : /home/noobron/rough/mri_pre_process/wd/main_workflow/spm_anat_preproc/tpm_bbox


Environment
~~~~~~~~~~~


* ANTSPATH : /opt/ANTs/bin/
* CLICOLOR : 1
* CLUTTER_IM_MODULE : xim
* COLORTERM : truecolor
* CONDA_EXE : /home/noobron/anaconda3/bin/conda
* CONDA_PYTHON_EXE : /home/noobron/anaconda3/bin/python
* CONDA_SHLVL : 0
* DBUS_SESSION_BUS_ADDRESS : unix:path=/run/user/1000/bus,guid=9ed3de2aa4dbdab80083bba15fe74706
* DBUS_STARTER_ADDRESS : unix:path=/run/user/1000/bus,guid=9ed3de2aa4dbdab80083bba15fe74706
* DBUS_STARTER_BUS_TYPE : session
* DEFAULTS_PATH : /usr/share/gconf/ubuntu.default.path
* DESKTOP_SESSION : ubuntu
* DISPLAY : :0
* GDMSESSION : ubuntu
* GIT_PAGER : cat
* GNOME_DESKTOP_SESSION_ID : this-is-deprecated
* GNOME_SHELL_SESSION_MODE : ubuntu
* GNOME_TERMINAL_SCREEN : /org/gnome/Terminal/screen/5ac8b324_5c54_4991_984c_242f89d8d80d
* GNOME_TERMINAL_SERVICE : :1.204
* GPG_AGENT_INFO : /run/user/1000/gnupg/S.gpg-agent:0:1
* GTK_IM_MODULE : ibus
* GTK_MODULES : gail:atk-bridge
* HOME : /home/noobron
* IM_CONFIG_PHASE : 2
* INVOCATION_ID : 55d45d7beee84523b5c9dbc65ea70c59
* JOURNAL_STREAM : 9:42624
* JPY_PARENT_PID : 11171
* KERNEL_LAUNCH_TIMEOUT : 40
* KMP_DUPLICATE_LIB_OK : True
* KMP_INIT_AT_FORK : FALSE
* LANG : en_IN
* LANGUAGE : en_IN:en
* LESSCLOSE : /usr/bin/lesspipe %s %s
* LESSOPEN : | /usr/bin/lesspipe %s
* LOGNAME : noobron
* LS_COLORS : rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
* MANAGERPID : 4675
* MANDATORY_PATH : /usr/share/gconf/ubuntu.mandatory.path
* MPLBACKEND : module://ipykernel.pylab.backend_inline
* PAGER : cat
* PATH : /opt/ANTs/bin/:/home/noobron/anaconda3/condabin:/home/noobron/.local/bin:/home/noobron/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/noobron/.dotnet/tools
* PWD : /home/noobron/rough/mri_pre_process
* QT4_IM_MODULE : xim
* QT_ACCESSIBILITY : 1
* QT_IM_MODULE : ibus
* SESSION_MANAGER : local/noobron08:@/tmp/.ICE-unix/4712,unix/noobron08:/tmp/.ICE-unix/4712
* SHELL : /bin/bash
* SHLVL : 1
* SSH_AGENT_PID : 4812
* SSH_AUTH_SOCK : /run/user/1000/keyring/ssh
* TERM : xterm-color
* TEXTDOMAIN : im-config
* TEXTDOMAINDIR : /usr/share/locale/
* USER : noobron
* USERNAME : noobron
* VTE_VERSION : 5202
* WINDOWPATH : 2
* XAUTHORITY : /run/user/1000/gdm/Xauthority
* XDG_CONFIG_DIRS : /etc/xdg/xdg-ubuntu:/etc/xdg
* XDG_CURRENT_DESKTOP : ubuntu:GNOME
* XDG_DATA_DIRS : /usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
* XDG_MENU_PREFIX : gnome-
* XDG_RUNTIME_DIR : /run/user/1000
* XDG_SEAT : seat0
* XDG_SESSION_DESKTOP : ubuntu
* XDG_SESSION_ID : 2
* XDG_SESSION_TYPE : x11
* XDG_VTNR : 2
* XMODIFIERS : @im=ibus
* ZEITGEIST_DATA_PATH : /home/noobron/.local/share/zeitgeist
* _ : /home/noobron/.local/bin/jupyter
* _CE_CONDA : 
* _CE_M : 


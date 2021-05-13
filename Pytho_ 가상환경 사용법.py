# pip install
  # open cmd/powershell/...
  # check current dir is [project path]\Scripts
  # type activate
  # if you just make this venv dir, type python pip install --upgrade pip
  # if you already made this venv dir or after upgrade pip, type pip install [packages that you want]
  # type deactivate
  # type exit

# vscode
  # open Scripts folder or open [project path] folder move Scripts using command prompt in VScode
    #after make [newfile].py in [project path]\Scripts Folder, write down codes you want to run and save that
  # terminal in VScode should swap powershell to command prompt
    #check current dir is [project path]\Scripts
    #check command prompt show ([project dir name]) [project path]\Scripts
    #type activate
    #if you want to run specific python file, type python [newfile/specific name].py
    #once you edited [newfile].py in VScode, press ctrl/cmd+s
    #click activate terminal(which is command prompt), press ⬆. Then the terminal show us last command that you typed just before.
  # deactivate

# jupyter
  # open cmd/powershell/terminal/...
  # check current dir is [project path]\Scripts
  # type activate
  # type pip install jupyter
  # type jupyter notebook
    # while using jupyter, you shouldn't exit/close cmd/powershell/terminal/...
  # if jupyter dosen't work, type ipython profile create
    # type jupyter notebook
  # after using jupyter, exit cmd/powershell/terminal/...

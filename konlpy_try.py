from konlpy.tag import Okt

okt=Okt()
print(okt.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))

print(okt.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))

#방법(windows기준__)
# 설정에서 본인 컴퓨터 버전을 확인->64bit면 64bit으로 install(Python 3.7.5) 우클릭 관리자 권한으로 실횅
    # 설치방법 1. custermize installation 혹시 Add Python 3.7 to PATH에 체크되어있다면 해제(이미 3.9가 설치된 뒤 경로 설정이 되었기 때문) 
            # 2. for all user로 설치하면 적당하게 설정됨
            # 3. 저장 경로를 본인이 편한 위치에 설정하고 경로는 메모하기(예) c:\Program Files\Python37)
# cmd(관리자 권한으로 연 뒤) 가상환경을 설정할 위치로 바꿈 cd ../../ cd ./등을 활용
# 이후부터 '>' 뒤의 내용이 cmd 입력한 명령어임 
# > python -m venv [가상환경 구성하고 싶은 폴더 경로]
    #대괄호는 빼고 경로만 입력
    # -->해당 폴더 존재하지 않으면, 파이썬이 알아서 가상환경 구상
    # 윈도우라면 해당 폴더 내에, Scripts폴더가 생성되었을 것이고, Mac이라면 해당 폴더 내에 bin폴더가 생성됨
# > cd ./Scripts
# > activate
    #하면 (가상환경폴더명)가상환경경로>Scripts로 활성화된 창이 보임
# vscode에서 해당 폴더를 연 뒤, pyvenv.cfg파일 열기
                    # home = [python폴더경로] #예) C:\Program Files\Python37
                    # include-system-site-packages = false
                    # version = 3.7.5
# 저장 한 뒤, 다시 vscode에서 Scripts 폴더 내의 activate 파일을 열기
                    # # unset irrelevant variables
                    # deactivate nondestructive

                    # VIRTUAL_ENV="[가상환경폴더경로]"  #예) "C:\nlpcrawling"
                    # export VIRTUAL_ENV

                    # _OLD_VIRTUAL_PATH="[python37경로]" #예) "C:\Program Files\Python37"
                    # PATH="[python37\Scripts]" #예)"C:\Program Files\Python37\Scripts"
                    # export PATH
# 저장 한 뒤, 다시 vscode에서 Scripts 폴더 내의 activate.bat 파일을 열기    #참고) activate.bat이 cmd에서 구동되는 것임
                    # set VIRTUAL_ENV=[가상환경폴더경로]    #예) C:\nlpcrawling

                    # if not defined PROMPT set PROMPT=$P$G

                    # if defined _OLD_VIRTUAL_PROMPT set PROMPT=%_OLD_VIRTUAL_PROMPT%
                    # if defined _OLD_VIRTUAL_PYTHONHOME set PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%

                    # set _OLD_VIRTUAL_PROMPT=%PROMPT%
                    # set PROMPT=(가상환경폴더명) %PROMPT%  #예) nlpcrawling

                    # if defined PYTHONHOME set _OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%
                    # set PYTHONHOME=[python37경로] #예) C:\Program Files\Python37
# 저장 한 뒤, 다시 vscode에서 Scripts 폴더 내에 pip3.9.exe가 있다면 pip3.7.exe로 이름변경                    
# JDK(google에 java development 8 검색) 윈도우 버전에 맞게끔 설치(경로 메모 후)
# 고급 시스템 설정->환경변수->시스템 변수의 Path를 편집->새로만들기->경로 추가
    # 예) C:\Program Files\Java\jdk1.8.0_291\bin
# 고급 시스템 설정->환경변수->시스템 변수에 새로 만들기
    # 변수명 JAVA_HOME  #경로예시) C:\Program Files\Java\jdk1.8.0_291
# 아까 activate한 cmd창에서
# > pip install --upgrade pip
# > pip install JPype1==1.2.0 konlpy
    # 이렇게 하면 가상환경 내의 Lib\site-package에 설치됨
# VScode에서 가상환경폴더의 Scripts폴더 안에 test.py생성
    # 강사님 교안 참고해서 코드 작성
# terminal은 powershell이 아닌 cmd에서 작동시켜야 함
    # > activate
    # > python test.py

# 해당 내용은 강의실 컴퓨터를 기준으로 작성되었으며, PC 사양 및 python 및 JDK 설치 위치, 가상환경폴더 경로에 따라 달라질 수 있습니다.
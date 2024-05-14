from pathlib import Path

desktop = Path().home().joinpath("Desktop")
pics = Path().home().joinpath('Pictures')
onedrivePy = Path().home().joinpath('OneDrive').joinpath('PY')
onedriveJs = Path().home().joinpath('OneDrive').joinpath('JS')
words = Path().home().joinpath('Documents').joinpath('.words')


# desktop.joinpath('WORDS').mkdir(exist_ok=True)
# desktop.joinpath('JAVASCRIPT').mkdir(exist_ok=True)
# desktop.joinpath('PYTHON').mkdir(exist_ok=True)
# desktop.joinpath('APPS').mkdir(exist_ok=True)
# desktop.joinpath('PHOTOS').mkdir(exist_ok=True)

for path in desktop.iterdir():
    num = 0
    if path.name == "DTCLEAN.py" or path.name == "desktop.ini":
        uhh = 1
    elif '.txt' in path.name:
        while True:
            count = 0
            for file in words.iterdir():
                if path.name[0:-4] + f'{num}' + '.txt' == file.name:
                    count += 1
            if count != 0:
                num += 1
            else:
                path.replace(words.joinpath(path.name[0:-4] + f'{num}' + '.txt'))
                break
    elif '.js' in path.name:
        while True:
            count = 0
            for file in onedriveJs.iterdir():
                if path.name[0:-3] + f'{num}' + '.js' == file.name:
                    count += 1
            if count != 0:
                num += 1
            else:
                path.replace(onedriveJs.joinpath(path.name[0:-3] + f'{num}' + '.js'))
                break
    elif '.py' in path.name:
        while True:
            count = 0
            for file in onedrivePy.iterdir():
                if path.name[0:-3] + f'{num}' + '.py' == file.name:
                    count += 1
            if count != 0:
                num += 1
            else:
                path.replace(onedrivePy.joinpath(path.name[0:-3] + f'{num}' + '.py'))
                break
    elif '.exe' in path.name:
        print('MOVE ME TO APPS')
    elif '.png' in path.name:
        while True:
            count = 0
            for file in pics.iterdir():
                if path.name[0:-4] + f'{num}' + '.png' == file.name:
                    count += 1
            if count != 0:
                num += 1
            else:
                path.replace(pics.joinpath(path.name[0:-4] + f'{num}' + '.png'))
                break




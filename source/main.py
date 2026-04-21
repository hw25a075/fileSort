from pathlib import Path
from collections import defaultdict

raw = input("ディレクトリパスを入力してください: ")
path = Path(raw)

docs = defaultdict(list)
dirs = []


print(raw.strip())

if not raw.strip(): print("空文字です") # 何も受け取らなかった時
elif not path.exists(): print("存在しません") # 受け取った文字列がファイルパスとして存在しない時
elif not path.is_dir(): print("ディレクトリではありません") # 受け取った文字列がファイルを指定していた時
else: # その他
    print("有効です")
    print("実行するファイルパス",path)
    print("実行するファイルパス.resolve()",path.resolve())

    for files in sorted(path.iterdir()):
        
        if  files.is_dir():
            print("ディレクトリ".ljust(16),files)
            dirs.append(files)
        else:
            print(files.suffix.ljust(16),files.name)
            suffix = files.suffix
            docs[suffix].append(files)


    active = None

    while active == None:

        permission = input("ファイル整理を実行しますか y/n")
        if permission == "y":
            active = True
            print("処理を行います")
            for i in dirs:
                print(i)
            for suffix, files in docs.items():

                name = suffix.replace(".","") or "no_extension"
                new_dir = path / name
                new_dir.mkdir(exist_ok=True)

                print(f"\n拡張子: {suffix}")
                print(new_dir)

                for f in files:

                    new_path = new_dir / f.name
                    f.rename(new_path)

                    print("    ",f.name)
                    print(new_path)
            print("完了")
        elif permission == "n":
            active = False
            print("処理を行いません\n終了します")
        else:
            print("無効な文字列")
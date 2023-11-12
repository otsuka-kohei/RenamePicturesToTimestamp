# RenamePicturesToTimestamp
## 概要
写真ファイルのファイル名を撮影日時にリネームします。  
引数で渡したディレクトリにある写真ファイルをすべてリネームします。  
連写撮影した写真は撮影日時が衝突することがあるので、撮影日時の後に元のファイル名が続きます。  
Python 3系で使用してください。  
例：7M400001.ARW => 2023-02-23_12-53-12_7M400001.ARW  
## 動作確認済みファイル形式
### 処理可能
- JPEG
- DNG
- ARW
- HIF (macOS上で実行する場合)
### 処理不可能
macOS以外の環境では以下の形式のファイルを処理することができません。
- HIF（ソニーαシリーズで撮影）
## 使用方法
python rename_picture_files_to_timestamp.py [写真ファイルを配置したパス]  
例：python ./rename_picture_files_to_timestamp.py ./pictures

## Summary
This program renames photo files to shooing date and time.  
This program renames all photo files in a directory that selected as argument.  
Original file name is appended after shooting date and time because shooting date and time can conflict when drive mode is used.  
Please use this program with Python 3.  
Example: 7M400001.ARW => 2023-02-23_12-53-12_7M400001.ARW  
## Tested file formats
### Processable
- JPEG
- DNG
- ARW
- HIF　(only when run this programm on macOS)
### Not processable
This program cannot process files of below format on other than macOS.
- HIF (taken by Sony α series)
## How to use
python rename_picture_files_to_timestamp.py [picture files directory path]  
Example: python ./rename_picture_files_to_timestamp.py ./pictures

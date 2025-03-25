# 使用方法
1. 將job產的yaml檔貼到與程式相同的路徑底下，以【job name】命名
2. 修改settings.ini的section最後的job name，前面的resources.jobs請勿修改，要與yaml檔名相同，不然會替換失敗
如果是執行檔請參考3.1，如果是執行python請參考3.2
3.1 直接執行exe，理論上會直接替換有在setting.ini中設定的值
3.2 確認python執行環境有ruamel.yaml套件後執行python(python main.py)
4. 執行後會產生job name.yml，再將這份檔案上傳到TFS

# 備註
* setting.ini、default.yml為必要存在
* 如果有多個Job要修改，可以直接新增一個section
* 如果找不到key值會直接跳過
* 米字號代表會替換掉該Array中所有有找到該key的值，如果不想全部替換就需要指定數字
* 如果有其他結構的yaml檔也可以使用，但要注意yaml檔的階層關係

pyinstaller --onefile main.py

# 使用方法
**dist中包含執行檔、settings.ini、範例yaml檔**
1. 將job產的yaml檔貼到與程式相同的路徑底下，以【job name】命名
2. 修改settings.ini的section最後的job name，前面的resources.jobs請勿修改，要與yaml檔名相同，不然會替換失敗
![image](https://github.com/user-attachments/assets/851c3907-7357-492e-a613-effb0a974962)
3. 直接執行exe，理論上會直接替換有在setting.ini中設定的值
4. 執行後會更新job name.yml，再將這份檔案上傳到TFS

# 備註
* 也可以使用python執行(python main.py)，但需確認有安裝必要套件(ruamel.yaml)
* setting.ini、job name.yml為必要存在
* 如果有多個Job要修改，可以直接新增一個section
* 如果找不到key值會直接跳過
* 米字號代表會替換掉該Array中所有有找到該key的值，如果不想全部替換就需要指定數字
* 如果有其他結構的yaml檔也可以使用，但要注意yaml檔的階層關係
* 打包語法：pyinstaller --onefile main.py

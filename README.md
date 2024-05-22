# Django Application - BMI
## 設計一個表單，可以輸入一群人的姓名、身高、體重。提交後會存到資料庫中，並進行下一筆資料的輸入。
### 需求：
- 點選統計：會呈現 BMI 過高的人、過低的人、以及正常的人的資訊。
- 點選繼續編輯：會回到編輯表單繼續加入資料
- 點選隨機輸入：會隨機輸入10筆資料，包含姓名身高體重等，都透過亂數輸入一些合理的值。(建議設計姓與名的詞典，組合出有意義的名字)

### 常用指令 1：

    // 建立虛擬環境
    py -m venv myworld

    // 啟動虛擬環境
    myworld\Scripts\activate.bat

    // 安裝 Django
    py -m pip install Django

    // 建立專案
    django-admin startproject my_tennis_club

    // 啟動伺服器
    py manage.py runserver

### 常用指令 2：

    // 把專案複製到你的電腦
    git clone https://github.com/nienlinh/vh5000.git

    // 檢查一下目前在的版本
    git branch

    // 切換到 dj01a 版本
    git checkout dj01a

    // 啟動伺服器
    python manage.py runserver

    // 切換到 dj03 版本
    git checkout dj03

    // 安裝 Pillow 套件
    python -m pip install Pillow

    // 啟動伺服器
    python manage.py runserver
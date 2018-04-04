# django_udemy

## Project Start
```
$django-admin startproject <ProjectName>
```

## RunServer
```aidl
$python manage.py runserver
```

## settings.py
LANGUAGE_CODE = 'en-us' -> 'ja'
TIME_ZONE = 'UTC' -> 'Asia/Tokyo'

## Migration
```aidl
$python manege.py migrate
```

## Applicationの作成
```aidl
$python manege.py startapp <App>
```
controller,view,modelなどを含むディレクトリが作成される
settings.pyのINSTALLED_APPSにAPPを追加

### PATHの設定
- プロジェクト全体のurls.pyとAPPごとのurls.pyがある
- ApplicationごとにPATHを指定する場合
-- 作成したappにurls.py追加
```
from django.urls import path
urlpatterns = [path('',views.index)]
```
-- プロジェクトのurls.pyには以下を追加
```aidl
from django.urls import path,include
urlpatterns = [
    path('crawl/', include('<app名>.urls',namespace='crawl')),
]
```

- includeを書かないで設定することも
```aidl
from <app> import <action>
```

- プロジェクトのurls.py


## テンプレートファイルの作成
- <app>直下にtemplates/<app名>フォルダを作成し、htmlファイル作成
- views.pyにrender(request,<app名>/<htmlファイル>)


## モデルの作成
- <app>直下のmodels.py
- modelsのFieldを用いて項目を記述する
作成後以下を実行
- マイグレーションファイルの作成
```aidl
$python manage.py makemigrations
```
- migrate
```aidl
$python manage.py migrate
```

## superuserの作成
```
$python manage.py createsuperuser
```
その後,アプリのadmin.pyに管理画面の設定を記述

## templateengine
- ModelとViewをつなぐもの

---

## Links

[画像の表示について](http://www.tohuandkonsome.site/entry/2017/06/10/211145)

---

## SQLite
```aidl
$sqlite3 db.sqlite3
```
- テーブル一覧
```aidl
.tables
```



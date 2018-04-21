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

## form
- <app名>/forms.pyを作成
```
from django.forms import ModelForm
from cms.models import Book


class BookForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Book
        fields = ('name', 'publisher', 'page', )
```
[qiita](https://qiita.com/kaki_k/items/6e17597804437ef170ae)

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

# MySQL
```
CREATE USER user IDENTIFIED BY [PASSWORD] 'password';
```
```
GRANT 権限 ON レベル TO user;
```

## heroku
[qiita](https://qiita.com/Shitimi_613/items/6627d0ce042d38b86893)
- Procfileでプロジェクト名を書き換える
- runtaime.txtは最新のpython verを指定

- import 
```aidl
$ mysql --host=HOST --user=USER_NAME --password=PASSWORD --reconnect DB_NAME < backup.sql
```
- export
```aidl
mysqldump -uUSER_NAME -pPASSWORD -h HOST -r backup.sql --single-transaction DB_NAME
```
[sequel pro](http://hhmmm.hateblo.jp/entry/2016/02/15/204638)

[musqlを使う方法](https://qiita.com/maez/items/c7fe024b3b8de1dedbcd)

## postgres
サーバ起動
```aidl
postgres -D /usr/local/var/postgres
```

ログイン
```aidl
psql postgres
```

テーブル情報
```aidl
\l : DB一覧
\c [DB名]: DB切り替え
\d : テーブル一覧
\q : psql終了
```

認証方法の変更(初回のみ)
https://b.pyar.bz/20141021/mac-postgresql-installation/
を参考に以下のファイルを変更
/usr/local/var/postgres/pg_hba.conf


ユーザ作成
```aidl
createuser -P <user-name>
```

DB作成
```aidl
createdb example-db -O <pg-user>
```


## Error
- CSS読み込めない
```
STATIC_URL = '/static/'

# Additional locations of static files
ROOT_PATH = os.path.dirname(__file__)
STATICFILES_DIRS = (
    [os.path.join(ROOT_PATH, 'static')]
)
```

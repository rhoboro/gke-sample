# GKEのサンプル

* all.yamlのYOUR_PROJECT_IDを自分のGCPプロジェクトIDに変更する。

```bash
# nginxディレクトリ
$ docker build -t gcr.io/YOUR_PROJECT_ID/app-nginx:0.1 .
$ gcloud docker -- push gcr.io/YOUR_PROJECT_ID/app-nginx:0.1
# appディレクトリ
$ docker build -t gcr.io/YOUR_PROJECT_ID/app:0.1 .
$ gcloud docker -- push gcr.io/YOUR_PROJECT_ID/app:0.1
# クラスタ作成
$ gcloud container clusters create app-gke --zone asia-northeast1-a --machine-type n1-standard-2
# 認証情報取得
$ gcloud container clusters get-credentials app-gke
# リソースの作成
$ kubectl create -f all.yaml
```

* Clean up

```
$ kubectl delete -f all.yaml
$ gcloud container clusters delete app-gke
```

# Slackバックアップビューア (作成中)

このアプリはSlackのバックアップビューアです。
よるにSlackのAPIで高階チャンネルの投稿内容を取得します。
取得したものが画面で閲覧できる予定

私物のMacの容量が足りなくなったり諸々あって開発を一旦ストップしていた
そしてそのままフェードアウト中・・・

## コンテナ構成

* app
  * 画面。next.jsで実装。作りかけ
* slackapi
  * 内部API (WebAPI)
* scheduler
  * Slackのログ収集用ロガー
  * 3時30分にログの書き出しを実行します
* MySQL
  * デイリーバックアップを管理するテーブル
* redis
  * Redisコンテナを作成するためのDockerfile
  * いま時点では特に使っていない

## インストール方法

1. .envの作成
  * .env.defaultをコピーして.envを作成してください
  * 作成した.envに各種情報を埋め込んでください
2. `docker-compose build`を実行する
  * `docker-compose build`を実行してコンテナを生成してください
3. `マイグレーション`
  * `docker-compose run --rm slackapi bash`を実行してください
  * 少しの時間お待ち下さい (MySQLのセットアップが走るため)
  * `flask db upgrade`を実行してください
  * 完了後、`exit`でslackapiから抜けてください
4. サービス起動
  * `docker-compose up -d`でアプリを起動してください
5. UI起動
  * UIはまだ完成していないので、`docker-compose exec app bash`を実行後に`yarn install / yarn dev`を実行



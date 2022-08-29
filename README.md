# Stock List

## やりたいこと

pythonからgoogle spleadsheetを操作してウェブ上で表示する

## やったこと

1. Google Cloud Platformの操作
   1. Google Cloud Platformにプロジェクトを作成する
   2. Google Drive APIを有効にする(APIライブラリ>Google Drive API)
   3. Google Sheets APIを有効にする(APIライブラリ>Google Sheets API)
   4. OAuth
      1. 認証情報を作成(APIライブラリ>認証情報>+認証情報を作成 / role:Project IAM 管理者？)
      2. 秘密鍵を作成
2. Spread Sheetの共有を変更
   1. GCPで作成したロールのアドレスにシートの共有を設定する

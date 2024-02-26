
# ディレクトリ説明

data: 画像データやcsvデータを保存するディレクトリ。中には以下のフォルダが含まれています。

- csv: csvデータを保存するディレクトリ。
- img: 画像データを保存するディレクトリ。中にはラマンイメージを格納する`raman_img`、スペクトルグラフを格納する`spectrum_graph`が含まれています。

src: ソースコードを保存するディレクトリ。中には以下のファイルが含まれています。

- raman.py: 実行ファイル
- RamanSpectrumClass.py: クラス定義ファイル

# 使い方

```bash
python src/raman.py <img_path> <spectrum_output_name> [<csv_path> <processed_output_name>]
```

のようにして使います。[]で囲まれた引数は、smoothingやdenoiseを行いたい場合のみに使います。

各引数の説明は以下の通りです。

- `<img_path>`: 入力画像のパス。例えば`test.jpg`など。
- `<spectrum_output_name>`: スペクトルのグラフ (pngファイル) の出力ファイル名。例えば`test`など。勝手に`.png`が付きます。
- `<csv_path>`: smoothingやdenoiseを行いたいデータ (csvファイル) のパス。例えば`test.csv`など。
- `<processed_output_name>`: 処理後のスペクトルの数値データ (csvファイル) の出力ファイル名。例えば`test`など。勝手に`.csv`が付きます。

# 使用例

```bash
python src/raman.py test.jpg test test.csv test
```

```bash
python src/raman.py test.jpg test
```

以上の2通りのいずれかの使い方をしてください。誤った使い方の場合、エラーが出ます。

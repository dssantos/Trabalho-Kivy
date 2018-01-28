# Requisitos

[Kivy e dependências](https://kivy.org/docs/installation/installation.html)
[Buildozer](https://kivy.org/docs/guide/packaging-android.html)
[Plyer](https://github.com/kivy/plyer) - pip install plyer

# Para gerar os arquivos \.apk:

1. Edite o arquivo [buildozer.spec]() existente em cada pasta e definir as seguintes variáveis, conforme o seu ambiente:
* android.ndk_path (caminho do NDK do android)
* android.sdk_path (caminho do SDK do android)
* android.ant_path (caminho do Apache Ant)
* p4a.source_dir (caminho do Python-for-android)
* build_dir (local onde será salvo todos os arquivos de dependências caso os caminhos citados acima não tenham sido definidos)
* bin_dir (local onde o \.apk será salvo)
Obs: Alternativamente, você pode comentar estas linhas, no entanto, o buildozer utilizará os valores default e realizará o download dos arquivos na pasta \.buildozer do seu home.

2. Dentro da pasta do aplicativo execute o comando buildozer -v android debug deploy run

3. Se tudo der certo, o arquivo .apk estará na pasta que você definiu na variável "bin_dir" do arquivo buildozer.spec ou caso tenha comentado na pasta \./bin do aplicativo.



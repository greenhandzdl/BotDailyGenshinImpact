# BotDailyGenshinImpact

## Préréquis
- Avoir installé le gestionnaire de paquets PIP
- Avoir installé le langage de programmation Python3

## Préparation
+ Récuperer la version de votre navigateur web préféré et le mettre dans votre répetoire Git

| Navigateur web | Lien |
| ------ | ------ |
| Chrome: | [https://sites.google.com/a/chromium.org/chromedriver/downloads] |
| Edge: | [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/] |
| Firefox: | [https://github.com/mozilla/geckodriver/releases] |
| Safari: | [https://webkit.org/blog/6900/webdriver-support-in-safari-10/]|

+ Aller sur le site hoyolab, connectez-vous puis récuperer le dossier /tmp/tarun et le mettre dans votre répetoire Git
https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=fr-fr

## Lancement 
+ Créer un environnement virtuel
    ```sh
    ./create_venv.sh
    ```
+ Configurer votre Crontab en remplaçant {PathRun} par le chemin absolue de votre répetoire Git
    ```sh
    crontab -e
    ```
    ```sh
    # Edit this file to introduce tasks to be run by cron.
    # 
    # Each task to run has to be defined through a single line
    # indicating with different fields when the task will be run
    # and what command to run for the task
    # 
    # To define the time you can provide concrete values for
    # minute (m), hour (h), day of month (dom), month (mon),
    # and day of week (dow) or use '*' in these fields (for 'any').# 
    # Notice that tasks will be started based on the cron's system
    # daemon's notion of time and timezones.
    # 
    # Output of the crontab jobs (including errors) is sent through
    # email to the user the crontab file belongs to (unless redirected).
    # 
    # For example, you can run a backup of all your user accounts
    # at 5 a.m every week with:
    # 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
    # 
    # For more information see the manual pages of crontab(5) and cron(8)
    # 
    # m h  dom mon dow   command
    00 18    * * * XDG_RUNTIME_DIR=/run/user/$(id -u) {PathRun}/run
    ```

### Copyright

(c) 2021, Nicolas DOLPHIN  (nicolas974dolphin@gmail.com)
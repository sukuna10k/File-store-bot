# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "24817837"))
	API_HASH = os.environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "7444104773:AAHlixOqe26mJ2lMBc3ck27Cvx2stK9y0iA")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "FelixFlixBot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002491166640"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "7428552084"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://FELIX:antiflix@felix.szbiv.mongodb.net/?retryWrites=true&w=majority&appName=Félix")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002265513823")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002376378205")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
Ceci est un bot de stockage de fichiers permanents ! Envoyez-moi n'importe quel fichier, je l'enregistrerai dans ma base de données. Il fonctionne également pour les canaux. Ajoutez-moi au canal en tant qu'administrateur avec des droits de modification, j'ajouterai l'option "Enregistrer le fichier téléchargé dans le canal" et un bouton de lien partageable.

🤖 **Mon Nom:** [FélixFlix Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hébergé sur:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developeur:** @Kingcey

👥 **Support Group:** [Bot Support](https://t.me/bot_Kingdot)

📢 **Updates Channel:** [AnitiFlix](https://t.me/AntiFlix_A)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @Kingcey

Le développeur est un super débutant. Il apprend juste à partir des documents officiels. Veuillez faire un don au développeur pour maintenir le service en vie.

N'oubliez pas que le développeur supprimera les contenus pour adultes de la base de données. Il vaut donc mieux ne pas stocker ce genre de choses.

[Donnez maintenant](https://www.paypal.me/Kingcey) (Par Mobile)
"""
	HOME_TEXT = """
Salut, [{}](tg://user?id={})\n\nCeci est un bot de stockage de fichiers permanents.

Envoyez-moi n'importe quel fichier, je vous fournirai un lien partageable permanent. Je prends également en charge les canaux ! Vérifiez le bouton **"À propos".**
"""

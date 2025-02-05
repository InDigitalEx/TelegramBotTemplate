# TelegramBotTemplate

Telegram bot project template

## Technology Stack and Features

- 🔮 [Aiogram](https://aiogram.dev/) for asynchronous framework for Telegram Bot API
- 📦 [SQLAlchemy](https://www.sqlalchemy.org/) for database management
- 🗃️ [Pydantic](https://pydantic.dev/) for a convenient project setup system via config
- 🐋 [Docker](https://www.docker.com) for development and production.

## How To Use It

✨It Works Using Superpower✨

### Instruction for installation

- Create a new GitHub repo, for example `MyTelegramBot`.
- Clone this repository manually, set the name with the name of the project you want to use, for example `MyTelegramBot`:

```bash
git clone git@github.com:InDigitalEx/TelegramBotTemplate.git MyTelegramBot
```

- Enter into the new directory

```bash
cd MyTelegramBot
```

- Set the new origin to your new repository, copy it from the GitHub interface, for example:

```bash
git remote set-url origin git@github.com:your_name/MyTelegramBot.git
```

- Add this repo as another "remote" to allow you to get updates later:

```bash
git remote add upstream git@github.com:InDigitalEx/TelegramBotTemplate.git
```

- Push the code to your new repository:

```bash
git push -u origin main
```

### Update From the Original Template

After cloning, you will need to fetch the changes from the template repository.

- Make sure you have added this repository as remote, you can check it with:

```bash
git remote -v

origin    git@github.com:your_name/MyTelegramBot.git (fetch)
origin    git@github.com:your_name/MyTelegramBot.git (push)
upstream    git@github.com:InDigitalEx/TelegramBotTemplate.git (fetch)
upstream    git@github.com:InDigitalEx/TelegramBotTemplate.git (push)
```

- Pull the latest changes without merging:

```bash
git pull --no-commit upstream main
```

### Configure
You can set the config in the `config` file to customize them to your choice

Before starting for the first time, be sure to configure the following settings:

- `BOT_TOKEN` - Bot token, which you can get from `@BotFather` bot in telegram

If you have done this, then proceed to create a virtual Python environment:

#### Step 1. Install virtualenv

```bash
pip install virtualenv
```

#### Step 2. Install environment

Go to the project root folder and write:

```bash
virtualenv .venv
```

#### Step 3. Activate environment

For Windows:

```bash
.venv\Scripts\activate.bat
```

For Linux:

```bash
source .venv/bin/activate
```

#### Step 4. Install dependencies

Go to the project root folder (if you are not there) and write:

```bash
pip install -r requirements.txt
```

#### Step 5. Run the bot
```bash
python3 run.py
```

After starting the bot, you can test it with the `/start` command.
Send it to the bot you pre-configured with `@BotFather`.
If you did everything correctly, you will receive a welcome message

## Release Notes

Check the file [release-notes.md](./release-notes.md).

## License

Telegram Bot Template is licensed under the terms of the GPL-3.0 License.
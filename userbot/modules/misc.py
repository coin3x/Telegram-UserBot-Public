# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD

""" Userbot module for other small commands. """

from random import randint
from time import sleep

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.random")
async def randomise(items):
    """ For .random command, get a random item from the list of items. """
    if not items.text[0].isalpha() and items.text[0] not in (
            "/", "#", "@", "!"):
        itemo = (items.text[8:]).split()
        index = randint(1, len(itemo) - 1)
        await items.edit("**Query: **\n`" + items.text[8:] + "`\n**Output: **\n`" + itemo[index] + "`")


@register(outgoing=True, pattern="^.sleep( [0-9]+)?$")
async def sleepybot(time):
    """ For .sleep command, let the userbot snooze for a few second. """
    message = time.text
    if not message[0].isalpha() and message[0] not in ("/", "#", "@", "!"):
        if " " not in time.pattern_match.group(1):
            await time.reply("Syntax: `.sleep [seconds]`")
        else:
            counter = int(time.pattern_match.group(1))
            await time.edit("`I am sulking and snoozing....`")
            sleep(2)
            if BOTLOG:
                await time.client.send_message(
                    BOTLOG_CHATID,
                    "You put the bot to sleep for " + str(counter) + " seconds",
                )
            sleep(counter)


@register(outgoing=True, pattern="^.shutdown$")
async def killdabot(event):
    """ For .shutdown command, shut the bot down."""
    if not event.text[0].isalpha():
        await event.edit("`Goodbye *Windows XP shutdown sound*....`")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#SHUTDOWN \n"
                "Bot shut down")
        await event.client.disconnect()


@register(outgoing=True, pattern="^.support$")
async def bot_support(wannahelp):
    """ For .support command, just returns the group link. """
    if not wannahelp.text[0].isalpha(
    ) and wannahelp.text[0] not in ("/", "#", "@", "!"):
        await wannahelp.edit("Link Portal: @userbot_support")


@register(outgoing=True, pattern="^.repo$")
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    if not wannasee.text[0].isalpha(
    ) and wannasee.text[0] not in ("/", "#", "@", "!"):
        await wannasee.edit("[Click Here To Get The Link Of My Userbot Repo](https://github.com/PainKiller3/Telegram-UserBot/)")


@register(outgoing=True, pattern="^.evox$")
async def evox_poco(wannasee):
    """ For .evox command, just returns the evox poco download link. """
    if not wannasee.text[0].isalpha(
    ) and wannasee.text[0] not in ("/", "#", "@", "!"):
        await wannasee.edit(
		"📲 EvolutionX for POCO F1 (beryllium).\n"
		"👤 by [Ninad Patil (REIGNZ)](@REIGNZ3)\n"
		"ℹ️ Version: Pie\n"
		"⬇️ [Download now](https://sourceforge.net/projects/evolution-x/files/beryllium/)\n"
		"📱 [XDA Thread](https://forum.xda-developers.com/poco-f1/development/rom-evolution-x-t3923023/amp/)\n"
		"#beryllium #KeepEvolving"
		)


CMD_HELP.update({
    'random': '.random <item1> <item2> ... <itemN>\
\nUsage: Get a random item from the list of items.'
})

CMD_HELP.update({
    'sleep': '.sleep 10\
\nUsage: Userbots get tired too. Let yours snooze for a few seconds.'
})

CMD_HELP.update({
    "shutdown": ".shutdown\
\nUsage: Sometimes you need to restart your bot. Sometimes you just hope to\
hear Windows XP shutdown sound... but you don't."
})

CMD_HELP.update({
    'support': ".support\
\nUsage: If you need help, use this command."
})

CMD_HELP.update({
    'repo': '.repo\
\nUsage: If you are curious what makes Paperplane work, this is what you need.'
})

CMD_HELP.update({
    'evox': '.evox\
\nUsage: Send the link of EvolutionX Rom For Poco F1 xD.'
})

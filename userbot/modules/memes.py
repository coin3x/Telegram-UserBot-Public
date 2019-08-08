# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
#

""" Userbot module for having some fun. """

import asyncio
import random
import re
import time

from userbot import bot
from cowpy import cow
from collections import deque
from telethon import events, functions, types

from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

# ================= CONSTANT =================
METOOSTR = [
    "Me too thanks",
    "Haha yes, me too",
    "Same lol",
    "Me irl",
    "Same here",
    "Haha yes",
    "Me rn",
]
EMOJIS = [
    "😂",
    "😂",
    "👌",
    "✌",
    "💞",
    "👍",
    "👌",
    "💯",
    "🎶",
    "👀",
    "😂",
    "👓",
    "👏",
    "👐",
    "🍕",
    "💥",
    "🍴",
    "💦",
    "💦",
    "🍑",
    "🍆",
    "😩",
    "😏",
    "👉👌",
    "👀",
    "👅",
    "😩",
    "🚰",
]
UWUS = [
    "(・`ω´・)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)∠☆",
    "(ô_ô)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(♥_♥)",
    "*(^O^)*",
    "((+_+))",
]
FACEREACTS = [
    "ʘ‿ʘ",
    "ヾ(-_- )ゞ",
    "(っ˘ڡ˘ς)",
    "(´ж｀ς)",
    "( ಠ ʖ̯ ಠ)",
    "(° ͜ʖ͡°)╭∩╮",
    "(ᵟຶ︵ ᵟຶ)",
    "(งツ)ว",
    "ʚ(•｀",
    "(っ▀¯▀)つ",
    "(◠﹏◠)",
    "( ͡ಠ ʖ̯ ͡ಠ)",
    "( ఠ ͟ʖ ఠ)",
    "(∩｀-´)⊃━☆ﾟ.*･｡ﾟ",
    "(⊃｡•́‿•̀｡)⊃",
    "(._.)",
    "{•̃_•̃}",
    "(ᵔᴥᵔ)",
    "♨_♨",
    "⥀.⥀",
    "ح˚௰˚づ ",
    "(҂◡_◡)",
    "ƪ(ړײ)‎ƪ​​",
    "(っ•́｡•́)♪♬",
    "◖ᵔᴥᵔ◗ ♪ ♫ ",
    "(☞ﾟヮﾟ)☞",
    "[¬º-°]¬",
    "(Ծ‸ Ծ)",
    "(•̀ᴗ•́)و ̑̑",
    "ヾ(´〇`)ﾉ♪♪♪",
    "(ง'̀-'́)ง",
    "ლ(•́•́ლ)",
    "ʕ •́؈•̀ ₎",
    "♪♪ ヽ(ˇ∀ˇ )ゞ",
    "щ（ﾟДﾟщ）",
    "( ˇ෴ˇ )",
    "눈_눈",
    "(๑•́ ₃ •̀๑) ",
    "( ˘ ³˘)♥ ",
    "ԅ(≖‿≖ԅ)",
    "♥‿♥",
    "◔_◔",
    "⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾",
    "乁( ◔ ౪◔)「      ┑(￣Д ￣)┍",
    "( ఠൠఠ )ﾉ",
    "٩(๏_๏)۶",
    "┌(ㆆ㉨ㆆ)ʃ",
    "ఠ_ఠ",
    "(づ｡◕‿‿◕｡)づ",
    "(ノಠ ∩ಠ)ノ彡( \\o°o)\\",
    "“ヽ(´▽｀)ノ”",
    "༼ ༎ຶ ෴ ༎ຶ༽",
    "｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡",
    "(づ￣ ³￣)づ",
    "(⊙.☉)7",
    "ᕕ( ᐛ )ᕗ",
    "t(-_-t)",
    "(ಥ⌣ಥ)",
    "ヽ༼ ಠ益ಠ ༽ﾉ",
    "༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽",
    "ミ●﹏☉ミ",
    "(⊙_◎)",
    "¿ⓧ_ⓧﮌ",
    "ಠ_ಠ",
    "(´･_･`)",
    "ᕦ(ò_óˇ)ᕤ",
    "⊙﹏⊙",
    "(╯°□°）╯︵ ┻━┻",
    r"¯\_(⊙︿⊙)_/¯",
    "٩◔̯◔۶",
    "°‿‿°",
    "ᕙ(⇀‸↼‶)ᕗ",
    "⊂(◉‿◉)つ",
    "V•ᴥ•V",
    "q(❂‿❂)p",
    "ಥ_ಥ",
    "ฅ^•ﻌ•^ฅ",
    "ಥ﹏ಥ",
    "（ ^_^）o自自o（^_^ ）",
    "ಠ‿ಠ",
    "ヽ(´▽`)/",
    "ᵒᴥᵒ#",
    "( ͡° ͜ʖ ͡°)",
    "┬─┬﻿ ノ( ゜-゜ノ)",
    "ヽ(´ー｀)ノ",
    "☜(⌒▽⌒)☞",
    "ε=ε=ε=┌(;*´Д`)ﾉ",
    "(╬ ಠ益ಠ)",
    "┬─┬⃰͡ (ᵔᵕᵔ͜ )",
    "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
    r"¯\_(ツ)_/¯",
    "ʕᵔᴥᵔʔ",
    "(`･ω･´)",
    "ʕ•ᴥ•ʔ",
    "ლ(｀ー´ლ)",
    "ʕʘ̅͜ʘ̅ʔ",
    "（　ﾟДﾟ）",
    r"¯\(°_o)/¯",
    "(｡◕‿◕｡)",
]
INSULT_STRINGS = [
    "Owww ... Such a stupid idiot.",
    "Don't drink and type.",
    "Command not found. Just like your brain.",
    "Bot rule 544 section 9 prevents me from replying to stupid humans like you.",
    "Sorry, we do not sell brains.",
    "Believe me you are not normal.",
    "I bet your brain feels as good as new, seeing that you never use it.",
    "If I wanted to kill myself I'd climb your ego and jump to your IQ.",
    "You didn't evolve from apes, they evolved from you.",
    "What language are you speaking? Cause it sounds like bullshit.",
    "You are proof that evolution CAN go in reverse.",
    "I would ask you how old you are but I know you can't count that high.",
    "As an outsider, what do you think of the human race?",
    "Ordinarily people live and learn. You just live.",
    "Keep talking, someday you'll say something intelligent!.......(I doubt it though)",
    "Everyone has the right to be stupid but you are abusing the privilege.",
    "I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.",
    "You should try tasting cyanide.",
    "You should try sleeping forever.",
    "Pick up a gun and shoot yourself.",
    "Try bathing with Hydrochloric Acid instead of water.",
    "Go Green! Stop inhaling Oxygen.",
    "God was searching for you. You should leave to meet him.",
    "You should Volunteer for target in an firing range.",
    "Try playing catch and throw with RDX its fun.",
    "People like you are the reason we have middle fingers.",
    "When your mom dropped you off at the school, she got a ticket for littering.",
    "You’re so ugly that when you cry, the tears roll down the back of your head, just to avoid your face.",
    "If you’re talking behind my back then you’re in a perfect position to kiss my a**!.",
]
CHINESESPAM_STRINGS = [
    "高雄好七桃 👍 三天兩暝尚叼好 坐高鐵只愛點半鐘 🚄 🙉沿途看風景 🙉 高雄人有本領 👏🏻 豪爽好客真熱情 ❤️ 世界一流高雄港 美麗夕陽西仔灣 月世界地質奇觀 擱有蓮池潭 來這打卡按個讚 👋🏼 晨鐘暮鼓佛光山 莊嚴佛陀紀念館 寶來溫泉一級棒 懷舊打狗領事館 一心二聖三多四維五福六合七賢八德九如十全 高雄路名有意義擱真好記 🤙🏻 So Fantastic 🤙🏻 So Fun 🤙🏻 愛河散步談戀愛 夜景繽紛又多彩 🌈 國際城巿人人愛 ❤️ 大家對這有期待 義大世界還有夢時代 🏬 吃喝玩樂逛不完 來去岡山吃羊肉 🥩 旗山出名是香蕉 🍌 鳳山排隊花生糖 🥜 緊來緊來好呷擱好耍 👅 鐵道文化哈瑪星 內門傳統宋江陣 高雄發展好站起 💪 經濟起飛大賺錢 💰",
    "在嗎==\n我勸你不要太過分哦\n威脅就算了 跟麻糬說那三小\n還有 這種事是你可以拿來亂講的？做人真的不要太過分\n之前對我也是，你到底是怎樣\n不想跟你撕破臉 但是你最近已經太超過了\n最後 不要逼我 只要我一個下令\n你的人脈都會消失 我也有你的把柄\n就這樣 我只是勸告",
    "邪氣小孩不用這麼吃嘴😏😏\n2486話術都一敗的👆👆\n當08塑膠就是了👌👌\n咖啡話一堆👏👏\n要這麼狂我也是笑笑😂😂\n阿三仔要灣都來😎😎\n不用在那邊七逃FB😑😑\n#少在那邊跟我旋轉🖕🖕\n#支援叫飽一點👈👈\n#我看你是沒遇過真流氓💪💪\n所以你走跳很大？哪裡的？拍謝 林北沒聽過。\n陣頭有惹到你是不是，你什麼級數想挑戰？\n陣頭文化歷史你懂多少？不懂你在說嘴什麼？\n總是都有你們這些2486在那邊嘴賤？年紀輕輕就想被砍？\n自以為是喔？不要以為口出狂言你會沒事！\n我們這邊八台廂型車準備處理你。 人沒很飽，你出門小心點黑～\n準備好過頭七了沒？我說到做到，咖小 幹、\n這種我看多了啦，沒有背景 出一張嘴，看哩娘？\n是當自己很猛？ 幹 要彎家你還不夠格\n你們這群吃嘴囝仔是安怎？\n幹拎娘哄幹喔？\n跨麥安抓攏總來啦\n人叫飽一點幹\n賣齁郎跨不起啦\n諺仔溫兄弟捏\n啊你給人家這樣Po是什麼心態啦蛤\n耖機掰不知死活屁小孩\n啊活網路很ㄏㄧㄠˊ膩？\n幹林娘我走跳社會十多年啦\n你這款的包包回家去\n少在那三砲兩砲幹機掰\n要橋攏嘎哇來\n河濱公園橋下那台紅色勁戰就是拎北啦",
    "你應該也要看到貝貝的發文吧？你直接來密我 我跟你說一切的事情 如果今天你真的把我當成是我 妹妹的話 那你就來密我 如果今天 是站佩佩那裡 我醜話先說 我跟你以後再也不是姐妹 我很直接沒錯",
    "幹我文章還沒看 惹我兄弟你就是對方\n最近聽到一點風聲\n有人在找我兄弟麻煩？\n原本想好好的躲通\n現在要讓我在背一條傷害也可以\n你們這些沒出社會走跳的小鬼\n最近最好躲好一點\n不然被我遇到一定讓你領保險\n不要以為我們是吃素的\n讓你們看看誰手骨比較粗\n身體防彈的都給我出來\n不用在那三砲五砲\n地址給一給馬上到\n出來再看誰比較硬別只會在網路上嗆兄嗆弟\n我他媽跟公司的 夠膽帶人來砸\n拎北這什麼都沒有 短支的不少長支的也有\n什麼年代還跟你用刀仔\n彈兩發讓你倒下三吋半\n我就是現實最狂的8+9啦😏😏\n嘴砲都是用RC來尬人的👆👆\n沒有醉狂只有更狂啦👏👏\n要來嘴都來😂😂\n少在那邊跟我彎棒球😂😂\n直接育達衝西瓜刀啦😜✌️\n#三餐吃飽一點😎😎\n#支援都被我斷截了啦😏\n#我看你是沒被砍過😍😍",
    "老大愛你餒我們認識到交往你都不知道打幾篇長文給我了.😳大愛你雖然我們認識的原因很好笑但我們要穩ㄛˊ你當兵我會等你ㄏㄚˋ👄放心吶我不是那種會自己離開的除非你惹我這個大公主生氣要不然我不會隨便離開你的我要一直被你寵然後對你生氣對你發脾氣對你任性都只對你.😛😛😛我們第一次牽手在望高寮休息的時後\nㄇㄨㄚˋ也是在那個時候.😳\n愛上你也不是因為你好看還是怎樣.那是因為你有辦法接受我的脾氣然後把我寵的真的像公主.👸\n這輩子也只想跟你到最後了.💕\n我先說ㄏㄚˋ我是一個很愛吃醋的公主ㄛˊ所以你真的不能跟女生走太近要不然你家這隻公主被爆氣的.😒還有你跟我在一起你就跑不掉了我會死死的把你綁在身邊不讓你跑掉的.😏\n還有你要跟我在一起你要答應我幾件事ㄏㄚˋ😎\n1.我跟你出門都要牽著我.👫【除非我叫你先不要牽🙈】\n2.還有對我不能隱瞞任何事情.👌【被我抓到你隱瞞我任何事情就死定】\n3.不能跟女生曖昧.👿【我會剁了你的🐥🐥】\n4.心裡只能有我這個大北鼻公主.👸【態度變我就會覺得你有別人了🖕】\n5.你要搬到哪還是去住誰那都要讓我知道.🏠【絕對絕對絕對不能是女生😡】\n6.你要去哪裡要幾點回家都要跟我說#記得要交代的一清二楚【敢騙我被抓到你就gg了👹】\n7.你的肩膀只能給我靠.😽【要給我一個人靠一輩子.😍】\n8.你的機車還有副駕駛只能載我一個女生【我有先說了ㄏㄚˋ先生.😒被我抓到載哪個女生他會怎樣知道ㄅ🙄（除了你媽媽你姐姐你妹妹你阿嬤其他的不能😂）】9.不能看其他的妹子.💢【我會打你】\n10.答應我要乖一點不要讓我擔心.😢【我會亂想】\n11.要去支援可以我不反對【但絕對不能受傷 受傷我一定找打你的人👿】\n12.早上中午晚上都要跟我問好.😛【除非你在睡覺休息可以不用其他都要】\n13.給我足夠的安全感😔【我很會亂想】\n14.不要讓我找不到你.😤【要不然我就搞失蹤】\n15.我不喜歡的事不能逼我.😅【要不然我會不理你】\n16.我跟你鬧脾氣吵架說要分手其實都不是真的要分手💔【我其實只想你多哄哄我】\n17.還有絕對不能兇我.🙂【要不然我哭給你看】\n18.出去不能無視我.👀【要一直帶在你身邊】\n19.在臉書要跟女生保持距離.🕳【要不然他會動心我會玻璃心】\n20.有女生在難過分手了找你安慰可以我不會說甚麼😘【但可以幹嘛不能幹嘛你應該知道】\n21.不能再我面前說到其他女生.🔊【要不然我就在你面前說其他男生】\n22.不能聽到別人說我怎樣就離開我🔕【要不然你可以直接跟我分手了】\n23.要把我介紹給你的朋友認識.🌏【這樣大家都知道我是你女友】\n24.你自己說要把我寵的像公主的ㄛˊ😳【到最後可別說我太公主病了】\n25.最後我要跟你說的是我會這輩子都黏著你不分開了.😘\n\n真的很愛你啦老大謝謝你把我哄的像公主跟你在一起真的什麼都不用擔心了真的好愛你ㄚㄚ還有老大我想你了.😭不知道為什麼今天一直想你可能真的很愛你了.🙈愛你老大我們要一直這樣穩穩的下去都不要分開ㄛˊㄇㄨㄚˋ我最愛的老大ㄐㄇ👄\n跟你在一起的這57天有分分合合但後來我們還是在一起了.😳這57天我們只要有時間都膩在一起都快變黏體嬰了還有ㄚ我可能真的要變公主了😶真的好愛你謝謝你為了我陪我到處玩到處跑真的好愛你老大.❤這輩子就你了.😳這57天真的跟你創造了許多回憶.有時候真的會捨不得你回家(cr有時候會怕你回去後就不會再來找我了老大對不起我很愛亂想寶貝我願意為了你改變自己的脾氣我也願意當你一輩子的公主我知道你很愛我.所以那天才會哭對不起老大這28天跟你鬧的許許多多的脾氣.(老實說我是一個很沒安全感的臭小孩所以前陣子跟最近你要親我我都會躲.(但現在你就是我的安全感了所以我不會再躲你了老大\n❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤\n老大我答應你我會好好的照顧自己不會讓你擔心也不會再傷害自己了老大穩穩的57天❤\n\n不留一點祝福的話嗎？😳😳\n有男朋友 朋友就都不見了嗎？😢\n\n#勿抄襲也不能複製我打的.👌",
    "我突然想到\n幹你娘不對啊\n這完全不是我的錯😒\n你自己去找女人 還不只一個\n遊戲也選單身還找女人\n每次都對我冷漠\n好啦 你很忙我可以體諒你\n但你再忙他媽還可以直播？\n阿不就很忙？？？\n你文章寫得好像是我的錯\n我還是會想你？\n你他媽再找其他女人的時候\n怎麼沒想到我💩",
    "笑死😂😂😂👍👍這你自己想出來的嗎😳😳很厲害欸😎😎 哈哈是我啦你是不是很懂嘻哈啊skrskr🤙🤙🤙😎😎😎👊👊👊🖕🖕🖕🖖🖖🖖 peace 笑死😂😂😂👍👍這你自己想出來的嗎😳😳很厲害欸😎😎露背😏😏比原住民加分還客家餒🤭🤭",
    "嗯哼一年就這樣過去了\n\n在今年大笑生氣也哭過\n\n留下的謝謝你們依舊在\n\n相信我們2014會更好^^\n\nOK再來要開始努力會考ˊˋ\n\n加油 <3",
    "老娘我天生脾氣不好😊\n只要動到我的人\n就算與全世界為敵 我也會除掉你😏\n我12y辣 小六齁\n再問年紀直接封鎖嘿🙄\n進來看了就加個好友吧💜\n2/23❤心有所屬❤\n我很愛他🤤\n討厭喝綠茶帶手婊☺",
    "很好....你很腦殘嗎....敢這樣講刀劍神域.......我死也不會放過你。我給你兩個選擇。 1:我把你送去給鬼灯 2:你給我做好心理準備...因為死亡已經降臨在你身邊了。 你逼我的，聖使之裝:裝備:聖冥靈武:真-聖星夜嵐靈刀、真-星夜慄凜靈刀 你給我受死吧:雙刀絕技:奧義，滅靈，賦予亡者戰魂力量，星夜冥靈閃-一式、奧義，聖靈，賦予王者戰魂力量，星夜聖靈閃-二式 要是敢在這裡再說一次反刀劍神域，你就別怪我不客氣了",
    'Very good….You very weak brain… dare say that to SAO… i won’t let you go til i die. i give you 2 choice.\n1. i send you to 鬼灯。\n2. you give me prepare your mind prepare…cuz death have came to your side.\nyou force me, Saint-Equip:Equipment:Saint-Hell Soul-Weapon:"Real Saint Star Night Arashi Soul-Sword", "Real Star Night Scared Soul-Sword"\nYou give me to die: double blades skill:Skill, Destroy-Soul, give the power of Battle-Soul to Deather, "Star Night Hell Soul Flash" Mode One, Skill, Saint Soul, give the power of Battle-Soul to king, "Star Night Saint Soul Flash" Mode Two\nIf you dare to say you anti-SAO again here, you just don’t blame my welcome.\nAt that time, you can’t save your head and your small life any more.',
    "你好 你說我電腦爛是嗎？ 我的顯卡1080 高效能主機 w10處理器 配備羅技G403 G340 煉獄奎蛇 雷蛇耳機 主機總價6萬8 你說電腦爛 你要不要讓我看看你的主機？",
    "人放錯，天在看\n我就不相信\n你有那麼大的本事來對付我\n動到我\n我會那你死得像鬼一樣\n感動到我的人\n我就讓你死無葬身之地\n最好別動到我\n我先跟你們說",
    "給庫痾痾痾痾痾痾 給庫痾痾痾痾痾痾 阿給 給庫 給庫 給ㄎ 阿哈 為什麼 為什麼不幫我 發大絕 極靈 嚕R 墮 嚕R 搭波kill 巨槌瑞斯 誇爪 哈哈哈哈 阿哈哈哈 嗯RRRRRRRRRR 嚕RRRRRRRRRRRRRR 還敢下來阿冰鳥 嚕RRRRRRRRRRRRRR 老爸墮起來 搭波kill 哈哈哈哈 哈哈哈哈哈哈 嚕RRRRRRRRRRRRRR 嚕RRRRRRRRRRRRRR 嬰兒 嚕RRRRRRRRRRRRRR 搭波KILL 達瑞斯 &^^^%%##$#%@$#@# 阿$#$%#%$$^u&^%##@ 阿ㄅㄅㄅ不要不要不要不要 有囉 這一波有囉 哈撒ㄎㄧ 吹起來 聊天室滑起來 滑起來 DEATH IS LIKE THE WIND ALWAYS BY MY 賽 牙索開滑 呼呼赫赫赫赫 地板很滑的阿 嘿嘿嘿嘿嘿嘿嘿 哈哈哈又要死囉 飛起來 哈哈哈哈 哈哈哈哈 爽阿 滑哥 墮胎屬叔 AAAAAAAAAAAA 一打二 瑞斯 瑞斯一打三(破音) AAAAAAAAAAAAAA 幹他媽在BANG 我牙素阿 操 屬叔開墮囉 欸 你 喔齁齁 你到底在 哇OOOOOOOOOOOO 這什麼到底什麼閃現 侯喔齁齁齁 又死一次 AAAAAAAAAAAAA 籃框 A A A 三個 RRRRRRRRRRR 幹我差一點外圈就可以捲出去 我就贏了 喔喔齁齁齁 呦呼 劃劃劃劃 滑起來 通通給我滑起來 SHUT DOWN 滑 起 來 通通給我滑起來 滑起來 DEATH IS LIKE THE WIND 哈哈 又CARRY了一場 媽的 哈哈哈哈 哈撒ㄎㄧ 哈撒ㄎㄧ 哈哈哈哈 哈哈哈哈 又贏了 爽阿 聊天室滑起來 通通給我滑起來 GG 牙素 第二勝到手 哈哈咻咻咻咻咻咻咻 咻 給庫 哈哈哈 FIRST BLOOD 嗚度度度 抓到你囉 還敢他媽藍開嘿嘿嘿嘿 給庫FIRST BLOOD 哈哈 咻 得勒得得得得得得得勒得得勒得勒得 乞丐大劍 轟 哈咖呦 劃劃劃劃 滑起來 HEHE 幹拎娘 RRRRRRRRRRR R呼 呼呼呼 呼嗚 好爛喔 你好爛喔",
    "馬的吃個飯本來就是各付各的\n我點460的東西 ， 妳們2人點了2200\n要我跟妳們平分唷\n我我說出600 妳還嫌少\n說以後別做朋友\n馬的\n要平分一開始不講\n我就點了牛肉丼飯160 唐揚雞120 蛤蜊湯 60 清酒 120\n妳們點2200我根本沒要吃 妳自己硬夾一個給我襪操\n其他幾乎妳們在吃\n事後用合菜抹黑我\n如果是中式料理我沒話說\n如果你事先說要平分我沒話說\n現在我就是單點點了460\n妳們點了2200\n到底誰有事 ?\n日式料理本來就很多 單點個人的東西 合菜 ? 合妳妹的火龍果啦\n整盤吃到剩一塊硬夾給我事後抹黑是哪招 ?\n我單點的唐揚雞跟清酒也主動分妳們吃\n這是禮貌性的互相分享食物 我跟同事吃西堤也會分享不同主餐\n但不會硬坳一定要怎樣平分 襪操\n從來沒看過日式丼飯 3個人合吃的啦 !",
]
ABUSESREACTS = [
    "Ur mum gey",
    "Ur dad trans",
    "Relax your Rear,ders nothing to fear,The Rape train is finally here",
    "Stfu and Gtfo U nub",
]
RUNSREACTS = [
    "Runs to Thanos",
    "Runs far, far away from earth",
    "Running faster than usian bolt coz I'mma Bot",
    "Runs to Marie",
    "Cya bois",
    "Kys",
    "I go away",
    "I am just walking off, coz me is too fat.",
    "I Fugged off!",
]
DISABLE_RUN = False


# ===========================================


@register(outgoing=True, pattern=r"^.(\w+)say (.*)")
async def univsaye(cowmsg):
    """ For .cowsay module, userbot wrapper for cow which says things. """
    if not cowmsg.text[0].isalpha() and cowmsg.text[0] not in (
            "/", "#", "@", "!"):
        arg = cowmsg.pattern_match.group(1).lower()
        text = cowmsg.pattern_match.group(2)

        if arg == "cow":
            arg = "default"
        if arg not in cow.COWACTERS:
            return
        cheese = cow.get_cow(arg)
        cheese = cheese()

        await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")

# remove unused memes
"""
@register(outgoing=True, pattern="^:/$")
async def kek(keks):
    # Check yourself ;)
    uio = ["/", "\\"]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])


@register(outgoing=True, pattern="^-_-$")
async def lol(lel):
    # Ok...
    okay = "-_-"
    for _ in range(10):
        okay = okay[:-1] + "_-"
        await lel.edit(okay)


@register(outgoing=True, pattern="^.cp(?: |$)(.*)")
async def copypasta(cp_e):
    # Copypasta the famous meme
    if not cp_e.text[0].isalpha() and cp_e.text[0] not in ("/", "#", "@", "!"):
        textx = await cp_e.get_reply_message()
        message = cp_e.pattern_match.group(1)

        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await cp_e.edit("`😂🅱️IvE👐sOME👅text👅for✌️Me👌tO👐MAkE👀iT💞funNy!💦`")
            return

        reply_text = random.choice(EMOJIS)
        # choose a random character in the message to be substituted with 🅱️
        b_char = random.choice(message).lower()
        for owo in message:
            if owo == " ":
                reply_text += random.choice(EMOJIS)
            elif owo in EMOJIS:
                reply_text += owo
                reply_text += random.choice(EMOJIS)
            elif owo.lower() == b_char:
                reply_text += "🅱️"
            else:
                if bool(random.getrandbits(1)):
                    reply_text += owo.upper()
                else:
                    reply_text += owo.lower()
        reply_text += random.choice(EMOJIS)
        await cp_e.edit(reply_text)
"""

@register(outgoing=True, pattern="^.vapor(?: |$)(.*)")
async def vapor(vpr):
    """ Vaporize everything! """
    if not vpr.text[0].isalpha() and vpr.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await vpr.get_reply_message()
        message = vpr.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await vpr.edit("`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
            return

        for charac in message:
            if 0x21 <= ord(charac) <= 0x7F:
                reply_text.append(chr(ord(charac) + 0xFEE0))
            elif ord(charac) == 0x20:
                reply_text.append(chr(0x3000))
            else:
                reply_text.append(charac)

        await vpr.edit("".join(reply_text))


@register(outgoing=True, pattern="^.str(?: |$)(.*)")
async def stretch(stret):
    """ Stretch it."""
    if not stret.text[0].isalpha() and stret.text[0] not in (
            "/", "#", "@", "!"):
        textx = await stret.get_reply_message()
        message = stret.text
        message = stret.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await stret.edit("`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
            return

        count = random.randint(3, 10)
        reply_text = re.sub(
            r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])",
            (r"\1" * count),
            message
        )
        await stret.edit(reply_text)


@register(outgoing=True, pattern="^.zal(?: |$)(.*)")
async def zal(zgfy):
    """ Invoke the feeling of chaos. """
    if not zgfy.text[0].isalpha() and zgfy.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await zgfy.get_reply_message()
        message = zgfy.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await zgfy.edit(
                "`gͫ ̆ i̛ ̺ v͇̆ ȅͅ   a̢ͦ   s̴̪ c̸̢ ä̸ rͩͣ y͖͞   t̨͚ é̠ x̢͖  t͔͛`"
            )
            return

        for charac in message:
            if not charac.isalpha():
                reply_text.append(charac)
                continue

            for _ in range(0, 3):
                randint = random.randint(0, 2)

                if randint == 0:
                    charac = charac.strip() + \
                        random.choice(ZALG_LIST[0]).strip()
                elif randint == 1:
                    charac = charac.strip() + \
                        random.choice(ZALG_LIST[1]).strip()
                else:
                    charac = charac.strip() + \
                        random.choice(ZALG_LIST[2]).strip()

            reply_text.append(charac)

        await zgfy.edit("".join(reply_text))

# i don't wanna greet anyone
"""
@register(outgoing=True, pattern="^hi$")
async def hoi(hello):
    # Greet everyone!
    await hello.edit("Hoi!😄")
"""

@register(outgoing=True, pattern="^.owo(?: |$)(.*)")
async def faces(owo):
    """ UwU """
    if not owo.text[0].isalpha() and owo.text[0] not in ("/", "#", "@", "!"):
        textx = await owo.get_reply_message()
        message = owo.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await owo.edit("` UwU no text given! `")
            return

        reply_text = re.sub(r"(r|l)", "w", message)
        reply_text = re.sub(r"(R|L)", "W", reply_text)
        reply_text = re.sub(r"n([aeiou])", r"ny\1", reply_text)
        reply_text = re.sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
        reply_text = re.sub(r"\!+", " " + random.choice(UWUS), reply_text)
        reply_text = reply_text.replace("ove", "uv")
        reply_text += " " + random.choice(UWUS)
        await owo.edit(reply_text)


@register(outgoing=True, pattern="^.react$")
async def react_meme(react):
    """ Make your userbot react to everything. """
    if not react.text[0].isalpha() and react.text[0] not in (
            "/", "#", "@", "!"):
        index = random.randint(0, len(FACEREACTS))
        reply_text = FACEREACTS[index]
        await react.edit(reply_text)


@register(outgoing=True, pattern="^.shrug$")
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    if not shg.text[0].isalpha() and shg.text[0] not in ("/", "#", "@", "!"):
        await shg.edit(r"¯\_(ツ)_/¯")


@register(outgoing=True, pattern="^.insult$")
async def insult(e):
    """ I make you cry ! """
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(random.choice(INSULT_STRINGS))

@register(outgoing=True, pattern="^.chnspam$")
async def insult(e):
    """ Spam in ching chong """
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(random.choice(CHINESESPAM_STRINGS))

# sorry i don't speak curry
"""
@register(outgoing=True, pattern="^.abuse$")
async def abuse(e):
    #Galli Dunga Bdske !!
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(random.choice(ABUSESREACTS))
"""

@register(outgoing=True, pattern="^.runs$")
async def runner_lol(run):
    """ Run, run, RUNNN! """
    if not DISABLE_RUN:
        if not run.text[0].isalpha() and run.text[0] not in (
                "/", "#", "@", "!"):
            index = random.randint(0, len(RUNSREACTS) - 1)
            reply_text = RUNSREACTS[index]
            await run.edit(reply_text)


@register(outgoing=True, pattern="^.disable runs$")
async def disable_runs(norun):
    """ Some people don't like running... """
    if not norun.text[0].isalpha() and norun.text[0] not in (
            "/", "#", "@", "!"):
        global DISABLE_RUN
        DISABLE_RUN = True
        await norun.edit("```Done!```")


@register(outgoing=True, pattern="^.enable runs$")
async def enable_runs(run):
    """ But some do! """
    if not run.text[0].isalpha() and run.text[0] not in ("/", "#", "@", "!"):
        global DISABLE_RUN
        DISABLE_RUN = False
        await run.edit("```Done!```")


@register(outgoing=True, pattern="^.metoo$")
async def metoo(hahayes):
    """ Haha yes """
    if not hahayes.text[0].isalpha() and hahayes.text[0] not in (
            "/", "#", "@", "!"):
        reply_text = random.choice(METOOSTR)
        await hahayes.edit(reply_text)


@register(outgoing=True, pattern="^.mock(?: |$)(.*)")
async def spongemocktext(mock):
    """ Do it and find the real fun. """
    if not mock.text[0].isalpha() and mock.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await mock.get_reply_message()
        message = mock.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await mock.edit("`gIvE sOMEtHInG tO MoCk!`")
            return

        for charac in message:
            if charac.isalpha() and random.randint(0, 1):
                to_app = charac.upper() if charac.islower() else charac.lower()
                reply_text.append(to_app)
            else:
                reply_text.append(charac)

        await mock.edit("".join(reply_text))


@register(outgoing=True, pattern="^.clap(?: |$)(.*)")
async def claptext(memereview):
    """ Praise people! """
    if not memereview.text[0].isalpha(
    ) and memereview.text[0] not in ("/", "#", "@", "!"):
        textx = await memereview.get_reply_message()
        message = memereview.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await memereview.edit("`Hah, I don't clap pointlessly!`")
            return
        reply_text = "👏 "
        reply_text += message.replace(" ", " 👏 ")
        reply_text += " 👏"
        await memereview.edit(reply_text)


@register(outgoing=True, pattern="^.bt$")
async def bluetext(bt_e):
    """ Believe me, you will find this useful. """
    if not bt_e.text[0].isalpha() and bt_e.text[0] not in ("/", "#", "@", "!"):
        if await bt_e.get_reply_message():
            await bt_e.edit(
                "/BLUETEXT /MUST /CLICK.\n"
                "/ARE /YOU /A /STUPID /ANIMAL /WHICH /IS /ATTRACTED /TO /COLOURS ?"
            )


@register(outgoing=True, pattern="^.cry$")
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")


@register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")

# ugh
"""
@register(outgoing=True, pattern="^.clock$")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    if event.fwd_from:
		    return
	    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
	    for _ in range(32):
		    await asyncio.sleep(0.1)
		    await event.edit("".join(deq))
		    deq.rotate(1)


@register(outgoing=True, pattern="^.moon$")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    if event.fwd_from:
		    return
	    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	    for _ in range(32):
		    await asyncio.sleep(0.1)
		    await event.edit("".join(deq))
		    deq.rotate(1)
"""

@register(outgoing=True, pattern="^.myusernames$")
async def _(event):
    if event.fwd_from:
        return
    result = await bot(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)


@register(outgoing=True, pattern="^.poco$")
async def poco(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("[Join the Evolution X Group For Pocophone F1](https://t.me/EvoXPoco)")


@register(outgoing=True, pattern="^.channel$")
async def channel(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("[Join my channel for more design and complaints](https://t.me/ShenComplaints)")


@register(pattern='.type(?: |$)(.*)')
async def typewriter(typew):
    """ Just a small command to make your keyboard become a typewriter! """
    if not typew.text[0].isalpha() and typew.text[0] not in (
            "/", "#", "@", "!"):
        textx = await typew.get_reply_message()
        message = typew.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await typew.edit("`Give a text to type!`")
            return
        sleep_time = 0.03
        typing_symbol = "|"
        old_text = ''
        await typew.edit(typing_symbol)
        await asyncio.sleep(sleep_time)
        for character in message:
            old_text = old_text + "" + character
            typing_text = old_text + "" + typing_symbol
            await typew.edit(typing_text)
            await asyncio.sleep(sleep_time)
            await typew.edit(old_text)
            await asyncio.sleep(sleep_time)


CMD_HELP.update({
    "memes": "Ask 🅱️ottom🅱️ext🅱️ot (@NotAMemeBot) for that."
})

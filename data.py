# got the list from wikipedia
most_visited_websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "whatsapp": "https://www.whatsapp.com",
    "x": "https://www.x.com",
    "wikipedia": "https://www.wikipedia.org",
    "chat gpt": "https://www.chatgpt.com",
    "amazon": "https://www.amazon.com",
    "baidu": "https://www.baidu.com",
    "yandex": "https://www.yandex.com",
    "yahoo": "https://www.yahoo.com",
    "netflix": "https://www.netflix.com",
    "tiktok": "https://www.tiktok.com",
    "reddit": "https://www.reddit.com",
    "linkedin": "https://www.linkedin.com",
    "live": "https://www.live.com",
    "zoom": "https://www.zoom.us",
    "microsoft": "https://www.microsoft.com",
    "bing": "https://www.bing.com",
    "naver": "https://www.naver.com",
    "vk": "https://www.vk.com",
    "qq": "https://www.qq.com",
    "sohu": "https://www.sohu.com",
    "taobao": "https://www.taobao.com",
    "mail.ru": "https://www.mail.ru",
    "sina": "https://www.sina.com.cn",
    "weibo": "https://www.weibo.com",
    "msn": "https://www.msn.com",
    "globo": "https://www.globo.com",
    "duckduckgo": "https://www.duckduckgo.com",
    "roblox": "https://www.roblox.com",
    "quora": "https://www.quora.com",
    "ebay": "https://www.ebay.com",
    "new york times": "https://www.nytimes.com",
    "cnn": "https://www.cnn.com",
    "bbc": "https://www.bbc.com",
    "espn": "https://www.espn.com",
    "weather.com": "https://www.weather.com",
    "stack overflow": "https://www.stackoverflow.com",
    "github": "https://www.github.com",
    "wordpress": "https://www.wordpress.com",
    "adobe": "https://www.adobe.com",
    "salesforce": "https://www.salesforce.com",
    "dropbox": "https://www.dropbox.com",
    "slack": "https://www.slack.com",
    "spotify": "https://www.spotify.com",
    "apple": "https://www.apple.com",
    "paypal": "https://www.paypal.com",
    "alibaba": "https://www.alibaba.com",
    "flipkart": "https://www.flipkart.com",
    "snapchat": "https://www.snapchat.com",
    "pinterest": "https://www.pinterest.com",
    "tumblr": "https://www.tumblr.com",
    "fandom": "https://www.fandom.com",
    "imdb": "https://www.imdb.com",
    "hulu": "https://www.hulu.com",
    "zillow": "https://www.zillow.com",
    "indeed": "https://www.indeed.com",
    "coursera": "https://www.coursera.org",
    "udemy": "https://www.udemy.com",
    "khan academy": "https://www.khanacademy.org",
    "medium": "https://www.medium.com",
    "the guardian": "https://www.theguardian.com",
    "forbes": "https://www.forbes.com",
    "bloomberg": "https://www.bloomberg.com",
    "reuters": "https://www.reuters.com",
    "the washington post": "https://www.washingtonpost.com",
    "the wall street journal": "https://www.wsj.com",
    "the times of india": "https://www.timesofindia.com",
    "ndtv": "https://www.ndtv.com",
    "hindustan times": "https://www.hindustantimes.com",
    "the hindu": "https://www.thehindu.com",
    "indian express": "https://www.indianexpress.com",
    "livemint": "https://www.livemint.com",
    "moneycontrol": "https://www.moneycontrol.com",
    "zee news": "https://www.zeenews.india.com",
    "rediff": "https://www.rediff.com",
    "business standard": "https://www.business-standard.com",
    "economic times": "https://economictimes.indiatimes.com",
    "firstpost": "https://www.firstpost.com",
    "dna india": "https://www.dnaindia.com",
    "oneindia": "https://www.oneindia.com",
    "news18": "https://www.news18.com",
    "the quint": "https://www.thequint.com",
    "scroll.in": "https://scroll.in",
    "the print": "https://theprint.in",
    "scoopwhoop": "https://www.scoopwhoop.com",
    "yourstory": "https://yourstory.com",
    "inc42": "https://inc42.com",
    "techcrunch": "https://techcrunch.com",
    "mashable": "https://mashable.com",
    "gizmodo": "https://gizmodo.com",
    "engadget": "https://www.engadget.com",
    "the verge": "https://www.theverge.com",
    "cnet": "https://www.cnet.com",
    "zdnet": "https://www.zdnet.com",
    "ars technica": "https://arstechnica.com",
    "wired": "https://www.wired.com",
    "vox": "https://www.vox.com",
    "vice": "https://www.vice.com",
    "buzzfeed": "https://www.buzzfeed.com",
    "huffpost": "https://www.huffpost.com",
    "the atlantic": "https://www.theatlantic.com",
    "new yorker": "https://www.newyorker.com",
    "time": "https://time.com",
    "national geographic": "https://www.nationalgeographic.com",
    "scientific american": "https://www.scientificamerican.com",
    "nature": "https://www.nature.com",
    "science": "https://www.sciencemag.org",
    "mit technology review": "https://www.technologyreview.com",
    "popular science": "https://www.popsci.com",
    "smithsonian magazine": "https://www.smithsonianmag.com"
}
   
# used powershell to get the list of the installed programs and then created a dictionary that maps lowercase list to its original version
installed_apps_and_programs_dict = {
    # Classic Win32 Applications (.exe)
    'anaconda navigator': 'anaconda-navigator.exe',
    'anaconda powershell prompt': 'powershell.exe',
    'anaconda prompt': 'cmd.exe',
    'armoury crate': 'ArmouryCrate.exe',
    'aura creator': 'AuraCreator.exe',
    'calculator': 'calc.exe',
    'character map': 'charmap.exe',
    'command prompt': 'cmd.exe',
    'component services': 'comexp.msc',
    'computer management': 'compmgmt.msc',
    'control panel': 'control.exe',
    'defragment and optimize drives': 'dfrgui.exe',
    'dev home': 'devhome.exe',
    'dev-c++': 'devcpp.exe',
    'disk cleanup': 'cleanmgr.exe',
    'event viewer': 'eventvwr.msc',
    'excel': 'excel.exe',
    'feedback hub': 'FeedbackHub.exe',
    'file explorer': 'explorer.exe',
    'free download manager': 'fdm.exe',
    'google chrome': 'chrome.exe',
    'idle (python 3.13 64-bit)': 'pythonw.exe',
    'intel® graphics command center': 'igfxCUIService.exe',
    'iscsi initiator': 'iscsicpl.exe',
    'jupyter notebook': 'jupyter-notebook.exe',
    'license': 'license.exe',
    'magnifier': 'Magnify.exe',
    'mcafee': 'mcafee.exe',
    'microsoft clipchamp': 'Clipchamp.exe',
    'microsoft edge': 'msedge.exe',
    'microsoft store': 'WinStore.App.exe',
    'microsoft teams': 'Teams.exe',
    'miktex console': 'miktex-console.exe',
    'nvidia control panel': 'nvcplui.exe',
    'odbc data sources (32-bit)': 'odbcad32.exe',
    'odbc data sources (64-bit)': 'odbcad64.exe',
    'onedrive': 'OneDrive.exe',
    'onenote': 'onenote.exe',
    'on-screen keyboard': 'osk.exe',
    'outlook (new)': 'outlook.exe',
    'paint': 'mspaint.exe',
    'performance monitor': 'perfmon.exe',
    'photos': 'Microsoft.Photos.exe',
    'power automate': 'PowerAutomate.exe',
    'powerpoint': 'powerpnt.exe',
    'python 3.13 (64-bit)': 'python.exe',
    'quick assist': 'QuickAssist.exe',
    'razer synapse': 'RazerSynapse.exe',
    'realtek audio console': 'RtkNGUI64.exe',
    'recovery drive': 'RecoveryDrive.exe',
    'registry editor': 'regedit.exe',
    'remote desktop connection': 'mstsc.exe',
    'resource monitor': 'resmon.exe',
    'services': 'services.msc',
    'settings': 'SystemSettings.exe',
    'snipping tool': 'SnippingTool.exe',
    'sound recorder': 'SoundRecorder.exe',
    'spotify': 'Spotify.exe',
    'spyder': 'spyder.exe',
    'steam': 'steam.exe',
    'steps recorder': 'psr.exe',
    'sticky notes': 'StikyNot.exe',
    'system configuration': 'msconfig.exe',
    'system information': 'msinfo32.exe',
    'task manager': 'Taskmgr.exe',
    'task scheduler': 'taskschd.msc',
    'terminal': 'wt.exe',
    'texworks': 'texworks.exe',
    'thunderbolt™ control center': 'tbctrl.exe',
    'tor browser': 'firefox.exe',
    'visual studio code': 'code.exe',
    'word': 'winword.exe',
    'windows backup': 'sdclt.exe',
    'windows defender firewall with advanced security': 'wf.msc',
    'windows memory diagnostic': 'mdsched.exe',
    'windows powershell': 'powershell.exe',
    'windows powershell ise': 'powershell_ise.exe',
    'windows security': 'windowsdefender.exe',
    'windows tools': 'control.exe',
    'xbox': 'XboxApp.exe',
    'youtube music': 'YouTubeMusic.exe',

    # UWP Apps (Must use shell: or URI scheme)
    'calendar': 'start outlookcal:',
    'camera': 'start microsoft.windows.camera:',
    'clock': 'start ms-clock:',
    'copilot': 'start ms-copilot:',
    'dolby access': 'start dolbyaccess:',
    'family': 'start ms-family:',
    'films & tv': 'start mswindowsvideo:',
    'game bar': 'start xbox-gamebar:',
    'get help': 'start ms-contact-support:',
    'get started': 'start ms-get-started:',
    'glidex': 'start GlideX:',
    'live captions': 'start ms-settings:cortana-languagesettings',
    'mail': 'start outlookmail:',
    'maps': 'start bingmaps:',
    'media player': 'start mswindowsmusic:',
    'microsoft 365 copilot': 'start copilot:',
    'microsoft teams (personal)': 'start ms-teams:',
    'microsoft to do': 'start ms-to-do:',
    'myasus': 'start MyASUS:',
    'narrator': 'start ms-settings:easeofaccess-narrator',
    'netflix': 'start netflix:',
    'news': 'start bingnews:',
    'notepad': 'start notepad:',
    'quick assist': 'start ms-quick-assist:',
    'solitaire & casual games': 'start xboxsolitaire:',
    'sticky notes (new)': 'start ms-sticky-notes:',
    'virtual assistant': 'start cortana:',
    'voice access': 'start ms-settings:easeofaccess-speechrecognition',
    'weather': 'start bingweather:',
    'whatsapp': 'start whatsapp:',
    'windows media player legacy': 'start wmplayer:',
    'windows tools': 'start shell:appsfolder\\WindowsTools',
}


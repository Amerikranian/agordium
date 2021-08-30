import os
import os.path
import urllib.parse

IGNORE_FILES = ['file_list.txt', 'main.py', 'readme.md']

def generate_index():
    str = """
<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<meta http-equiv='X-UA-Compatible' content='IE=edge'>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>Audio Game Recording Repository</title>
</head>
<body>
<h1>Welcome</h1>
<p>Welcome to the Audio Games Recordings Repository.</p>
<p>The aim of the website is to list audio recordings of people playing Audio Games.  The hope is that this will preserve a history of content whether for nostalgic purposes, provide walkthroughs, or to provide an avenue for discovering new and old games.</p>
<h2>Important Please Read</h2>
<p>A small website such as this does not have any rules.</p>
<p>The only rule is to please refrain from mass downloading all of the files available here. Using automated tools such as scripts, Curl, Wget, etc for the automating of downloads is strongly discouraged.</p>
<p>In other words, if you use the website as normal, downloading few files and listening to them at a time is perfectly fine and is why this site exists.</p>
<p>In the event this request is not honored, the files will be blocked from being downloaded for the remainder of a month the violation takes place. Example,  on June 10 we notice people mass downloaded files, the files will not download for the remainder of June. They will be back in July.</p>
<h2>A Note to Content Creators</h2>
<p>An archive of recordings from a number of content creators has been provided here. We do not intend to steal content from creators. If you, a creator, has a problem with us hosting and listing content here, please feel free to contact us.</p>
<h2>Contacting Us</h2>
<p>You can now contact us using this <a href="https://forms.gle/ye5pxqwdakAYNr5g8">contact form.</a> Send us suggestions, recordings, or feedback about this project.</p>
<p>You can also contact us through <a href="https://forum.audiogames.net/topic/40657/game-recordings-repository-anyone-consider-doing-it/">this post</a> on the Audio Games forum. Just post a reply if you have an account and we'll see it.</p>
<p>If you want to increase this collection, we're happy to talk to you about missing content, or if you want to record your own content.</p>
<h2>Please Support These Creators</h2>
<p>We appreciate you checking out this website. However, before anything, we feel it important to point you to where many of these creators originally host their content so that you may support them.</p>
<p>If you are a creator and you wish your content-hosting platform is listed, please contact us.</p>
<p>This listing only includes content sources that currently exist and are live.</p>
<ul>
<li><a href="https://www.youtube.com/c/44KLetsPlays">44K LetsPlays YouTube</a></li>
<li>Aprone <a href="https://www.kaldobsky.com/ssl/audiogames.php">Website</a> <a href="https://www.youtube.com/user/TheAprone">YouTube</a></li>
<li><a href="https://www.youtube.com/channel/UCNbcgG4B9D4DTtIOXrnjUqQ">Audiogame edits YouTube</a></li>
<li><a href="https://www.youtube.com/channel/UCB1L76VgaXxCfwZX3VqiqeQ">Audiogame Extraordinaire YouTube</a></li>
<li>Brandon Cole <a href="https://www.youtube.com/channel/UCbJy3rXhAbRwG85D3yceS5A">YouTube</a> <a href="https://www.twitch.tv/superblindman/">Twitch</a></li>
<li><a href="https://blackscreengaming.com/">Black Screen Gaming (BSG)</a></li>
<li><a href="https://www.youtube.com/channel/UCDWOwfwJ18lQiXRubVBEFkw">Chris Wright YouTube</a></li>
<li><a href="https://www.youtube.com/channel/UCeNPXAts2OyU64yPUiL-faw">Evangelosz Nagy YouTube</a></li>
<li><a href="https://www.youtube.com/channel/UC0fNzoN5T_VwX08CI-xJUzg">Evil Chocolate Cookie YouTube</a></li>
<li><a href="https://www.youtube.com/channel/UCrI_FoGiniXlCa817LhB7OA">Gilbert Neiva YouTube</a></li>
<li><a href="https://www.youtube.com/channel/UCx-2KuqTyJylJAl8lwwJgww">Kavya YouTube</a></li>
<li>Liam Erven <a href="https://www.youtube.com/user/liamerven">YouTube</a> <a href="https://www.twitch.tv/liamerven">Twitch</a></li>
<li>Orinks <a href="https://www.youtube.com/user/Orinks">YouTube</a> <a href="https://www.twitch.tv/orinks1">Twitch</a></li>
<li>PG13LP <a href="https://pg13lp.com/">Website</a> <a href="https://www.youtube.com/channel/UCwsmTHviOiomYiRW0WPyqfA">Youtube</a></li>
<li><a href="http://samtupy.com/">Sam Tupy Website</a></li>
<li><a href="https://www.youtube.com/channel/UCqr0Igol9df3CC_QsPyuv_g">Sarah Alawami YouTube</a></li>
<li><a href="https://stevend.net/">Steven D Website</a></li>
<li><a href="https://www.youtube.com/channel/UCCIMEu3mUuoNrvCIqm0wv3A/">The Audio Game Club- For Blind Gamers Everywhere YouTube</a></li>
</ul>
<h2>Creator Listing</h2>
<ul>
    """
    with os.scandir() as files:
        for entry in files:
            if entry.name[-4:] == "html":
                str += f"<li><a href=\"{entry.name}\">{entry.name[:-5]}</a></li>"
    temp = open("index.html", "w")
    temp.write(str)
    temp.write("</body>\n</html>")
    temp.close()

def generate_clean_list(file_name):
    file_listing = open(f"{file_name}", "r")
    clean_list = open("clean_list.txt", "w")
    
    for line in file_listing:
        clean_list.write(line[31:])
    
    # Close files
    clean_list.close()
    file_listing.close()

def pre_populate(file_name):
    if not os.path.exists(file_name):
        temp_file = open(f"{file_name}", "w")
        str = """<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<meta http-equiv='X-UA-Compatible' content='IE=edge'>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>%s | Audio Game Recording Repository</title>
</head>
<body>
<h1>%s</h1>
        """ % (file_name[:len(file_name)-4], file_name[:len(file_name)-4])
        temp_file.write(str)
        temp_file.close()

def post_populate():
    with os.scandir("./") as files:
        for entry in files:
            if entry.name[-5:] == ".html":
                temp = open(entry.name, "a")
                temp.write("</body></html>")
                temp.close()

def generate_files():
    """ This function generates files for each author and series in the listing. """
    file = open("clean_list.txt", "r")
    extensions = [".mp3", ".ogg", ".wav", ".flac", ".wma", ".ogg"]
    for line in file:
        strings = line.split("/")
        if len(strings) == 3 and line[line.rfind("."):-1].lower() in extensions:
            author = strings[0]
            series = strings[1]
            if author != series:
                series_file = open(f"{author}__{series}.txt", "a")
                series_file.write(line)
                series_file.close()
            else:
                series_file = open(f"{author}.txt", "a")
                series_file.write(line)
                series_file.close()
        elif len(strings) == 2 and line[line.rfind("."):-1].lower() in extensions:
            author = strings[0]
            author_file = open(f"{author}", "a")
            author_file.write(line)
            author_file.close()
        elif len(strings) == 4:
            author = strings[0]
            series = strings[2]
            series_file = open(f"{author}__{series}.txt", "a")
            series_file.write(line)
            series_file.close()
    # Close file
    file.close()

def generate_html():
    """ This will generate HTML files from the helper text files. """
    with os.scandir("./") as files:
        for entry in files:
            if entry.name not in IGNORE_FILES and entry.name[-5:] != ".html" and entry.name != "clean_list.txt":
                strings = entry.name.split('__')
                if len(strings) == 2 and strings[0] != strings[1]:
                    author = strings[0]
                    series = strings[1]
                    pre_populate(f"{author}.html")
                    author_file = open(f"{author}.html", "a")
                    list_file = open(f"{entry.name}", "r")
                    author_file.write(f"<h2>{series[:len(series)-4]}</h2>\n")
                    author_file.write("<ul>\n")
                    for line in list_file:
                        BASE = "https://audio-game-recordings.s3.us-east-2.amazonaws.com"
                        line = line[:len(line)-1]
                        url = f"{line}"
                        line = line[:len(line)-4]
                        line = line.split('/')[-1]
                        url = urllib.parse.quote(url)
                        author_file.write(f"<li><a href=\"{BASE}/{url}\">{line}</a></li>\n")
                    author_file.write("</ul>\n")
                    author_file.close()
                    list_file.close()
                else:
                    author = strings[0]
                    if author[-4:] == ".txt": author = author[:-4]
                    pre_populate(f"{author}.html")
                    author_file = open(f"{author}.html", "a")
                    list_file = open(f"{entry.name}", "r")
                    author_file.write(f"<h2>Other</h2>\n")
                    author_file.write("<ul>\n")
                    for line in list_file:
                        BASE = "https://audio-game-recordings.s3.us-east-2.amazonaws.com"
                        line = line[:len(line)-1]
                        url = f"{line}"
                        line = line[:len(line)-4]
                        line = line.split('/')[-1]
                        url = urllib.parse.quote(url)
                        author_file.write(f"<li><a href=\"{BASE}/{url}\">{line}</a></li>\n")
                    author_file.write("</ul>\n")
                    author_file.close()
                    list_file.close()

def clean_up():
    """ Delete all files not needed """
    with os.scandir('./') as files:
        for entry in files:
            if (
              entry.name not in IGNORE_FILES and
              entry.name[-5:] != ".html"
            ):
                os.remove(entry.name)

def move_files():
    if not os.path.isdir("./output"):
        os.mkdir("output")
    with os.scandir("./") as files:
        for entry in files:
            if entry.is_file() and entry.name[-4:] == "html":
                os.rename(f"./{entry.name}", f"./output/{entry.name}")

print("Generating clean list of files.")
generate_clean_list(IGNORE_FILES[0])
print("Generating some helper text files.")
generate_files()
print("Generating HTML files.")
generate_html()
post_populate()
print("Cleaning up helper files")
clean_up()
print("Success! HTML files were generated.")
print("Generating index.html file.")
generate_index()
move_files()
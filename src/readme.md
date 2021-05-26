## How It Works
The script in this folder obviously requires Python. It is designed to simplify generating files for the audio game recordings archive.

It uses helper text files to keep track of lists, and generates HTML files according to the text files. Clean up should run smoothly.

Before generating files, just to be safe, make sure there is no output directory in this folder.

I recommend running this on command line to see if there are any errors.
## Where Does It Get Its Input From?
This is a semi-automatic solution and may be the official way of generating files. The input for this program was obtained from using the AWS CLI. Help can be found [at this link.](https://aws.amazon.com/cli/)

I got the CLI to generate a text file containing a snapshot listing of  all the files in audio-game-recordings bucket at time of running. In this directory, the file generated is called file_list.txt .

The steps needed to get it to work are:
1. Download AWS CLI from the link above
2. Run
```
$ aws configure
```
3. Enter information as requested. Credentials should have been provided.
4. Finally, to get it to generate a text file of file listing, I ran:
```
$ aws s3 ls --recursive audio-game-recordings > file_list.txt
```

And assuming the main.py file and the file_list.txt file are in the same directory (recommend folder with just these two files), things should work because the rest is just Python basics.

Feel free to improve!

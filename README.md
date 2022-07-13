This program allows you to find identical files in your directory. 
###To run program execute "main.py" and give working directory
python main.py [OPTIONS] [PATH]
###Options
  -h, --help            show this help message and exit\
  -i, --hidden          include hidden files\
  -o, --output          show table on exit\
  -d, --delimiter       update delimiter for default output\
  -s, --silent          no output for human




###To run docker container, first you need to build an image
docker build -t [BUILD-NAME] .

###To run docker container you need to run this command, inner directory must be named "mounted"
docker run -it --rm --name [CONTAINER-NAME] -e options="[OPTIONS]" -v [PATH]:/mounted [BUILD-NAME] 

if you need to run container with some options, please update dockerfile yourself
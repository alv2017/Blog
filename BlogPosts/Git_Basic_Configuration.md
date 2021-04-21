
Git is a version control system used by nearly every software developer.
In this blog post I will describe the basic setup that I'm using when
working with Git. I must admit that this is not my invention, and I shamelessly
picked it up from Peter Bell's amazing video course:
[Git and Github Live Lessons](https://www.oreilly.com/library/view/git-and-github/9780133992748/).
The course was published in 2014 by **Addison-Wesley Professional**, and in 2021
it still very relevant and super useful for everyone willing to use Git on a sensible basis.

### Git Configuration Levels

There are three levels of configuration in Git: local, global, and system.

In this post we will be focusing on *global* settings. You are applying Git global settings, 
when configuring *all* your projects and repositories for your personal user account. 

### Basic Settings
Let's open the terminal and let's type in the commands given below:

    $ git config --global user.name "Your Name" 

    $ git config --global user.email your@email.com

    $ git config --global color.ui true

In the first command we setting up our Git username. In the second command we are setting up 
our email address. In the third command we are telling Git to use colourful user interface. It is 
still a command line interface, but with the use of colors, it makes Git commands and Git output 
slightly more readable.


### CRLF (aka Carriage Return Line Feed)

Next, let's configure the line endings, or, precisely speaking, *auto carriage return line feed*.
On Linux and Mac system there is a line feed at the end of the line, and on Windows there is a
carriage return and line feed at the end of the line. It may result in a situation, when a
person commits the code to a Git repository, and it looks like every single line of the file
was changed, but in reality the user changed only a couple of lines of the code. Windows kindly
added carriage returns at the end of each line, and as per Git every single line was changed. In
order to avoid this kind of situation, we need to set up auto carriage return line feed.


If you are on Windows use:

    $ git config --global core.autocrlf true

If you are on Linux or Mac use:
    
    $ git config --global core.autocrlf input


### Useful Aliases

Aliases in Git allow users to create their own commands, that normally require less typing
than built-in Git commands and options.

    
Short version of git status:

    $ git config --global alias.s "status -s"

Nice graphical presentation of the git log:

    $ git config --global alias.lg "log --oneline --all --graph --decorate"

The first alias needs to be called using the command:
    
    $ git s

The second alias needs to be called using the command:
    
    $ git lg


### Git Global Configuration File

The git global configuration file is called **.gitconfig**, and on Linux system it can be found
in user's home directory. You can have a look at this file by issuing the command:

    $ cat ~/.gitconfig

If you followed the instructions in this post, your **.gitconfig** is going to look as follows:

    [user]
        name = your_username
        email = your@email.com
    [core]
            autocrlf = input
    [alias]
            s = status -s
            lg = log --oneline --all --graph --decorate


** This is it! Thanks for reading! **
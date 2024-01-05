# how-to-add-line-numbers-and-filename-when-printing-in-python
We all do it. Yes we all use print for debugging. Should we do it? Maybe. Should we feel guilty about it? No!  In fact, printing to the console is a perfectly valid way of debugging. Source: Tips for debugging with print() https://adamj.eu/tech/2021/10/08/tips-for-debugging-with-print/
So it would be great if we could print the file and line number of where the print statement lives.

In the past this has been a complete nightmare. Often you end up calling modules you’ve never heard of from some script found on some dodgy looking site and it all just feel unpythonic and icky.

Wouldn’t it be great if someone had already handled the icky for you?

Enter the Rich formatting library!
The Rich library is built to for writing rich text. You know text with colors and other things like … line numbers!
https://rich.readthedocs.io/en/stable/appendix/colors.html#appendix-colors

Lets get started!
In the virtual environment of your choice – begin by installing Rich.

pip install rich

Now that we have Rich installed. Let’s create a script called printlog.py

And begin by setting up Rich and the Rich Console. The Console is a function that allows you to readily create richly formatted text.

from rich.console import Console

console = Console()

And now we are ready to rock. To print something to the console you call console.log("Your text") and the text will be printed along with the file name and line number that the console.log() statement lives on.

Let’s populate printlog.py with some code.

In line 1 and 3 we are setting up rich. In line 5 we are printing to the console that we are beginning – and we’ve given it the color red. You remember how I said rich allows you to print colors? Well here we are! There are plenty of colours to choose from – as well as all the hex and rgb colors as well (provided your terminal supports them).

Then we run a loop – in practice this would be your code. We print out where we are up to with another console.log() command, run another loop and then print some more.

You should get output much like this:


Notice that not only do we get the filename and line number on the right – but we also get the time (to the second) that the script ran on the left.

All that info for free! And in a really pythonic way.

Wow – what a great library!

Plus console.log() can be used in any python script that prints to the console. I use it in my Django projects all the time.

So check out the Rich console.log() command today!

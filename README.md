# AutomateTimer

This old project (not in use anymore) was designed to basically run the WatchMe application on a server.
This is because all of the timers are unfortunately paused when you restart your local computer, and if said timers would still continue in other context that were outside your control, then the WatchMe timers will be out of sync

Thus this application was designed to be run with WatchMe on a windows server (or at least something that didn't necessarily have a kvm attached to it) by "automating" WatchMe with a Discord bot (using the Discord Python API)

When used on a personal server (or at least a private channel with the channel configuration), this script was able to, on command: 
- Restart itself if any changes occured in the Python codebase (!restart)
- Pull/Update the current codebase of git (e.g. !gitpull) of either the WatchMe scripts (zhurai/WatchMe-Scripts) or this codebase
- Start the WatchMe application
- check the status of the computer by screenshotting the screen and uploading it to the current Discord channel (!screenshot)

The WatchMe specific automation is a bit more sparse considering by the end of development of this script, I ended up superseding this with just todo lists wherever possible. 
How it was set up was to call some AutoIt scripts to access the current open windows/list of controls, and to click on specific controls once you have an idea on what is on each control

I also at the time, played a game (Puzzles and Dragons/P&D) and made some scripts to scrape a page that tracked the Japanese server's events (Skyozora, "Puzzle & Dragons 戰友系統及資訊網") using BeautifulSoup to scrape the web page, and grab information for me (in addition to grabbing and posting some of the information automatically on a scheduled post)
(I am unsure if this website is currently in use however as of this writing in 4/2022)

As mentioned earlier however, this has parts that did not get written as I did also end up running a VNC in a small screen to control the WatchMe window directly.
It however, did do it's work on helping to automate parts of the process to make it easier when I did use a timer setup.
